print('**********************************************************************')

# リストの中のfruitをひとつずつ出力するループ
for fruit in ['apple', 'banana', 'orange']:
    print(fruit)

print('**********************************************************************')

# インデックスを表示したい場合
i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1

print('**********************************************************************')

# 変数を定義せずにループ結果にインデックスを表示したい場合
## emumirate関数を使用する
### enumirate関数が、ループのたびにiにインデックスを入れてくれる。またfruitに値を入れてくれる
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

# enumerate関数参考
# https://techacademy.jp/magazine/15640




