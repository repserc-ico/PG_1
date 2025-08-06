import random
#Vampire's castle

class Castle:
    above=[0]*6
    under=[0]*6
    search_abv=[False]*6
    search_blw=[False]*6
    is_under=False

    def __init__(self):
        on_G=1
        while on_G<=3:
           r=random.randint(0,5)
           if self.above[r]==0:
              self.above[r]=on_G	#1...地図, 2...鍵, 3...ドアとする
              on_G+=1
        un_G=4
        while un_G<=5:
           r=random.randint(0,5)
           if self.under[r]==0:
              self.under[r]=un_G	#4...十字架, 5...吸血鬼の玄室とする
              un_G+=1
        self.is_under=False	#地下にいるかどうか(Trueなら地下)

    def info(self,player):
        print("+-+-+-+-+-+-+　　現在地: ",end="")
        if self.is_under==False:
            print("地上",end="")
        else:
            print("地下",end="")
        print("\n|",end="")
        for i in range(0,6):
            if self.search_abv[i]==True or player.scroll==True:
                if self.above[i]==1:
                    print("m|",end="")
                elif self.above[i]==2:
                    print("k|",end="")
                elif self.above[i]==3:
                    print("d|",end="")
                else:
                    if self.search_abv[i]==True:
                        print("0|",end="")
                    else:
                        print(" |",end="")
            else:
                if self.search_abv[i]==True:
                    print("0|",end="")
                else:
                    print(" |",end="")
        print("　　カギ=",end="")
        if player.key==True:
            print("k,",end="")
        print(" 地図=",end="")
        if player.scroll==True:
            print("m,",end="")
        print(" 地下入口=",end="")
        if player.door==True:
            print("d",end="")
        print("\n+-+-+-+-+-+-+")
        if self.is_under==True or player.scroll==True:
            print("|",end="")
            for i in range(0,6):
                if self.search_blw[i]==True or player.scroll==True:
                    if self.under[i]==4:
                        print("x|",end="")
                    elif self.under[i]==5:
                        print("V|",end="")
                    else:
                        if self.search_blw[i]==True:
                            print("0|",end="")
                        else:
                            print(" |",end="")
                else:
                    if self.search_blw[i]==True:
                        print("0|",end="")
                    else:
                        print(" |",end="")
            print("　　十字架=",end="")
            if player.cross==True:
                print("x,",end="")
            print(" 吸血鬼=",end="")
            if player.scroll==True:
                print("V,",end="")
            print("\n+-+-+-+-+-+-+")

    def fight(self,player):
        print("吸血鬼との戦いが始まりました！")
        you=random.randint(1,6)
        vamp=random.randint(1,6)
        if player.cross==True:
            print("吸血鬼は十字架を見てたじろいでいます。チャンス！")
            you+=3
        if you > vamp:
            print("おめでとう！　吸血鬼を倒すことができた！")
            print("*** HAPPY END ***")
        elif you < vamp:
            print("残念！　吸血鬼にやられてしまった…")
            print("*** WORST END ***")
        else:
            print(":\n:\nそこには静粛があった。")
            print("立ち上がる者はなく、")
            print("ただひんやりとした空気だけがただよっていた。")
            print("あなたが吸血鬼を倒したのは事実だ。")
            print("だが、それを誰にも報告することはできなかった。")
            print("しばしの時を経て、誰かがあなたの偉業に気付く。")
            print("その時には、すでに吸血鬼の館はなく、")
            print("白い花が一輪咲いていた…")
            print("*** BITTER END ***")
#クラスCastleここまで

class Player:
    scroll=False
    key=False
    door=False
    cross=False
    time=14

    def __init__(self):
        scroll=False	#地図(の巻物)
        key=False	#鍵
        door=False	#地下への入口
        cross=False	#十字架
        time=14	#ゲーム開始時刻

    def search(self,area,castle):
        self.time+=1
        if self.time>23:	#24時になったら吸血鬼と自動戦闘
            print("真夜中になり、目覚めた吸血鬼が襲ってきました！")
            castle.fight(player)
            return True
        if castle.is_under==False:
            if castle.above[area]==1:
                if castle.search_abv[area]==False:
                    print("地図を見つけました")
                    self.scroll=True
                else:
                    print("他には何もありません")
            elif castle.above[area]==2:
                if castle.search_abv[area]==False:
                    print("鍵を見つけました")
                    self.key=True
                else:
                    print("他には何もありません。地下に向かいましょう")
            elif castle.above[area]==3:
                if castle.search_abv[area]==False:
                    print("地下の入口を見つけました")
                    self.door=True
                    if self.key==True:
                        print("地下に移動します")
                        castle.is_under=True
                else:
                    if self.key==True:
                        print("地下に移動します")
                        castle.is_under=True
                    else:
                        print("鍵がかかっていて、地下に移動できません")
            else:
                print("何も見つかりませんでした")
            castle.search_abv[area]=True
            #print(f"area{area}={castle.search_abv[area]}")	#DBG
        else:
            if castle.under[area]==4:
                if castle.search_blw[area]==False:
                    print("十字架を見つけました！")
                    self.cross=True
                else:
                    print("他には何もありません")
                pass
            elif castle.under[area]==5:
                print("吸血鬼がいました！！")
                castle.fight(player)
                return True
            else:
                print("何も見つかりませんでした")
            castle.search_blw[area]=True
        return False
#クラスPlayerここまで

def select():
    while True:
        try:
            area=int(input("どのエリアを探索しますか？(1-6、0で終了)"))
            if area>=0 or area<=6:
                break
            else:
                print("数値は0-6の範囲で入力してください")
                continue
        except ValueError:
            print("数値を入力してください。")
            continue
    return area
#select関数ここまで

def game(castle, player):
    result=False
    print("あなたはようやく吸血鬼が棲むという館についた。")
    print("館は６つの広いエリアに分かれており、探索に時間がかかりそうだ。")
    print("地下の入口への鍵を見つけないと、吸血鬼の玄室のある地下には行けない。")
    print("ぐずぐずしていると、吸血鬼が目覚めてしまうから気をつけないと。")
    print("あなたは覚悟を決めて、館へと入っていった…")
    while True:
        print("\n††† 吸血鬼の館 †††")
        print(f" 1 2 3 4 5 6     時刻:{player.time}時")
        castle.info(player)
        area=select()
        #途中終了
        if area==0:
            print("あなたは怖くなって館を逃げ出した。")
            print("吸血鬼が相手なのだから、当然かもしれない。")
            print("だが、逃げ出したあなたには懸賞金がかけられた。")
            print("あなたは吸血鬼と同じく追われる身となった…")
            print("*** BAD END ***")
            break
        #探索結果
        result=player.search(area-1,castle)
        if result==True:
            break
#game関数ここまで

#ここからmain
print("ゲーム開始します")
castle=Castle()
player=Player()
game(castle, player)
print("ゲームを終了します")
#mainの終わり
