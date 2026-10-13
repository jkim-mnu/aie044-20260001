from pathlib import Path

out = Path("out")
out.mkdir(parents=True, exist_ok=True)
for name in ["a.txt", "b.txt", "memo.md"]:
    (out / name).write_text(name + " 내용\n", encoding="utf-8")

for f in sorted(out.glob("*.txt")):
    print(f.name, "->", f.read_text(encoding="utf-8").strip())
print("하위 폴더까지:", [str(f) for f in sorted(Path(".").rglob("*.md"))])
