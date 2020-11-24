print('**********************************************************************')

# 複数のリストをforループで出力する
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

print('**********************************************************************')

# 上記の構文はiが複数個所にあって分かりずらい
# zip関数を使用するとシンプルになる
# zip関数は、定義された変数を取り出し、for文の中の新たな変数に入れる。そしてこの処理をループさせる。
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

print('**********************************************************************')





