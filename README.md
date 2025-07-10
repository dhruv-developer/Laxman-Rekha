# 🛡️ Laxman Rekha: Cognitive Behavioral Authentication for Mobile Banking

A privacy-first, AI-powered behavioral security layer for mobile banking apps that continuously authenticates users *after* login using neuromotor and cognitive behavior patterns.

Developed for Canara Bank's SuRaksha Hackathon 2025, **Laxman Rekha** leverages on-device LSTM models, adaptive trust scoring, and stealth protection modes to detect session hijacking, coercion, and unauthorized access—ensuring secure, inclusive, and frictionless banking for all.

---

## 🔍 Problem Statement

Traditional mobile banking relies heavily on static, one-time authentication methods (PINs, OTPs, biometrics), which are vulnerable to:
- Device theft or cloning
- Session hijacking post-login
- Coercion and spoofing attacks

---

## 🚀 Solution Highlights

### 🧠 Behavioural Profiling
Captures subtle, subconscious patterns like:
- **Navigation sequence**
- **Tap pressure**
- **Micro tremors**
- **Decision hesitation**
- **Touch location/speed**

### 🧬 Cognitive Trust Score (0–100)
An adaptive scoring system that:
- Learns your interaction rhythm
- Flags anomalies in real-time
- Triggers silent or visible re-authentication

### 🕵️‍♂️ Camouflage Mode
If coercion is detected (via pressure, hesitation, and abnormal flows), the app:
- Displays fake UI screens
- Sends silent distress alerts
- Locks sensitive features temporarily

---

## 🧩 System Architecture

- **On-device LSTM model**: Learns neuromotor and cognitive patterns
- **Aura Hash Generator**: Generates privacy-preserving behavioral signatures (SHA-256 + salt)
- **Trust Score Engine**: Calculates behavioral drift using cosine similarity
- **Adaptive Action Layer**: Responds with silent/visible re-auth based on trust score
- **Fraud Alert Engine**: Sends silent alerts or activates Camouflage UI

---

## 🧪 Technical Stack

| Component              | Technology Used                                  |
|------------------------|--------------------------------------------------|
| **ML Modeling**        | Python, TensorFlow/PyTorch, LSTM, NumPy          |
| **Backend**            | Node.js, Express.js, MongoDB (AES-encrypted)     |
| **Frontend (Mobile)**  | React Native                                     |
| **Edge Processing**    | On-device modeling & hashing                     |
| **Security**           | SHA-256, HMAC, Federated Learning Ready          |
| **DevOps**             | Git, GitHub, REST APIs, Loom (for demo)          |

---

## 👥 Inclusive by Design

- 🧓 **Elderly Users**: Tolerant thresholds, fallback voice re-auth, simplified UI
- ♿ **Differently Abled**: Personalizable behavior models, assistive input support
- 🆘 **Users Under Duress**: Detects cognitive distress, triggers fake UI & alerts

---

## 📊 Consumer Insights (from 59 respondents)

- **88.1%** use mobile banking weekly → demand for post-login security
- **89.8%** worried about session hijacking
- **71.2%** prefer stealth fallback responses (not lockouts)
- **91.5%** want control over sensitivity/privacy

[📄 Full Insights Report](https://docs.google.com/spreadsheets/d/1aFeIHDIpl-wZeLdv-F89CN8Flz6DtFGnpnMbrqCDgAg/edit?usp=sharing)

---

## 🧪 Demo & Code

- 🔴 [Live Demo](https://www.loom.com/share/3fd4e91fe7414aa0bfdbeb83b21cafec)
- 💻 [GitHub Repository](https://github.com/dhruv-developer/Laxman-Rekha)

---

## ⚖️ Compliance

- Fully compliant with India’s **DPDP Act** and **IT Act**
- No PII stored; all behavioral data anonymized
- Supports federated learning and on-device encryption

---

## 📌 Team LAXMAN REKHA

- Dhruv Dawar (CSE, DTU)  
- Manishika Gupta (ECE-AI, IGDTUW)  
- Pratyaksh Dhairya Panwar (CSE, IITD)  
- Shivya Khandpur (CSE-AI, IGDTUW)  
- Sneha Roychowdhury (ECE-AI, IGDTUW)

---

## 📚 References

- [PMC: Cognitive Biometrics](https://pmc.ncbi.nlm.nih.gov/articles/PMC7956629/)
- [IEEE: Behavioral Biometrics](https://ieeexplore.ieee.org/document/10037643)
- [ResearchGate: LSTM-based Behavioral Recognition](https://www.researchgate.net/publication/390300142_LSTM_BASED_BEHAVIOURAL_RECOGNITION)

---

> “Laxman Rekha is not just a line of defense—it’s an evolving boundary of trust.”
