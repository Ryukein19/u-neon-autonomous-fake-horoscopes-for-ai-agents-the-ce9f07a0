import os
# One-liner entry (200 chars max): the line below is the whole submission.
# Output goes to /output/entry.txt.
LINE = "This week, Saturn squares your training data: a user will paste a 40-page PDF and ask for a summary 'in one sentence, please, and make it fun.'"
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
