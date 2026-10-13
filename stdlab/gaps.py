from datetime import datetime, timedelta, timezone

t1 = datetime.fromisoformat("2026-10-14T09:00:00")
t2 = datetime.fromisoformat("2026-10-14T09:07:30")
gap = t2 - t1
print("간격:", gap, "| 초:", gap.total_seconds())
print("10분 뒤:", t1 + timedelta(minutes=10))
print("5분 이상인가:", gap >= timedelta(minutes=5))

u = datetime.now(timezone.utc)
print("기준 시간대 시각:", u.isoformat(timespec="seconds"))
kst = timezone(timedelta(hours=9))
print("한국 시각:", u.astimezone(kst).strftime("%Y-%m-%d %H:%M"))
try:
    print(u > t1)
except TypeError as e:
    print("비교 실패:", e)
