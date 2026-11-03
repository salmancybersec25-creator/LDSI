# Local Device Security Inventory (LDSI)

A Python-based defensive security tool that collects basic system information and generates a professional JSON inventory report. 

## 📌 Project Objective
In cybersecurity, you cannot defend what you do not know exists. Asset inventory is the first step of any security audit, penetration test, or compliance check. LDSI provides a lightweight, read-only snapshot of a local machine's system and network configuration.

## ✨ Features (v1.0)
- Detects the local hostname and operating system version.
- Detects the installed Python version.
- Inventories all local network adapters (IPv4 addresses and subnet masks).
- Exports the findings into a structured, machine-readable JSON report.

## 🛠️ Security Findings & Lessons Learned
During development, the following real-world security concepts were observed and handled:
- **Stale DNS vs. Live State:** Initial attempts to gather IP addresses via `socket.gethostbyname_ex()` returned stale DNS cache data. This was resolved by switching to `psutil.net_if_addrs()` to read the live kernel adapter table.
- **APIPA Addresses:** The tool correctly identifies `169.254.x.x` addresses, indicating DHCP failure on disconnected adapters.
- **Data Sanitization:** `.gitignore` is strictly configured to ensure real network configurations and generated reports are never committed to public repositories.

## 🚀 Installation & Usage
1. Clone the repository:
   `git clone https://github.com/salmancybersec25-creator/LDSI.git`
2. Navigate into the directory and create a virtual environment:
   `python -m venv venv`
3. Activate the environment (Windows):
   `venv\Scripts\activate`
4. Install dependencies:
   `pip install -r requirements.txt`
5. Run the tool:
   `python main.py`

## 🗺️ Future Roadmap
- **v1.1:** Implement IP classification (Private, Loopback, APIPA).
- **v2.0:** Security Configuration Checks (Windows Firewall & Defender status).
- **v3.0:** Network Asset Inventory tracking.
- **v4.0:** Log Analysis (parsing event logs for anomalies).

## ⚠️ Disclaimer
This tool is intended for **educational and defensive purposes only**. It is designed to be run exclusively on machines you own or have explicit authorization to audit.

---
*Created by [Mohammad Salman] as part of a cybersecurity portfolio.*