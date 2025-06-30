#!/usr/bin/python3

import json
from datetime import datetime, timedelta
import subprocess

LOG_PATH = "/var/log/suricata/eve.json"
EMAIL = "jagadeesh12699@gmail.com"  # <-- Replace with your actual email

def send_email(subject, message):
    subprocess.run(['mail', '-s', subject, EMAIL], input=message.encode())

with open(LOG_PATH, 'r') as file:
    for line in file:
        try:
            entry = json.loads(line)
            if entry.get("event_type") == "alert":
                ts = datetime.strptime(entry["timestamp"], "%Y-%m-%dT%H:%M:%S.%f%z")
                if ts > datetime.now(ts.tzinfo) - timedelta(hours=1):
                    severity = entry["alert"]["severity"]
                    if severity <= 2:  # High (1) or Medium (2)
                        msg = f"ALERT:\n{entry['alert']['signature']}\nSeverity: {severity}\nSrc: {entry['src_ip']}:{entry.get('src_port', '')} -> Dst: {entry['dest_ip']}:{entry.get('dest_port', '')}"
                        send_email("⚠️ Suricata High-Severity Alert", msg)
        except Exception:
            continue
