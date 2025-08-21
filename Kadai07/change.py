#金額入力：入力チェック付き
while True:
    try:
        coin=int(input("お釣りの金額は？>"))
        if coin < 1:
            print("1以上を入力してください")
            continue
        else:
            break
    except ValueError:
        print("数値を入力してください")
        continue
#枚数計算
coin100=coin//100
coin-=coin100*100
coin10=coin//10
coin-=coin10*10
#表示
print(f"100円玉{coin100}枚,10円玉{coin10}枚,1円玉{coin}枚")

