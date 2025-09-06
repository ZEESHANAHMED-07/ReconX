import os
import json
import nmap
import webbrowser
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

# ==============================
# Setup paths
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "reports")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# Ensure reports folder exists
os.makedirs(REPORT_DIR, exist_ok=True)


# ==============================
# Save JSON Report
# ==============================
def save_json_report(target, mode, results):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(REPORT_DIR, f"scan_{mode}_{target.replace('/', '_')}_{timestamp}.json")

    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

    print(f"[+] JSON Report saved to {filename}")


# ==============================
# Save HTML Report
# ==============================
def save_html_report(target, mode, results):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("report.html")

    html_output = template.render(
        target=target,
        mode=mode,
        date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        results=results
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(REPORT_DIR, f"scan_{mode}_{target.replace('/', '_')}_{timestamp}.html")

    with open(filename, "w") as f:
        f.write(html_output)

    print(f"[+] HTML Report saved to {filename}")

    # Open in default browser
    webbrowser.open(f"file://{filename}")


# ==============================
# Run Scan
# ==============================
def scan_target(target, mode="quick"):
    nm = nmap.PortScanner()

    print(f"[+] Running {mode} scan on {target}...")

    try:
        if mode == "quick":
            nm.scan(target, arguments="-T4 -F")
        elif mode == "full":
            nm.scan(target, arguments="-T4 -p-")
        elif mode == "vuln":
            nm.scan(target, arguments="--script vuln")
        else:
            print("[-] Unknown scan mode. Use: quick | full | vuln")
            return
    except Exception as e:
        print(f"[-] Scan failed: {e}")
        return

    results = nm._scan_result  # raw results

    # Save reports
    save_json_report(target, mode, results)
    save_html_report(target, mode, results)


# ==============================
# CLI Entry Point
# ==============================
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ReconX - Automated Nmap Scanner")
    parser.add_argument("target", help="Target IP or range (e.g., 192.168.1.1 or 192.168.1.0/24)")
    parser.add_argument("mode", choices=["quick", "full", "vuln"], help="Scan mode: quick, full, vuln")

    args = parser.parse_args()

    scan_target(args.target, args.mode)
