import random

def judge(game):	#勝ち負け判定と勝敗記録
    win=False
    if game[0]==3 and game[1]==1:
           win=True
    else:
        if game[1]==game[0]+1:
            win=True
    if win==True:
        print("あなたの勝ちです")
        game[2]+=1
    else:
        print("あなたの負けです")
        game[3]+=1
    return game

janken=["","グー","チョキ","パー"]
bout=[0,0,0,0]	#勝負と勝敗記録[人間の手,コンピュータの手,人間の勝数,コンピュータの勝数]
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
        bout[0]=human
        bout[1]=com
        bout=judge(bout)

print(f"{bout[2]}勝{bout[3]}敗で",end="")
if bout[2]==bout[3]:
    print("引き分けでした")
else:
    if bout[2]>bout[3]:
        print("あなたの勝ちです！")
    else:
        print("あなたの負けです...")
#print(bout)	#デバッグ用 
