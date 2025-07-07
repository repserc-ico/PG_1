astro=["","山羊座","水瓶座","魚座","牡羊座","牡牛座","双子座","蟹座","獅子座","乙女座","天秤座","蠍座","射手座"]
month=int(input("生まれた月を入力してください"))
day=int(input("生まれた日を入力してください"))

if month==1 and day>=20: #山羊座だけど
    month+=1    #水瓶座にする
elif month==2 and day>=19: #水瓶座
    month+=1
elif month==3 and day>=21: #魚座
    month+=1
elif month==4 and day>=20: #牡羊座
    month+=1
elif month==5 and day>=21: #牡牛座
    month+=1
elif month==6 and day>=22: #双子座
    month+=1
elif month==7 and day>=23: #蟹座
    month+=1
elif month==8 and day>=23: #獅子座
    month+=1
elif month==9 and day>=23: #乙女座
    month+=1
elif month==10 and day>=24: #天秤座
    month+=1
elif month==11 and day>=23: #蠍座
    month+=1
elif month==12 and day>=22: #射手座
    month=1

print(f"あなたの星座は{astro[month]}です")
