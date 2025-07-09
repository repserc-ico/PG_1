import random

score=5
loop=10
game=1
while game>0:
    
    print(f"\n＊＊第{game}ゲーム＊＊　チャレンジ回数:{loop}回")
    number=random.randint(1,10)
    for i in range(1,loop+1):
        print(f"Challenge:{i}")
        guess=int(input("数を当ててください"))
        if guess==0:
            print("ゲームを中途終了します")
            game=-1
            break
        if number==guess:
            print(f"当たり！正解は{number}でした！")
            score+=10
            loop-=1
            break
        elif number>guess:
            print("数字が小さいです")
            score-=1
        elif number<guess:
            print("数字が大きいです")
            score-=1
        if i==loop:
            print("残念！当たりませんでした！")
            print(f"正解は{number}でした")
            game=-1
    game+=1

print(f"あなたの得点は{score}です")
