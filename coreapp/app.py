# imports
from flask import Flask, request, jsonify, render_template, g
import sqlite3

# define the app
app = Flask(__name__)

# database
DATABASE = "/app/data/telemetry.db"

def init_db():
    db = sqlite3.connect(DATABASE)
    db.execute("""
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            rpm INTEGER,
            coolant_temp_c REAL,
            fuel_level_pct REAL
        )
    """)
    db.commit()
    db.close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# route handlers
# home route
@app.route('/')
def home():
    return "Core App: Root OK"

# api route
@app.route("/api", methods=["POST", "GET"])
def api():
    if request.method == "POST":
        data = request.get_json(force=True)

        db = get_db()
        db.execute(
            """
            INSERT INTO telemetry (timestamp, rpm, coolant_temp_c, fuel_level_pct)
            VALUES (?, ?, ?, ?)
            """,
            (
                data["timestamp"],
                data.get("rpm"),
                data.get("coolant_temp_c"),
                data.get("fuel_level_pct")
            )
        )
        db.commit()

        return jsonify({"status": "ok", "msg": "Data written to database"})

    return jsonify({"status": "ready", "msg": "Send a POST with vehicle telemetry"})

# data route
@app.route("/data", methods=["GET"])
def get_data():
    db = get_db()
    cursor = db.execute("""
        SELECT timestamp, rpm, coolant_temp_c, fuel_level_pct
        FROM telemetry
        ORDER BY timestamp ASC
    """)
    rows = cursor.fetchall()

    # Convert to list of dicts
    results = [
        {
            "timestamp": row[0],
            "rpm": row[1],
            "coolant_temp_c": row[2],
            "fuel_level_pct": row[3]
        }
        for row in rows
    ]

    return jsonify(results)

# dashboard route
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# main
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)