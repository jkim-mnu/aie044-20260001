import subprocess
import sys

result = subprocess.run([sys.executable, "stdlab/summary.py"],
                        capture_output=True, text=True, encoding="utf-8")
rows = [line.split() for line in result.stdout.splitlines()[2:] if line.strip()]
problems = []
sensors = [row[0] for row in rows]
if sensors != sorted(sensors):
    problems.append(f"규칙 4항 위반: 센서가 이름순이 아님 {sensors}")
for row in rows:
    if len(row[4].split(".")[1]) != 2:
        problems.append(f"규칙 3항 위반: 평균 {row[4]}이 소수 둘째 자리가 아님")
for p in problems:
    print(p)
print("검사 통과" if not problems else f"검사 실패 {len(problems)}건")
sys.exit(1 if problems else 0)
