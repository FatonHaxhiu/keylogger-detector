# 🔐 Keylogger Detector

![CI](https://github.com/YOUR_USERNAME/keylogger-detector/actions/workflows/test-detector.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A safe, educational Python tool that simulates the detection of potential keyloggers in a Linux (WSL) environment. Designed to help understand basic cybersecurity monitoring, this tool scans for:

- Suspicious running processes (e.g., containing `key`, `log`, `input`)
- Unauthorized access to raw keyboard/mouse input devices (`/dev/input/*`)

> ⚠️ No actual keylogging is performed. This tool **does not contain or run any malicious code.**

---

## 🛠️ How It Works

The project has two main detectors:

1. **Process Scanner**  
   Scans all running processes for suspicious keywords in their command line.

2. **Raw Input Access Checker**  
   Uses `lsof` to check if any process is reading from Linux input devices.

---

## 🧪 How to Test It

### ▶️ Local Test (WSL or Linux)

```bash
git clone https://github.com/YOUR_USERNAME/keylogger-detector.git
cd keylogger-detector
pip install -r requirements.txt

# Run process detection
python3 detector/detect_suspicious_processes.py

# Run input access check (needs sudo)
sudo python3 detector/check_raw_input_access.py

# Run in Docker
```bash
docker build -t keylogger-detector .
docker run --rm --privileged keylogger-detector

📄 License
This project is licensed under the MIT License. See LICENSE for details.