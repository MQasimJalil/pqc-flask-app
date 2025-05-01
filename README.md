# 🔐 Post-Quantum Cryptography Flask App (Kyber512)

This project demonstrates secure encryption and decryption using **Post-Quantum Cryptography** (PQC) through a **Flask web application**. It uses **Kyber512 (ML-KEM)**, a NIST finalist algorithm, along with **AES-GCM** for message encryption via a hybrid cryptosystem.

---

## 🚀 Features

- 🔑 Key generation using Kyber512 (ML-KEM)
- 🧾 Message encryption using AES-GCM with a Kyber-derived shared secret
- 🔓 Decryption to retrieve the original message
- 🖥️ Clean Bootstrap 5 web interface
- 🛡️ Secure headers via Flask-Talisman
- 🧪 Minimal, readable codebase with simple logic

---

## 🛠 Technologies Used

| Component     | Tech                          |
|---------------|-------------------------------|
| Backend       | Python 3, Flask               |
| PQC Library   | `kyber_py`                    |
| Symmetric Enc | AES-GCM (from `cryptography`) |
| Frontend      | HTML, Bootstrap 5             |
| Security      | Flask-Talisman, `.env`        |

---

## 📁 Project Structure

pqc-flask-app/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── pqc.py            
│   ├── templates/
│   │   ├── index.html
│   ├── static/
│       ├── bootstrap.min.css
├── requirements.txt
├── run.py
├── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/MQasimJalil/pqc-flask-app.git
cd pqc-flask-app

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the app
python run.py

### 4. Open web app
Go to your browser and visit http://localhost:5000

