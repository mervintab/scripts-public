import json
import re
import sys
import os

def parse_log_file(filepath):
    with open(filepath, 'r') as file:
        content = file.read()

    # Split log entries by two or more newlines
    raw_entries = re.split(r'\n\s*\n', content.strip())
    parsed_entries = []

    for entry in raw_entries:
        log_data = {}
        lines = entry.strip().split('\n')
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                log_data[key.strip()] = value.strip()
        parsed_entries.append(log_data)

    return parsed_entries

def write_to_json(data, output_path):
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 log_to_json.py <log_file_path>")
        sys.exit(1)

    log_file = sys.argv[1]

    if not os.path.isfile(log_file):
        print(f"Error: File '{log_file}' does not exist.")
        sys.exit(1)

    output_file = "output.json"
    log_data = parse_log_file(log_file)
    write_to_json(log_data, output_file)
    print(f"✅ Successfully converted {len(log_data)} entries to '{output_file}'.")

if __name__ == "__main__":
    main()
