import statistics
from itertools import islice, pairwise
from load import load

rows = load()
for r in islice(rows, 2):
    print(r)
diffs = [round(b["value"] - a["value"], 2) for a, b in pairwise(rows)]
print("변화량 앞 5개:", diffs[:5])

values = [r["value"] for r in rows]
print("평균:", round(statistics.mean(values), 2))
print("중앙값:", statistics.median(values))
print("표준편차:", round(statistics.stdev(values), 2))
try:
    statistics.stdev([25.0])
except statistics.StatisticsError as e:
    print("계산 실패:", e)
