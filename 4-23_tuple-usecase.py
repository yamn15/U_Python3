print('******************************************************************')
# 3つの選択肢から2つ回答を選んでもらうアプリケーションの場合
chose_from_two = ('A', 'B', 'C')
answer = [ ]
answer.append('A')
answer.append('C')

## chose_from_two.append('A')
## chose_from_two.append('C')
### tupleにappendはできないのでエラーになる

print(chose_from_two)
print(answer)

print('******************************************************************')
# 3つの選択肢から2つ回答を選んでもらうアプリケーション
## 間違えて、リストを定義し、そのリストに回答をappendしてしまった場合。

chose_from_two = ['A', 'B', 'C']
answer = [ ]

chose_from_two.append('A')
chose_from_two.append('C')

print(chose_from_two)
print(answer)

print('******************************************************************')
