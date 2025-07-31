#Dragon Care (class仕様版)
import random

class Dragon():
    name="ル'ケブレス"	#名前
    cloy=10	#満腹度
    mood=10	#機嫌度
    feed=0	#餌を与えた回数(一日ごとにリセット)
    pout=0	#寝床の汚れ具合(掃除しないと累積する)
    slept=False	#寝かしつけフラグ(寝ない日はペナルティあり)

    def __init__(self):
        option=["スマウグ","クオックス","ファフニル","レオリウス","ブルース","シェンロン"]
        naming=input("ドラゴンの名前は何にしますか？")
        if naming=="":
            self.name=random.choice(option)
        self.cloy=10
        self.mood=10
        self.feed=0
        self.pout=0
        self.slept=False

    def eat(self):
        print(f"{self.name}に餌をあげました")
        if self.feed<=3:
            self.cloy+=2
            if self.cloy > 10:
               self.cloy=10	#10を超えない
            self.feed+=1
        else:
            print(f"{self.name}はお腹いっぱいみたいです")

    def clean(self):
        print(f"{self.name}の寝床を掃除しました")
        self.cloy-=1 
        self.pout=0	#不機嫌のフラグだけオフ

    def walk(self):
        print(f"{self.name}を散歩に連れ出しました")
        self.cloy-=1
        self.mood+=1
        if self.mood>10:
            self.mood=10	#10を超えない

    def sleep(self):
        print(f"{self.name}を寝かしつけました")
        self.cloy-=2
        self.mood+=2
        if self.mood>10:
            self.mood=10	#10を超えない
        self.slept=True

    def info(self):
        print(f"満腹度：{self.cloy} 機嫌度：{self.mood}")
        #print(f"給餌：{self.feed} 清掃：{self.pout} 入眠:{self.slept}")	#デバッグ用表示
        print("餌：",end="")
        if self.feed>0:
            print("あげた　",end="")
        else:
            print("まだ　",end="")
        print("掃除：",end="")
        if self.pout==0:
            print("きれい　",end="")
        else:
            print("まだ　",end="")
        print("寝かしつけ：",end="")
        if self.slept:
            print("やった")
        else:
            print("まだ")

    def penalty(self):
        if self.feed==0 and self.cloy>0:
            print(f"{self.name}はひどくお腹を空かせています")
            self.cloy-=3
        if self.slept==False:
            print(f"{self.name}は寝てないので不機嫌です")
            self.mood-=3
        if self.pout==1 and self.mood>0:
            print(f"寝床が汚いので{self.name}は不機嫌です")
            self.mood-=1
        elif self.pout>1 and self.mood>0:
            print(f"寝床が汚なすぎて{self.name}は怒っています")
            self.mood=self.mood-3*self.pout
    #>>class Dragon end<<

def getcmd(turn,prev):
    care=0
    print(f"{turn}回目のコマンドです")
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
                    if care==prev:
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

def game(dragon):
    days=7
    action=4
    quit_game=False
    print(f"あなたはドラゴンの{dragon.name}を{days}日間お世話することになりました。")
    print(f"１日にお世話のコマンドを{action}回実行できます。")
    print(f"{dragon.name}の機嫌を損ねないように頑張ってください。")
    for day in range(1,days+1):
        print(f"\n{day}日めです")
        prev=0
        for turn in range(1,action+1):
            dragon.info()
            cmd = getcmd(turn,prev)
            if cmd == 1:
                dragon.eat()
            elif cmd == 2:
                dragon.clean()
            elif cmd == 3:
                dragon.walk()
            elif cmd == 4:
                dragon.sleep()
            else:   #GiveUpの場合
                quit_game=True
                break
            if dragon.cloy<1 or dragon.mood<1:	#どちらかがゼロ以下で即ゲームオーバー
                break
            prev=cmd
        
        if quit_game:
            print("\nあなたは逃げ出した。")
            print("「こんなのやってられるか！！」")
            print(f"懸命に走るあなたの背後に、{dragon.name}が近づいてきます。")
            print("あなたは、逃げられないことを悟りました。")
            print("(||ﾟДﾟ)ﾋｨｨｨ!")
            break
        #追加ステータス変化
        dragon.penalty()
        dragon.pout+=1	#ドラゴンの寝床汚れる
        #ここでゲームオーバーの判定
        if dragon.cloy<1:
            print(f"\nあなたはお腹を空かせた{dragon.name}に食べられてしまいました")
            quit_game=True
            break
        if dragon.mood<0:
            print(f"\n腹を立てた{dragon.name}の炎であなたは黒焦げにされました")
            quit_game=True
            break

        print(f"{day}日めが終わりました")
        dragon.feed=0
        dragon.slept=False
        prev=0
 
    #ゲームクリアの処理
    if not quit_game:
        print(f"\nあなたは７日間{dragon.name}を世話することができました。")
        print(f"{dragon.name}を送り出して「やれやれ」と息をつくあなた。")
        print("しかし、家に戻ると別のドラゴンが待っていました。")
        print("┐(´д｀)┌")
    #>>game() end<< 
     
#ここからmain        
print("ゲーム開始します")
dragon=Dragon()
game(dragon)
print("ゲーム終了です")
