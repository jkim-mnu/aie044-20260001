from pathlib import Path


def load(path="data/readings.csv"):
    rows = []
    for line in Path(path).read_text(encoding="utf-8").splitlines()[1:]:
        t, sensor, v = line.split(",")
        rows.append({"timestamp": t, "sensor_id": sensor, "value": float(v)})
    return rows
