import random

number=random.randint(1,10)

for i in range(1,11):
    print(f"Challenge:{i}")
    guess=int(input("数を当ててください"))
    if number==guess:
        print(f"当たり！正解は{number}でした！")
        break
    elif number>guess:
        print("数字が小さいです")
    elif number<guess:
        print("数字が大きいです")
    if i==10:
        print("残念！当たりませんでした！")
        print(f"正解は{number}でした")

