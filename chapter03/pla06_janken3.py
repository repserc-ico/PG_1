import random

g_human=0
g_com=0
g_janken=["","グー","チョキ","パー"]

def judge(hand):	#勝ち負け判定
    global g_human, g_com
    win=False
    com_hand=random.randint(1,3)	#ここでコンピュータが手を出す
    print(f"あなたは{g_janken[hand]}、コンピュータは{g_janken[com_hand]}を出しました")
    if hand == com_hand:
        print("あいこです")
        return
    else:
        if hand==3 and com_hand==1:
            win=True
        else:
            if com_hand == hand+1:
                win=True
    if win == True:
        print("あなたの勝ちです")
        g_human+=1
    else:
        print("あなたの負けです")
        g_com+=1
    #戻り値なし

print(" _____________")
print("/ ゲーム開始 /")
print("~~~~~~~~~~~~~")
for i in range(1,11):
    print(f"\n-----第{i}回-----")
    print("じゃんけんで何を出しますか？")
    te=int(input("グー:1 チョキ:2 パー:3 終了:0 >>"))
    if te==0:
        print("ゲームを途中終了します")
        break
    judge(te)

print("======最終結果======")
print(f"{g_human}勝{g_com}敗で",end="")
if g_human == g_com:
    print("引き分けでした")
else:
    if g_human > g_com:
        print("あなたの勝ちです！")
    else:
        print("あなたの負けです...")
print(" _____________")
print("/ ゲーム終了 /")
print("~~~~~~~~~~~~~")
