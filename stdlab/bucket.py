from datetime import datetime, timedelta


def bucket_start(t, base, minutes):
    elapsed = int((t - base).total_seconds())
    index = elapsed // (minutes * 60)
    return base + timedelta(minutes=minutes * index)


base = datetime.fromisoformat("2026-10-14T09:00:00")
for s in ["09:09:59", "09:10:00", "09:19:59", "09:20:00"]:
    t = datetime.fromisoformat("2026-10-14T" + s)
    print(s, "-> 구간 시작", bucket_start(t, base, 10).strftime("%H:%M"))
