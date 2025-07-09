engl=int(input("英語の点数を入力してください>"))
math=int(input("数学の点数を入力してください>"))
score=""
if engl>=90 and math>=90:
    score="S"
elif engl>=70 or math>=70:
    score="A"
elif engl>=50 or math>=50:
    score="B"
elif engl<50 and math<50:
    score="C"

print(f"あなたの成績は{score}です")
