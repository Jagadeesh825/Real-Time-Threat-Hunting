import json
from collections import defaultdict

LOG_FILE = "/var/log/suricata-live/eve.json"

def summarize_alerts():
    severity_count = defaultdict(int)
    total = 0

    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if "alert" in data:
                        severity = data["alert"].get("severity", "unknown")
                        severity_count[severity] += 1
                        total += 1
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        print(f"Error: {LOG_FILE} not found.")
        return

    print("\n🛡️  Alert Summary")
    print("-" * 30)
    for severity, count in sorted(severity_count.items()):
        print(f"Severity {severity}: {count} alerts")
    print("-" * 30)
    print(f"Total alerts: {total}\n")

if __name__ == "__main__":
    summarize_alerts()
