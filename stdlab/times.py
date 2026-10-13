from datetime import datetime

print("지금:", datetime.now())
t = datetime(2026, 10, 14, 9, 30, 0)
print("속성:", t.year, t.month, t.day, t.hour, t.minute)
print("형식 지정:", t.strftime("%Y-%m-%d %H:%M"))

a = datetime.fromisoformat("2026-10-14T09:30:00")
b = datetime.strptime("2026/10/14 09:30", "%Y/%m/%d %H:%M")
print("두 값이 같은가:", a == b, "| 표준 형식:", a.isoformat())
try:
    datetime.strptime("2026-10-14 09:30", "%Y/%m/%d %H:%M")
except ValueError as e:
    print("해석 실패:", e)
