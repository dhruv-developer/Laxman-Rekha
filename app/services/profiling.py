import numpy as np
from datetime import datetime
from typing import List, Dict

def extract_features(events: List[Dict]) -> Dict:
    if not events:
        raise ValueError("No events provided.")

    # Sort by timestamp (ensure timestamps are datetime objects)
    try:
        events.sort(key=lambda e: e["timestamp"])
    except Exception as e:
        raise ValueError(f"Invalid or missing timestamp in events: {e}")

    # 1. Hesitation Signature
    t0 = next((e["timestamp"] for e in events if e.get("event_type") == "app_open"), None)
    t1 = next((e["timestamp"] for e in events if e.get("event_type") == "tap"), None)

    if not t0 or not t1:
        hesitation = 0.0  # or float("nan")
    else:
        try:
            hesitation = (t1 - t0).total_seconds()
        except Exception:
            hesitation = 0.0

    # 2. Tap Pressure Curve
    pressures = [
        e["details"]["pressure"]
        for e in events
        if e.get("event_type") == "tap"
        and isinstance(e.get("details"), dict)
        and "pressure" in e["details"]
        and isinstance(e["details"]["pressure"], (int, float))
    ]
    tap_mean = float(np.mean(pressures)) if pressures else 0.0
    tap_std = float(np.std(pressures)) if pressures else 0.0

    # 3. Hover Fingerprint
    hovers = [
        e["details"]["duration"]
        for e in events
        if e.get("event_type") == "hover"
        and isinstance(e.get("details"), dict)
        and "duration" in e["details"]
        and isinstance(e["details"]["duration"], (int, float))
    ]
    hover_mean = float(np.mean(hovers)) if hovers else 0.0

    # 4. Tremor Frequency (sensor jitter std)
    mags = []
    for e in events:
        if e.get("event_type") == "sensor" and isinstance(e.get("details"), dict):
            a = e["details"].get("accelerometer", {})
            g = e["details"].get("gyroscope", {})
            if all(k in a for k in ("x", "y", "z")) and all(isinstance(a[k], (int, float)) for k in ("x", "y", "z")):
                mags.append(np.linalg.norm([a["x"], a["y"], a["z"]]))
            if all(k in g for k in ("x", "y", "z")) and all(isinstance(g[k], (int, float)) for k in ("x", "y", "z")):
                mags.append(np.linalg.norm([g["x"], g["y"], g["z"]]))
    tremor_std = float(np.std(mags)) if mags else 0.0

    # 5. Intent Drift & Switchback Loops
    screens = [
        e["details"]["screen"]
        for e in events
        if e.get("event_type") in ("tap", "swipe", "back")
        and isinstance(e.get("details"), dict)
        and "screen" in e["details"]
    ]
    unique_screens = len(set(screens)) if screens else 0
    loops = sum(1 for i in range(2, len(screens)) if screens[i] == screens[i - 2]) if len(screens) >= 3 else 0

    # 6. Contextual Anchors (location)
    locs = [
        e["details"]["location"]
        for e in events
        if e.get("event_type") == "location"
        and isinstance(e.get("details"), dict)
        and "location" in e["details"]
        and isinstance(e["details"]["location"], dict)
    ]
    if locs:
        latest_loc = locs[-1]
        lat = float(latest_loc.get("lat", 0.0))
        lng = float(latest_loc.get("lng", 0.0))
    else:
        lat = lng = 0.0

    # 7. Time of Day & Battery
    times = [
        e["timestamp"].hour + e["timestamp"].minute / 60
        for e in events
        if isinstance(e.get("timestamp"), datetime)
    ]
    time_of_day = float(np.mean(times)) if times else 0.0

    bats = [
        e["details"]["battery"]
        for e in events
        if e.get("event_type") == "battery"
        and isinstance(e.get("details"), dict)
        and "battery" in e["details"]
        and isinstance(e["details"]["battery"], (int, float))
    ]
    battery = float(np.mean(bats)) if bats else 0.0

    return {
        "hesitation": hesitation,
        "tap_mean": tap_mean,
        "tap_std": tap_std,
        "hover_mean": hover_mean,
        "tremor_std": tremor_std,
        "intent_drift": unique_screens,
        "switchback_loops": loops,
        "location_lat": lat,
        "location_lng": lng,
        "time_of_day": time_of_day,
        "battery": battery,
    }
