print('**********************************************************************')

# 条件に合致する場合にリストの内の特定のインデックスを出力するwhileループ
some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

print('**********************************************************************')

# 条件に合致する場合にリストの内の特定のインデックスを出力するforループ
# somelist2の中身をiにいれて、終わりまで一つずつ出力する
## 反復処理をするものをイテレータと呼ぶ
### イテレータで、iにリストの中の値を反復処理で入れていく
some_list2 = [1, 2, 3, 4, 5]

for i in some_list2:
    print(i)

print('**********************************************************************')

# for ループは文字列にも使える

for s in 'abcdefg':
    print(s)

print('**********************************************************************')

# strが入っているリストにも使える

for word in ['My', 'name', 'is', 'Mike']:
    print(word)

print('**********************************************************************')

# forループでもbreakを使える
## if文に合致し、ブレイクに至ったらfor文全体の処理が終了する
## if文に合致し、コンティニューに至ったら、処理(print)をスキップし、forループを続行する
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
#        break
        continue
    print(word)

print('**********************************************************************')
