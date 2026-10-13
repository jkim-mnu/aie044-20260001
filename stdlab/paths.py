from pathlib import Path

p = Path("data") / "readings.csv"
print("현재 폴더:", Path.cwd())
print("경로:", p)
print("이름:", p.name, "| 확장자 뺀 이름:", p.stem, "| 확장자:", p.suffix)
print("부모 폴더:", p.parent)
print("절대 경로:", p.resolve())
print("있는가:", p.exists())
