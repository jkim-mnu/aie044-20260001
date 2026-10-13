from collections import Counter, defaultdict, deque
from load import load

rows = load()
c = Counter(r["sensor_id"] for r in rows)
print("센서별 개수:", c)
print("가장 많은 두 센서:", c.most_common(2))

groups = defaultdict(list)
for r in rows:
    groups[r["sensor_id"]].append(r["value"])
print("분류한 센서:", sorted(groups))

window = deque(maxlen=3)
for r in rows[:5]:
    window.append(r["value"])
    print("최근 값", list(window), "평균", round(sum(window) / len(window), 2))
