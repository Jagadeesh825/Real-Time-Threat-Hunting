Real-Time Threat Hunting and Incident Response Toolkit

This project demonstrates a practical implementation of a basic SOC (Security Operations Center) workflow using Suricata IDS and Python scripting to detect and alert on suspicious network activities in real-time.

👤 Author
Jagadeesh Kumar S
Email: [jagadeesh12699@gmail.com](mailto:jagadeesh12699@gmail.com)  
GitHub: [Jagadeesh825](https://github.com/Jagadeesh825)  
LinkedIn: [Jagadeesh Kumar S](https://www.linkedin.com/in/jagadeesh-kumar-s-98b232150)

🧩 Project Overview

This toolkit is designed to monitor network traffic, detect potential threats using Suricata IDS, and send real-time alerts for high or critical severity incidents.

Features
- Intrusion detection using Suricata IDS.
- Real-time monitoring of Suricata's `eve.json` logs.
- Python script that parses logs and sends email alerts.
- Focused on high/critical severity alerts to reduce noise.
- Helps simulate SOC alerting and response processes.

---

## 🛠️ Technologies Used

| Tool        | Purpose                              |
|-------------|--------------------------------------|
| Suricata    | IDS engine to monitor network traffic|
| Python      | Scripting for parsing and alerting   |
| Linux (Kali)| OS environment for deployment        |
| Mail Utils  | For sending alert emails             |

---

## 🚀 Installation & Setup

### Step 1: Install Suricata

```bash
sudo apt update
sudo apt install suricata -y
````

### Step 2: Configure Logging

Ensure Suricata outputs logs to `/var/log/suricata/eve.json`. Modify `/etc/suricata/suricata.yaml` if needed.

### Step 3: Test Suricata with Sample Traffic

```bash
sudo suricata -i eth0 -l /var/log/suricata
```

Generate some traffic using your browser or tools like `ping`, `nmap`, etc.

---

Python Alert Script

Create a directory:

```bash
sudo mkdir -p /opt/threat-monitor
sudo nano /opt/threat-monitor/email-alert.py
```

Paste the following script:

```python
#!/usr/bin/python3
import json
from datetime import datetime, timedelta
import subprocess

LOG_PATH = "/var/log/suricata/eve.json"
EMAIL = "youremail@example.com"  # Replace with your email

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
```

Give execution permission:

```bash
sudo chmod +x /opt/threat-monitor/email-alert.py
```

Run the script:

```bash
sudo /opt/threat-monitor/email-alert.py
```

---

✅ Output

* Alerts are emailed when high/critical threats are detected.
* Suricata logs are stored in `/var/log/suricata/eve.json`.
* `fast.log`, `stats.log`, and `suricata.log` are also available for analysis.

---
 Learning Objectives

* Understand IDS systems and log monitoring.
* Learn how to automate threat detection workflows.
* Gain practical exposure to cybersecurity tools used in SOC environments.

---

## 📎 License

This project is for educational purposes only. You're free to use and modify it for learning.

---
🤝 Contributing

Pull requests are welcome! If you'd like to contribute ideas or improvements, feel free to fork the repo and submit your suggestions.


