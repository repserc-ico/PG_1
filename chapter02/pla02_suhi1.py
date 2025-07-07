year=input("生まれた年を入力してください")
month=input("生まれた月を入力してください")
day=input("生まれた日を入力してください")
number=0

for i in range(0,4):
    number+=int(year[i])

if int(month)<10:
    number+=int(month)
else:
    for i in range(0,2):
        number+=int(month[i])

if int(day)<9:
    number+=int(day)
else:
    for i in range(0,2):
        number+=int(day[i])

tmp=str(number)
if number>9:
    number=0
    for i in range(0,2):
        number+=int(tmp[i])

print(f"あなたの運命数は{number}です")
