import random

#グローバル変数
g_brd=[0]*30	#ゲームボード	#何の効果もないマス=ゼロで埋める
g_you=[0,5]	#人間側プレイヤー：[ボードの位置,所持してる金貨]
g_com=[0,5]	#comプレイヤー   ：[ボードの位置,所持してる金貨]
g_progress[0,False,False] #進行管理：[ターン,一回休みフラグ,ゴールフラグ]
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
    return

def game(player,turn):
    dice=random.randint(1,6)
    player[0]+=dice
        
    return stay

def gold(player, getloss):	#金貨の増減
    r=random.randint(1,3)
    if getloss==1:
        print(f"金貨を{r}枚ゲットしました。やった！")
        player[1]+=r
    else:
        print(f"金貨を{r}枚なくしました。残念orz")
        player[1]+=r
    return player

def moving(player, steploss):	#追加移動
    r=random.randint(1,3)
    if steploss==3:
        print(f"{r}マス進みます！")
        player[0]+=r
    else:
        print(f"{r}マス戻ります…")
        player[0]+=r
    return player

def rest(turn):	#一回休み
    print(f"{player[turn]}は1回休みです。")
    stay=True
    return stay

def restart(player):	#ふりだしに戻る
    print(f"なんと！ふりだしに戻ります(><)ｼｸｼｸ…")
    player[0]=0
    return player

def goal(turn):	#ゴール判定
    print(f"{player[turn]}がゴールしました！！")
    return

#メインの部分
#初期化
player=["あなた","com"]
init()
print("\n=== すごろく ===")
turn=random.randint(0,1)
print(f"{player[turn]}が先攻です")
#メインループ
while True:
    stay=False
    if turn==0:
        stay=game(you,turn)
    else:
        stay=game(com,turn)
    if stay==False:	#一回休みでなければターン切り替え
        turn=abs(turn-1)
        
#結果表示
print("*** 結果発表 ***")
print("スピード的勝利：",end="")
if you[0]==com[0]:
    print("ひきわけ")
else:
    if you[0]>com[0]:
        print("あなた")
    else:
        print("com")
print("金銭的勝利：",end="")
if you[1]==com[1]:
    print("ひきわけ")
else:
    if you[1]>com[1]:
        print("あなた")
    else:
        print("com")
print("お疲れ様でした。プログラムを終了します")

