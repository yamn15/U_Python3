# デバッガで処理をひとつづつ確認するとプログラムの動きがわかりやすい
print('**********************************************************************')

#一定の条件を指定し、条件に合致している間のみcountを出力し続ける
count = 0
while count < 5:
    print(count)
    count += 1
    #count = count + 1 ←という書き方もあるがあまり使われない
    ## count +=の条件式を忘れると無限ループになるので要注意

print('**********************************************************************')

## 以下のプログラムは無限ループ要注意
# while True:
#     print('XXX')

# break文を使用する方法
## countの値が5になると、if判定の中にbreakが適用される
count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1

print('**********************************************************************')

# continueを使用したループ処理
## continueの条件に合致すると、その下の処理(今回はprint)を行わず、ループ処理のはじめに戻る
count = 0
while True:
    if count >= 5:
        break
    
    if count == 2:
        count+= 1
        continue

    print(count)
    count += 1
