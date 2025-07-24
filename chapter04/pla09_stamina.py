import random

#グローバル変数
g_brd=[0]*30	#ゲームボード	#何の効果もないマス=ゼロで埋める
g_progress=[0,False,False] #進行管理：[ターン,追越フラグ,ゴールフラグ]
#各関数
def init():
    global g_brd
    dub=[False]*30	#効果マス設定の重複チェック用
    count=0
    while count<10:	#金貨増減/マス進む戻るの効果マス設定
        r=random.randint(1,28)
        effect=random.randint(1,4)
        if dub[r]==False:
            g_brd[r]=effect	#金貨増:1 金貨減:2 進む:3 戻る:4 とする
            dub[r]=True
            count+=1
    stay=0
    while stay<3:	#1回休みの効果マス設定
        r=random.randint(1,28)
        if dub[r]==False:
            g_brd[r]=5	#一回休みのマスは5とする
            dub[r]=True
            stay+=1
    while True:	#振り出しに戻る効果マスの設定
        r=random.randint(1,28)
        if dub[r]==False:
            g_brd[r]=6	#ふりだしに戻るマスは6とする
            break
    g_brd[0]=-1	#スタート
    g_brd[29]=7	#ゴール
    return

def disp(human, computer):
    pos=["　"]*30
    if human[0]==computer[0]:
        pos[human[0]]="＃"
    else:
        pos[human[0]]="＠"
        pos[computer[0]]="＊"
    for i in range(30):
        print(f"{pos[i]}",end="")    
    print("\n始", end="")	#スタート
    for j in range(1,29):
        if g_brd[j]==1:	#金貨プラス
            print("＋", end="")
        if g_brd[j]==2: #金貨マイナス
            print("ー", end="")
        if g_brd[j]==3: #Xマス進む
            print("＞", end="")
        if g_brd[j]==4: #Xマス戻る
            print("＜", end="")
        if g_brd[j]==5: #１回休み
            print("＆", end="")
        if g_brd[j]==6: #ふりだしに戻る
            print("！", end="")
        if g_brd[j]==0: #何もない
            print("＿",end="")
    print("終")	#ゴール
    return

def game(player):
    global g_progress
    key=""
    if player[2]==True:
        print(f"{member[g_progress[0]]}の番はお休みです")
        g_progress[0]=abs(g_progress[0]-1)	#ターン切り替え
        player[2]=False
        return player
    while True:
        #print(f"{player} {g_progress}")
        print(f"{member[g_progress[0]]}の番です")
        key=input("エンターキーを押してください(eで途中終了)")
        if key=="e":
            print("ゲームを途中終了します")
            g_progress[2]=True
            return player
        else:
            break
    if g_progress[0]==0 and key=="1":
        if player[1]>0:
            print(f"{member[g_progress[0]]}は食事をしました")
            player[3]=6	#スタミナ回復
            player[1]-=1
        else:
            print("金貨が足りません(><)")
    if g_progress[0]==1 and g_progress[1]==True:
        if player[1]>0:
            print("comは食事をしました")
            player[3]=6	#スタミナ回復
            player[1]-=1
        else:
            print("(com)ぐぬぬ…金貨が足りない(-_-ﾒ)")
    dice=random.randint(1,player[3])
    print(f"サイコロの目は{dice}です")
    player[0]+=dice
    if player[3]>1:	#スタミナ消費
        player[3]-=1
    #ゴールオーバーチェック
    if player[0]>29:
        print(f"余った分の{player[0]-29}マス戻ります")
        player[0]=29-(player[0]-29)
    #止まったマスの処理
    if g_brd[player[0]]==1 or g_brd[player[0]]==2:	#金貨増減
        player=gold(player, g_brd[player[0]])
    elif g_brd[player[0]]==3 or g_brd[player[0]]==4:	#追加移動
        player=moving(player, g_brd[player[0]])
    elif g_brd[player[0]]==5:	#1回休み
        player=rest(player)
    elif g_brd[player[0]]==6:	#振り出しに戻る
        player=restart(player)
    elif g_brd[player[0]]==7:	#ゴール
        goal()
    else:
        print("このマス目は何もありません")
    g_progress[0]=abs(g_progress[0]-1)	#ターン切り替え
    return player

