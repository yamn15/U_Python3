# オンラインショップで果物を売るような場合
print('**********************************************************************')

fruits =  {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

# 商品の値段を調べたい場合に、keyを指定する
print(fruits['apple'])

print('**********************************************************************')

# リストで同じこともできるが、結果の出力まで少々手間がかかる
## リストから任意の値を出力すrためには、目的の値のインデックスを見つけるプログラムを書く必要がある
# l = [
#     ['aaple', 100],
#     ['banana', 200],
#     ['orange', 300],
# ]

### Keyで何かを検索して値を取ってきたい場合は、dictionaryが適している
### listは上から検索していくのでプログラムに時間がかかる
### dictionaryはハッシュテーブルを用いているので処理が早い

print('**********************************************************************')













