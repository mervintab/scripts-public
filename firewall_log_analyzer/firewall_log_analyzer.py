import json
import re
import matplotlib.pyplot as plt
from collections import Counter

# === Step 1: Log Parsing ===
def parse_log(file_path, output_path):
    log_entries = []
    pattern = re.compile(r"(?P<timestamp>\S+) (?P<src_ip>\S+) (?P<dst_ip>\S+) (?P<action>\S+) (?P<port>\d+)")

    with open(file_path, "r") as file:
        for line in file:
            match = pattern.search(line)
            if match:
                log_entries.append(match.groupdict())

    with open(output_path, "w") as outfile:
        json.dump(log_entries, outfile, indent=2)

    print(f"Parsed {len(log_entries)} log entries and saved to {output_path}.")

# === Step 2: Visualization ===
def visualize_top_blocked_ips(json_path):
    with open(json_path) as f:
        logs = json.load(f)

    blocked_ips = [log['src_ip'] for log in logs if log['action'].upper() == 'BLOCK']
    ip_counter = Counter(blocked_ips).most_common(10)

    if not ip_counter:
        print("No blocked IPs found.")
        return

    ips, counts = zip(*ip_counter)
    plt.figure(figsize=(10, 6))
    plt.bar(ips, counts)
    plt.title("Top 10 Blocked Source IPs")
    plt.xlabel("Source IP")
    plt.ylabel("Blocked Attempts")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# === Main Execution Example ===
if __name__ == "__main__":
    parse_log("logs/sample_firewall_log.txt", "parsed/parsed_output.json")
    visualize_top_blocked_ips("parsed/parsed_output.json")
