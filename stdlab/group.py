from itertools import groupby
from load import load

rows = load()
key = lambda r: r["sensor_id"]
print("정렬 전 묶음 개수:", len(list(groupby(rows, key=key))))

rows.sort(key=key)
print("정렬 후 묶음 개수:", len(list(groupby(rows, key=key))))
for sensor, group in groupby(rows, key=key):
    print(sensor, len(list(group)), "개")

top = sorted(rows, key=lambda r: r["value"], reverse=True)[:3]
print("값이 큰 3개:", [(r["sensor_id"], r["value"]) for r in top])
