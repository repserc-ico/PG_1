import random

score=5
loop=10
game=0
repeat=True
while repeat:
    game+=1
    print(f"\n＊＊第{game}ゲーム＊＊　チャレンジ回数:{loop}回")
    number=random.randint(1,10)
    for i in range(1,loop+1):
        print(f"Challenge:{i}")
        guess=int(input("数を当ててください"))
        if guess==0:
            print("ゲームを中途終了します")
            repeat=False
            break
        if number==guess:
            print(f"当たり！正解は{number}でした！")
            score+=10
            loop-=1
            if loop==0:
                print("素晴らしい！パーフェクトゲームです！")
                score+=100
                repeat=False
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
            print("ゲームオーバーです")
            repeat=False

print(f"あなたの得点は{score}です")
