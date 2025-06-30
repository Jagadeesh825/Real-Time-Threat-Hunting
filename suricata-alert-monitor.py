import json
import time
import os

log_file = "/var/log/suricata-live/fast.log"
output_file = "/var/log/suricata-live/incident.log"

def monitor_fast_log():
    print("🔍 Monitoring Suricata Alerts...")
    with open(log_file, "r") as f:
        f.seek(0, os.SEEK_END)  # Move to end of file
        while True:
            line = f.readline()
            if line:
                print("🚨 ALERT:", line.strip())
                with open(output_file, "a") as out:
                    out.write(line)
            else:
                time.sleep(1)

if __name__ == "__main__":
    monitor_fast_log()
