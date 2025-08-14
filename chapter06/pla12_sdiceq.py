#Super Dice Q
import random

class Board:
    panel=[""]*9	#パネル表示用
    flip=[0]*9	#開いたパネル(True=Open, False=not Open)
    
    def __init__(self):
        self.reset()

    def reset(self):	#パネルを戻す
        self.panel=["１","２","３","４","５","６","７","８","９"]
        self.flip=[False]*9

    def is_all_open(self):	#ラウンドクリア判定
        if sum(self.flip)==9:
           return True
        else:
           return False

    def show(self):	#パネル表示
        print("+ー+ー+ー+")
        print("|",end="")	#１行目
        for i in range(0,3):
            print(f"{self.panel[i]}|",end="")
        print("\n+ー+ー+ー+")
        print("|",end="")	#２行目
        for i in range(3,6):
            print(f"{self.panel[i]}|",end="")
        print("\n+ー+ー+ー+")
        print("|",end="")	#３行目
        for i in range(6,9):
            print(f"{self.panel[i]}|",end="")
        print("\n+ー+ー+ー+")

    def turn(self, select):	#パネル選択
        point=select-1	#リストなので-1してる
        if self.flip[point]==True:
            print(f"パネル{select}はすでに開いています")
            return False
        else:
            print(f"パネル{select}を開きました")
            self.panel[point]="Ｘ"
            self.flip[point]=True
            return True
#Boardクラスここまで

class Game:
    game_round=1	#ゲームラウンド
    score=0	#得点
    is_turned=False	#ダイスを振ってからパネルを１枚でも開いたか(True=開いた, False=まだ)
    reserve=0	#ダイスの残り目
    out=False	#ゲーム終了
    dice=[0]*2	#各ダイスの目
    is_double=False	#ゾロ目の場合(True=ゾロ目, False=ゾロ目ではない)

    def __init__(self):
        self.game_round=1
        self.score=0
        self.is_turned=False
        self.reserve=0
        out=False
        dice=[0]*2
        is_double=False
        
    def play(self,board):	#ゲームの手順繰り返し
        while True:
            print("\n*** Super Dice Q ***")
            print(f"Round: {self.game_round}, Score={self.score}")
            self.dice[0]=random.randint(1,6)
            self.dice[1]=random.randint(1,6)
            print(f"{self.dice[0]}と{self.dice[1]}の目が出ました。")
            self.is_turned=False
            self.reserve=sum(self.dice)
            check=0
            chk_max=self.reserve
            if chk_max>9:
                chk_max=9
            for i in range(0,chk_max):
                check+=board.flip[i]
            if check==chk_max:
                board.show()
                print("開けるパネルがありません！")
                print("残念ですが、ここでゲームオーバーです！")
                self.out=True
                break
            if self.dice[0]==self.dice[1]:
                print("ゾロ目が出ました。ポイント２倍！")
                self.is_double=True
            while True:
                board.show()
                print(f"残りのサイコロの目: {self.reserve}")
                select=self.assign()
                if select==-1:
                    self.out=True
                    break
                if select==0:
                    if self.is_turned==True:
                        print("サイコロを振り直します")
                        break
                    else:
                        print("１つでもパネルを開かないと振り直しはできません。")
                        print("１つも開くことができない場合はゲーム終了です")
                    continue
                if board.turn(select)==True:
                    self.is_turned=True
                    self.score=self.score+select+(select*self.is_double)
                    self.reserve-=select
                    if board.is_all_open():
                        print("パネルを全て開きました！")
                        board.reset()
                        self.game_round+=1
                        if self.reserve>0:
                            print(f"余った目{self.reserve}はスコアから差し引きます")
                            self.score-=self.reserve
                        break
                    if self.reserve==0:
                        print("残りサイコロの目がありません。振り直します")
                        break
                else:
                    self.is_turned=False
            if self.out==True:
                break

    def assign(self):	#消すパネルの指定とサイコロの目の残りのチェック
        while True:
            try:
                print("どのパネルを開きますか？")
                select=int(input("(1-9で指定します。0: 振り直し -1:終了 >>)"))
                if select<-1 or select>9:
                    print("-1から9までの数を入力してください。")
                    continue
            except ValueError:
                print("数値を入力してください。")
                continue
            if select<=self.reserve:
                break
            else:
                print("残りのサイコロの目が足りません。")
        return select
#Gameクラスここまで

#ここからmain
print("プログラム開始します")
board=Board()
game=Game()
while True:
    game.play(board)
    if game.out==True:
        break
print(f"今回の成績：Round:{game.game_round} Score={game.score}")
print("プログラム終了します")

