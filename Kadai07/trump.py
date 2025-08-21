import random
def pick(c):    #引数c:トランプの通し番号(1〜52)
    mark = ["スペード", "ダイヤ", "ハート", "クラブ"]
    s=int(c//13)    #スート
    if s==4:    #52の場合だけ
        s=3
    n=(c%13)+1  #ナンバー
    return str(mark[s])+"の"+str(n)

trump=52    #トランプの枚数(ジョーカーは抜き)
cards=[t for t in range(1,trump+1)] #1〜52の値をセット
random.shuffle(cards)

print("あなたが引いたトランプは、")
for i in range(0,5):    #リスト先頭から5枚
    up=cards[i]
    print(f"{pick(up)}")
print("です。")

