#Dragon Care
import random

def getcmd(t,p):
    care=0
    print(f"{t}回目のコマンドです")
    print("　1: 給餌する")
    print("　2: 寝床を掃除")
    print("　3: 散歩する")
    print("　4: 寝かしつけ")
    print("　5: Give up")
    while True:
        try:
            care = int(input("どうお世話をしますか？"))
            if care > 0 and care <= 5:
                if care==2 or care==3:	#掃除と散歩は連続実行しない
                    if care==p:
                        print("そのコマンドは連続指定できません")
                        continue
                break
            else:
                print("1-5の数字を入力してください")
                continue
        except ValueError:
            print("文字は入力できません。1-5の数字を入力してください")
            continue
    return care

dragon=["スマウグ","クオックス","ファフニル","レオリウス","ブルース","シェンロン"]
print("*** Dragon Care ***")
name=input("ドラゴンの名前は何にしますか？")
if name=="":
    name=random.choice(dragon)
print(f"あなたはドラゴンの{name}を７日間預かることになりました。")

quit=False  #Give upのフラグ
hungry=10   #満腹度
mental=10   #機嫌度
feed=0
slept=False
pout=1
prev=0
for i in range(1,8):
    print(f"\n{i}日めです")
    for c in range(1,5):
        print(f"満腹度：{hungry} 機嫌度：{mental}")
        print(f"給餌：{feed} 清掃：{pout} 入眠:{slept} さっきのcmd:{prev}")
        cmd = getcmd(c,prev)
        if cmd == 1:
            if feed<=3:
                print(f"{name}に餌をあげました")
                hungry+=2
                if hungry>10:
                    hungry=10
                feed+=1
            else:
                print(f"{name}はお腹いっぱいみたいです")
        elif cmd == 2:
            print(f"{name}の寝床を掃除しました")
            hungry-=1
            pout=0
        elif cmd == 3:
            print(f"{name}を散歩に連れ出しました")
            hungry-=1
            mental+=1
            if mental>10:
                mental=10
        elif cmd == 4:
            print(f"{name}を寝かしつけました")
            hungry-=2
            mental+=2
            if mental>10:
                mental=10
            slept=True
        else:   #GiveUpの場合
            quit=True
            break
        if hungry<1 or mental<1:	#どちらかがゼロ以下で即ゲームオーバー
            break
        prev=cmd

    #各コマンドの処理を抜けたらここにくる
    if quit:
        print("あなたは逃げ出した。")
        print("「こんなのやってられるか！！」")
        print(f"歩を急ぐあなたの背後に、{name}の羽音が近づいてきます。")
        print("あなたは、逃げられないことを悟りました。")
        print("(||ﾟДﾟ)ﾋｨｨｨ!")
        break
    #追加ステータス減少
    if feed==0 and hungry>0:
        print(f"{name}はひどくお腹を空かせています")
        hungry-=3
    if slept==False:
        print(f"{name}は寝てないので不機嫌です")
        mental-=3
    if pout==1 and mental>0:
        print(f"寝床が汚いので{name}は不機嫌です")
        mental-=1
    elif pout>1 and mental>0:
        print(f"寝床が汚なすぎて{name}は怒っています")
        mental=mental-3*pout
    pout+=1	#ドラゴンのうんち増加
    #ここでゲームオーバーの判定
    if hungry<1:
        print(f"あなたはお腹を空かせた{name}に食べられてしまいました")
        quit=True
        break
    if mental<0:
        print(f"腹を立てた{name}の炎であなたは黒焦げにされました")
        quit=True
        break

    print(f"{i}日めが終わりました")
    feed=0
    slept=False
    prev=0

#７日が過ぎたかGiveUpしたらここへくる
if not quit:
    print(f"あなたは７日間{name}を世話することができました。")
    print("「やれやれ」と息をつくあなた。")
    print("しかし、家に戻ると別のドラゴンが待っていました。")
    print("┐(´д｀)┌")

print("ゲーム終了です")
