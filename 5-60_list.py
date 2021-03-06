# リスト内包表記
print('*******************************************************************************')
print('(1)')

# タプルの中の数字をリストとして表示するプログラム
t = (1, 2, 3, 4, 5)

r = []
for i in t:
    r.append(i)
print(r)


print('*******************************************************************************')
print('(2)')

# リスト内包表記
t2 = (1, 2, 3, 4, 5)

#  [for i in t]のforループでtから取り出した値を、先頭のiに順繰りで入れるイメージ
r2 = [i for i in t2]
print(r2)

print('*******************************************************************************')
print('(3)')

# タプルの中の数字をリストとして表示するプログラム。
# 余りがない場合出力するという追加条件あり
t3 = (1, 2, 3, 4, 5)

r3 = []
for i in t3:
    if i % 2 == 0:
        r3.append(i)
print(r3)

print('*******************************************************************************')
print('(4)')

# リスト内包表記2
## リスト内包表記はメモリの消費が少ない、処理が速いなどのメリットあり。

t4 = (1, 2, 3, 4, 5)

r4 = [i for i in t4 if i % 2 == 0]
print(r4)


print('*******************************************************************************')
print('(5)')

# リストを２つ使用してかけ算している
t5_1 = (1, 2, 3, 4, 5)
t5_2 = (6, 7, 8, 9, 10)


r5 = []
for i in t5_1:
    for j in t5_2:
        r5.append(i * j)

print(r5)


print('*******************************************************************************')
print('(6)')

# (5)のリスト内包表記
t6_1 = (1, 2, 3, 4, 5)
t6_2 = (6, 7, 8, 9, 10)


r6 = [i * j for i in t6_1 for j in t6_2]

print(r6)

### 短い簡潔な処理にのみ、リスト内包表記を使ったほうがいい。
### コードが読みづらくなるので、乱用は要注意