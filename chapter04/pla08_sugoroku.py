import random

#グローバル変数
g_brd=[0]*30	#ゲームボード	#何の効果もないマス=ゼロで埋める
g_progress=[0,None,False] #進行管理：[ターン,(未使用),ゴールフラグ]
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
    #print(f"{g_brd}")
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
    if player[2]==True:
        print(f"{member[g_progress[0]]}の番はお休みです")
        g_progress[0]=abs(g_progress[0]-1)	#ターン切り替え
        player[2]=False
        return player
    while True:
        print(f"{member[g_progress[0]]}の番です")
        key=input("エンターキーを押してください(eでギブアップ)")
        if key=="e":
            print("ゲームを途中終了します")
            g_progress[2]=True
            return player
        else:
            break
    dice=random.randint(1,6)
    print(f"サイコロの目は{dice}です")
    player[0]+=dice
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
        g_progress=goal(g_progress)
    else:
        print("このマス目は何もありません")
    g_progress[0]=abs(g_progress[0]-1)	#ターン切り替え
    #print(f"you{you}、com{com}、g_progeress{g_progress}")
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
        else:
            print("なくす金貨もありません(ToT)")
    return player

def moving(player, steploss):	#追加移動
    r=random.randint(1,3)
    if steploss==3:
        print(f"{member[g_progress[0]]}はさらに{r}マス進みます！")
        player[0]+=r
        #ゴールオーバーチェック
        if player[0]>29:
            print(f"{member[g_progress[0]]}は余った分の{player[0]-29}マス戻ります")
            player[0]=29-(player[0]-29)
    else:
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
    return player

def restart(player):	#ふりだしに戻る
    print(f"{member[g_progress[0]]}はふりだしに戻ります(><)ｼｸｼｸ…")
    player[0]=0
    return player

def goal(proceed):	#ゴール判定
    print(f"{member[proceed[0]]}がゴールしました！！")
    proceed[2]=True
    return proceed

#メインの部分
#初期化
member=["あなた","com"]
you=[0,5,False]	#人間側プレイヤー：[ボードの位置,所持してる金貨,一回休みフラグ]
com=[0,5,False]	#comプレイヤー   ：[ボードの位置,所持してる金貨,一回休みフラグ]
init()
print("\n=== すごろく ===")
g_progress[0]=random.randint(0,1)
print(f"{member[g_progress[0]]}が先攻です")
#メインループ
turn=1
while True:
    print(f"\n--- Turn:{turn} ---",end="")
    print(f"　金貨：あなた(＠)…{you[1]}、com(＊)…{com[1]}")
    disp(you,com)	#画面表示
    if g_progress[0]==0:
        you=game(you)
    else:
        com=game(com)
    if g_progress[2]==True:	#ゴールしたらループを抜ける
        break
    turn+=1
        
#結果表示
print("*** 結果発表 ***")
print("スピード的勝利：",end="")
if you[0]==com[0]:
    print("ひきわけ")
else:
    if you[0]>com[0]:
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
print("お疲れ様でした。プログラムを終了します")
