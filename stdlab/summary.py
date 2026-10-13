import statistics
from collections import defaultdict
from pathlib import Path

values = defaultdict(list)
with Path("data/readings.csv").open(encoding="utf-8") as f:
    next(f)
    for line in f:
        t, sensor, v = line.strip().split(",")
        values[sensor].append(float(v))

print(f"{'sensor':<8}{'count':>6}{'min':>8}{'max':>8}{'mean':>8}")
print("-" * 38)
for sensor in sorted(values):
    vs = values[sensor]
    print(f"{sensor:<8}{len(vs):>6}{min(vs):>8.2f}{max(vs):>8.2f}{statistics.mean(vs):>8.1f}")
