# Log to JSON Converter

This is a simple Python script to convert structured log files into JSON format.

## Features
- Parses logs with multiple fields per entry
- Outputs a clean JSON array of log entries
- Easy to adapt to different log formats

## How to Use

1. Place your log file in the same directory as the script.
2. Run the script:

```bash
python3 log_to_json.py sampleLog.log
```

3. The output will be saved as `output.json`.

## Example

**Log Input:**
```
Date/Time: 2023-12-20 18:45:22
Web Server: 192.168.1.102
...
```

**JSON Output:**
```json
{
  "Date/Time": "2023-12-20 18:45:22",
  "Web Server": "192.168.1.102",
  ...
}
```

## License

MIT
