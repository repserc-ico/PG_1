import random
num=[0]*7
#出たサイコロの目の回数をカウント
for i in range(0,100):
    dice=random.randint(1,6)
    num[dice]+=1
#サイコロの目の数を表示
for j in range(1,7):
    print(f"{j}:",end="")
    for k in range(1,num[j]+1):
        print("*",end="")
    print("")

