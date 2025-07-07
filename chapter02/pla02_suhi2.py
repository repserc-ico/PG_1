year=int(input("生まれた年を入力してください"))
month=int(input("生まれた月を入力してください"))
day=int(input("生まれた日を入力してください"))
number=(year+month+day)%9
if number==0:
    number=9

print(f"あなたの運命数は{number}です")
