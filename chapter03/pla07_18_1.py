import random

janken=["","グー","チョキ","パー"]
human_score=0	
com_score=0
human_finger=18
com_finger=18
for i in range(1,11):
    if i==6 or i==10:
        print(f"\nChallenge:{i} **ポイント２倍**")
    else:
        print(f"\nChallenge:{i}")
    while True:
        com=random.randint(1,3)
        if com==1:
            break
        else:
            if com==2:
               if com<=com_finger:
                   break
               else:
                   print("(com)困ったな…")
            else:
               if com_finger>=com+2:
                   break
               else:
                   print("(com)まいったな…")
    while True:
        print("じゃんけんの手は何にしますか？")
        try:
            human=int(input("グー:1 チョキ:2 パー:3 終了:0 >>"))
        except (ValueError, TypeError):	#数字以外の文字や空のenter
            print("数字を入力してください")
            continue
        if human<0 or human>3:
            print("0-3の範囲で正しく入力してください")
            continue
        if human<2:
            break
        else:
            if human==2:
                if human<=human_finger:
                    break
                else:
                    print("指が足りません。入力し直してください")
            else:
                if human_finger>=human+2:
                    break
                else:
                    print("指が足りません。入力し直してください")
    if human==0:
        print("ゲームを途中終了します")
        break
    print(f"コンピュータは{janken[com]}を出しました")
    if human==2:
        human_finger-=2
    if human==3:
        human_finger-=5
    if com==2:
        com_finger-=2
    if com==3:
        com_finger-=5
    if human==com:
        print("惜しい！あいこです")
    else:
        if human==1:
            if com==2:
                print("勝ちました！")
                human_score+=1
                if i==6 or i==10:
                    human_score+=1
            else:
                print("負けました！")
                com_score+=1
                if i==6 or i==10:
                    com_score+=1
        elif human==2:
            if com==3:
                print("勝ちました！")
                human_score+=1
                if i==6 or i==10:
                    human_score+=1
            else:
                print("負けました！")
                com_score+=1
                if i==6 or i==10:
                    com_score+=1
        elif human==3:
            if com==1:
                print("勝ちました！")
                human_score+=1
                if i==6 or i==10:
                    human_score+=1
            else:
                print("負けました！")
                com_score+=1
                if i==6 or i==10:
                    com_score+=1
    print(f"人間:{human_finger}、コンピュータ:{com_finger}")	#デバッグ用

print("余った指の本数をポイントから差し引きます")
print(f"あなたのポイント={human_score}点")
print(f"コンピュータのポイント={com_score}点")
if human_score==com_score:
    print("引き分けでした")
else:
    if human_score>com_score:
        print("あなたの勝ちです！")
    else:
        print("あなたの負けです...") 
