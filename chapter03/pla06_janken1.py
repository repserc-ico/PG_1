import random

janken=["","グー","チョキ","パー"]
number=random.randint(1,10)
human_score=0
com_score=0
for i in range(1,11):
    print(f"\nChallenge:{i}")
    com=random.randint(1,3)
    print("じゃんけんの手は何にしますか？")
    human=int(input("グー:1 チョキ:2 パー:3 終了:0 >>"))
    if human==0:
        print("ゲームを途中終了します")
        break
    print(f"コンピュータは{janken[com]}を出しました")
    if human==com:
        print("惜しい！あいこです")
    else:
        if human==1:
            if com==2:
                print("勝ちました！")
                human_score+=1
            else:
                print("負けました！")
                com_score+=1
        elif human==2:
            if com==3:
                print("勝ちました！")
                human_score+=1
            else:
                print("負けました！")
                com_score+=1
        elif human==3:
            if com==1:
                print("勝ちました！")
                human_score+=1
            else:
                print("負けました！")
                com_score+=1
print(f"{human_score}勝{com_score}敗で",end="")
if human_score==com_score:
    print("引き分けでした")
else:
    if human_score>com_score:
        print("あなたの勝ちです！")
    else:
        print("あなたの負けです...") 
