#Super Dice Q
import random

Class Board:
    panel=[""]*9	#パネル表示用
    table[0]*9	#パネル判定用
    flip=[0]*9	#開いたパネル(True=Open, False=not Open)
    
    def __init__(self):
        self.reset()

    def reset(self):	#パネルを戻す
        panel=["１","２","３","４","５","６","７","８","９"]
        table[1,2,3,4,5,6,7,8,9]
        flip=[False]*9

    def is_all_open(self):	#ラウンドクリア判定
        if sum(self.panel)==9:
           return True
        else:
           return False

    def show(self):	#パネル表示
        print("* Super Dice Q *")
        print("+ー+ー+ー+")
        print("|",end="")	#１行目
        for i in range(0,3):
            print(f"{panel[i]}|",end="")
        print("\n+ー+ー+ー+")
        print("|",end="")	#２行目
        for i in range(3,6):
            print(f"{panel[i]}|",end="")
        print("\n+ー+ー+ー+")
        print("|",end="")	#３行目
        for i in range(6,9):
            print(f"{panel[i]}|",end="")
        print("+ー+ー+ー+")

    def turn(self, select):	#パネル選択
        point=select-1
        if self.flip[point]==True:
            print(f"パネル{select}はすでに開いています")
            return False
        else:
            print(f"パネル{select}を開きました")
            panel[point]="Ｘ"
            self.flip[point]=True
            return True
#Boardクラスここまで

Class Game:
    game_round=1	#ゲームラウンド
    score=0	#得点
    is_rolled=False	#このターンにダイスを振ったか(True=振った, False=まだ)
    reserve=0	#ダイスの残り目
    out=False	#ゲーム終了
    def __init__(self):
        game_round=1
        board=Board()
        score=0
        is_rolled=False
        reserve=0
        
    def play(self):	#ゲームの手順繰り返し
        pass
    
    def assign(self):	#消すパネルの入力
        pass
#Gameクラスここまで

#ここからmain
print("プログラム開始します")
game=Game()
while True:
    game.play()
    if game.out=True:
        break
print("プログラム終了します")

