# ReconX 🔍
**Automated Nmap Scanner with JSON & HTML Reports**

ReconX is a lightweight Python tool that automates **Nmap scans** and generates clean reports in **JSON** and **hacker-style HTML**.  
Built for penetration testers, bug bounty hunters, and sysadmins who want fast recon with reports they can share.  

---

## ✨ Features
- 🚀 Quick, Full, and Vulnerability scans  
- 📊 JSON report generation  
- 🕶 Hacker-style HTML report with color-coded results  
- 🗂 Automatic timestamped reports stored in `reports/`  
- ⚡ Simple CLI interface  

---

## 📦 Installation
```bash
# Clone repo
git clone https://github.com/ZEESHANAHMED-07/ReconX.git
cd ReconX
```
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate
```
```bash
# Install dependencies
pip install -r requirements.txt
```
⚡ Usage

Run the scanner with:
```bash
python3 autoscan.py <target> <mode>
```

Example scans:
```bash
# Quick scan on localhost
python3 autoscan.py 127.0.0.1 quick

# Full scan on single host
python3 autoscan.py 192.168.1.1 full

# Quick scan on local subnet
python3 autoscan.py 192.168.1.0/24 quick

# Vulnerability scan on scanme.nmap.org
python3 autoscan.py scanme.nmap.org vuln
```
📁 Reports

Reports are saved automatically in the reports/ folder:

JSON → scan_<mode>_<target>_<timestamp>.json

HTML → scan_<mode>_<target>_<timestamp>.html

Example output:


🛠 Roadmap

 Add live progress bar for scans

 Export reports to PDF

 AI-powered scan analysis & recommendations

 Integration with other recon tools (Nikto, Gobuster, etc.)

⚔️ Disclaimer

ReconX is for educational and authorized security testing only.
Do not use against systems you don’t own or have explicit permission to test.