def gold(player, getloss):	#金貨の増減
    r=random.randint(1,3)
    if getloss==1:
        print(f"{member[g_progress[0]]}は金貨を{r}枚ゲットしました。")
        player[1]+=r
    else:
        if player[1]>0:
            print(f"{member[g_progress[0]]}は金貨を{r}枚なくしました。")
            player[1]-=r
            if player[1]<0:
               player[1]=0
        else:
            print("なくす金貨もありません(ToT)")
    return player

def moving(player, steploss):	#追加移動
    r=random.randint(1,3)
    if player[3]>1:	#スタミナ消費
        player[3]-=1
    if steploss==3:
        print(f"{member[g_progress[0]]}はさらに{r}マス進みます！")
        player[0]+=r
        if g_brd[player[0]]==7:	#ちょうどぴったりならゴール
            goal()   
        #ゴールオーバーチェック
        if player[0]>29:
            print(f"{member[g_progress[0]]}は余った分の{player[0]-29}マス戻ります")
            player[0]=29-(player[0]-29)
    else:
        if player[3]>1:	#スタミナ消費
            player[3]-=1
        print(f"{member[g_progress[0]]}は{r}マス戻ります…")
        player[0]-=r
        #振り出しチェック
        if player[0]<0:
            print("振り出しに戻りました")
            player[0]=0
    return player

def rest(player):	#一回休み
    print(f"{member[g_progress[0]]}は1回休みです。")
    player[2]=True
    player[3]+=3	#スタミナ半分回復
    if player[3]>6:
        player[3]=6
    return player

def restart(player):	#ふりだしに戻る
    print(f"{member[g_progress[0]]}はふりだしに戻ります(><)ｼｸｼｸ…")
    player[0]=0
    return player

def goal():	#ゴール判定
    global g_progress
    print(f"{member[g_progress[0]]}がゴールしました！！")
    g_progress[2]=True
    return

#メインの部分
#初期化
member=["あなた","com"]
you=[0,10,False,6]	#人間側プレイヤー：[ボードの位置,所持してる金貨,一回休みフラグ,スタミナ]
com=[0,10,False,6]	#comプレイヤー   ：[ボードの位置,所持してる金貨,一回休みフラグ,スタミナ]
init()
print("\n=== すごろく ===")
g_progress[0]=random.randint(0,1)
print(f"{member[g_progress[0]]}が先攻です")
#メインループ
turn=1
while True:
    print(f"\n--- Turn:{turn} ---",end="")
    print(f"　金貨：あなた(＠)…{you[1]}、com(＊)…{com[1]}　スタミナ：あなた…{you[3]}、com…{com[3]}")
    disp(you,com)	#画面表示
    if g_progress[0]==0:
        you=game(you)
    else:
        com=game(com)
    if g_progress[2]==True:	#ゴールしたらループを抜ける
        break
    if you[0]>com[0]:	#追い越しフラグ判定
        g_progress[1]=True
    else:
        g_progress[1]=False
    turn+=1
        
#結果表示
print("*** 結果発表 ***")
print("スピード的勝利：",end="")
if you[0]<29 and com[0]<29:
    print("途中終了")
else:
    if you[0]==com[0]:
        print("ひきわけ")
    elif you[0]>com[0]:
        print(member[0])
    else:
        print(member[1])
print("金銭的勝利：",end="")
if you[1]==com[1]:
    print("ひきわけ")
else:
    if you[1]>com[1]:
        print(member[0])
    else:
        print(member[1])
print("スタミナ的勝利：",end="")
if you[3]==com[3]:
    print("ひきわけ")
else:
    if you[3]>com[3]:
        print(member[0])
    else:
        print(member[1])
print("お疲れ様でした。プログラムを終了します")
