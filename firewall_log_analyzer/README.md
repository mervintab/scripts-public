# 🔥 Firewall Log Analyzer

A lightweight Python tool for parsing and analyzing firewall logs. It converts raw log files into structured JSON format and visualizes blocked IPs to help identify potential intrusion attempts or suspicious activity.

---

## 🧠 Features
- Parses log files using regex into structured JSON
- Identifies and counts blocked source IPs
- Visualizes the top 10 blocked IPs using bar charts
- Customizable and beginner-friendly

---

## 📂 Sample Log Format
```
2025-03-29T12:45:22Z 192.168.1.10 10.0.0.1 BLOCK 443
2025-03-29T12:45:23Z 192.168.1.11 10.0.0.1 ALLOW 80
2025-03-29T12:45:24Z 192.168.1.10 10.0.0.1 BLOCK 22
```
Format: `timestamp src_ip dst_ip action port`

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/mervintab/firewall-log-analyzer.git
cd firewall-log-analyzer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Script
```bash
python firewall_log_analyzer.py
```

### 4. View the Chart
A matplotlib chart will display the top 10 blocked source IPs.

---

## 📁 Directory Structure
```
firewall-log-analyzer/
├── firewall_log_analyzer.py
├── logs/
│   └── sample_firewall_log.txt
├── parsed/
│   └── parsed_output.json
├── requirements.txt
└── README.md
```

---

## 📊 Example Output
> You can include a screenshot here once the graph is generated. 

---

## 🤝 Contributions
Feel free to fork this repo, suggest improvements, or open a pull request!

---

## 🧑‍💻 Author
**Mervin Tabernero**  
[LinkedIn](https://www.linkedin.com/in/mervintab/)
