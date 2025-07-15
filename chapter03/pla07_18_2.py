import random

def judge(game):
    casewin=["ぐぬぬ…","まだまだ…","次こそは…","なかなかやるな…","負けないぞ！"]
    caselose=["ふふふふ…","やったね！","調子いいな","いけるいける！","次も勝つぞ！"]
    print(f"あなたは{janken[game[0]]}、コンピュータは{janken[game[1]]}を出しました")
    result=(game[0]-game[1]+3)%3
    if result==0:
        print("惜しい！あいこでした")
        print(f"(com){random.choice(caselose+casewin)}")
    else:
        if result==1:
            print("残念！あなたの負けです")
            print(f"(com){random.choice(caselose)}")
            game[3]+=game[6]
        else:
            print("やった！あなたの勝ちです")
            print(f"(com){random.choice(casewin)}")
            game[2]+=game[6]
    return game

def comhand(game):
    print("(com)よーし",end="")
    while True:
        hand=random.randint(0,2)
        if hand==0:
           break
        else:
            if hand==1:
                if game[5]>=2:
                    game[5]-=2
                    break
                else:
                    print("…",end="")
            else:
                if game[5]>=5:
                    game[5]-=5
                    break
                else:
                    print("…",end="")
    print("決めた！")
    game[1]=hand
    return game

def youhand(game):
    while True:
        print("じゃんけんの手は何にしますか？")
        try:
            hand=int(input("グー:0 チョキ:1 パー:2 終了:3 >>"))
        except (ValueError, TypeError):	#数字以外の文字や空のenter
            print("数字を入力してください")
            continue
        if hand<0 or hand>3:
            print("0-3の範囲で正しく入力してください")
            continue
        if hand<1 or hand>2:
            break
        else:
            if hand==1:
                if game[4]>=2:
                    game[4]-=2
                    break
                else:
                    print("指が足りません。入力し直してください")
            else:
                if game[4]>=5:
                    game[4]-=5
                    break
                else:
                    print("指が足りません。入力し直してください")
    game[0]=hand
    return game

#メインプログラム始まり
janken=["グー","チョキ","パー"]	#グー:0、チョキ:1、パー:2 とする
bout=[0, #人間の手
      0, #comの手
      0, #人間のポイント
      0, #comのポイント
      18, #人間の指の本数 
      18, #comの指の本数
      1 #獲得ポイント数
]
#人間の手,comの手,人間のポイント,comのポイント,人間の指の本数,comの指の本数,獲得ポイント数
print("\n=== 18(ｲﾁﾊﾁ) ===")

for i in range(1,11):	#10回勝負
    print(f"\n--- 第{i}回 ---", end="")
    if i==6 or i==10:
        print("  **ポイント２倍**")
        bout[6]=2
    else:
        print("")
        bout[6]=1

    bout=comhand(bout)
    bout=youhand(bout)
    
    if bout[0]==3:
        print("ゲームを途中終了します")
        #さっきcomが出した手を戻す
        if bout[1]==1:
            bout[5]+=2
        elif bout[1]==2:
            bout[5]+=5
        break

    bout=judge(bout)
    print(f"残りの指…あなた:{bout[4]}本　com:{bout[5]}本")
    #ここでforループ折返し

#ゲーム結果
print("余った指の本数をポイントから差し引きます")
bout[2]-=bout[4]
bout[3]-=bout[5]
print("\n*** 最終結果 ***")
print(f"あなたのポイント={bout[2]}点")
print(f"コンピュータのポイント={bout[3]}点")
if bout[2]==bout[3]:
    print("引き分けでした")
else:
    if bout[2]>bout[3]:
        print("あなたの勝ちです！")
        print("(com)悔しい…")
    else:
        print("あなたの負けです…")
        print("(com)わっはっはっはっ！") 
#メインプログラムの終わり
