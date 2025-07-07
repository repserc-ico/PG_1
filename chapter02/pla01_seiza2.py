astro=["","山羊座","水瓶座","魚座","牡羊座","牡牛座","双子座","蟹座","獅子座","乙女座","天秤座","蠍座","射手座","山羊座"]
skip=[0,20,19,21,20,21,22,23,23,23,24,23,22]
month=int(input("生まれた月を入力してください"))
day=int(input("生まれた日を入力してください"))
seiza=month

for i in range(1,13):
    if month==i and day>=skip[month]:
        seiza+=1

print(f"あなたの星座は{astro[seiza]}です")
