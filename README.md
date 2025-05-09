# RangerNode

**RangerNode** is a containerized, real-time vehicle telemetry system designed for Raspberry Pi deployment and local garage analysis. It reads OBD-II data, logs it into a structured SQLite database, and visualizes it through a live-updating Flask + Chart.js dashboard. Future versions will integrate a local LLM (e.g. Mistral 7B) to generate natural language diagnostics based on drive history.

---

## 🚗 What It Does

- 📡 Collects real-time vehicle telemetry (e.g., RPM, coolant temp, fuel level) via OBD-II
- 🧠 Logs data into a lightweight SQLite database, containerized via Flask
- 📊 Serves a web dashboard for live telemetry visualization
- 🛰️ Designed for in-vehicle Pi deployment with post-drive sync to a garage “mainframe”
- 🧾 Future: AI-generated diagnostics via locally hosted LLM (no cloud dependency)

---

## 🧱 Project Structure

```bash
ranger-node/
├── coreapp/            # Flask app container (runs on Pi)
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates/
│       └── dashboard.html
├── garage-server/      # Future home for Mistral + diagnostics
├── scripts/            # Sync logic (Pi → garage)
├── README.md
├── ROADMAP.md
├── .gitignore
└── LICENSE
```

---

## 🚀 Quick Start

1. Clone and build the core Flask app:

```bash
cd coreapp
podman build -t coreapp .
podman run -dit -p 5000:5000 --name coreapp coreapp
```

2. Post simulated data to `/api`:

```json
{
  "timestamp": "2025-05-09T21:33:00Z",
  "rpm": 950,
  "coolant_temp_c": 89.7,
  "fuel_level_pct": 64.0
}
```

3. Visit `/dashboard` to view live data.

---

## 🛠️ Technologies Used

- Python 3 + Flask
- SQLite
- Chart.js
- Podman (or Docker)
- Planned: Mistral 7B via local inference

---

## 🧭 Project Vision

RangerNode is the first step toward a fully local, intelligent vehicle diagnostic assistant—running entirely on personal hardware. It’s meant to feel like a trusted garage companion, not a cloud service. Over time, it will grow to include real diagnostics, trend analysis, and a natural voice interface powered by local LLMs.

---

## 📄 License

MIT License. Use, fork, and improve.