#素数を算出
num = [True] * 101
prime = []
num[0] = num[1] = False #ゼロと1は素数でないので除外
#エラトステネスのふるい
for i in range(2, 101):
    if i == 2 or i == 3 or i == 5 or i == 7:
        pass
    else:
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            num[i] = False
#ふるいから素数のみを取り出す
for j in range(1, 101):
    if num[j] == True:
        prime.append(j)
#素数のリストを10個ごとに改行して表示する
count=0
for k in prime:
    count+=1
    print(f"{k},", end="")
    if count==10:
        print("")
        count=0
print("")


