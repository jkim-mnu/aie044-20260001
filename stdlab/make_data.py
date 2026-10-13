import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)
start = datetime(2026, 10, 14, 9, 0, 0)
lines = ["timestamp,sensor_id,value"]
for i in range(60):
    t = start + timedelta(seconds=37 * i)
    sensor = random.choice(["T01", "T02", "T03"])
    value = round(random.uniform(20, 30), 2)
    lines.append(f"{t.isoformat()},{sensor},{value}")

Path("data").mkdir(exist_ok=True)
Path("data/readings.csv").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("저장한 줄 수:", len(lines) - 1)
