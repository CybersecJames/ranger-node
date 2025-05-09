import requests
import random
from datetime import datetime, timezone
import time

API_URL = "http://localhost:8080/api"  # Adjust if hitting container directly

def simulate_fuel_level(start=100.0, drop_per_loop=0.5, min_level=0.0):
    current = start
    while current > min_level:
        yield round(current, 1)
        current -= drop_per_loop
    while True:
        yield min_level

fuel_gen = simulate_fuel_level()

def simulate_coolant_temp(start=85.0, max_temp=102.0, noise=0.3):
    current = start
    while True:
        # Simulate gradual warm-up with soft random variation
        if current < max_temp:
            current += random.uniform(0.1, 0.4)  # slow rise
        else:
            # Add tiny fluctuation once at cruising temp
            current += random.uniform(-noise, noise)
        yield round(current, 1)

coolant_gen = simulate_coolant_temp()

def generate_fake_obd():
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": "ranger_node",
        "rpm": random.randint(700, 1200),
        "coolant_temp_c": next(coolant_gen),
        "fuel_level_pct": next(fuel_gen),
        "status": "normal"
    }

while True:
    data = generate_fake_obd()
    print(f"Posting: {data}")
    try:
        res = requests.post(API_URL, json=data)
        print(f"Response: {res.status_code}")
    except Exception as e:
        print(f"Failed to post: {e}")
    time.sleep(4)
