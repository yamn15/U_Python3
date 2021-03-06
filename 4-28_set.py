# 数学でいう集合
print('**********************************************************************')

# 重複された数字は省略されて出力される
a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)

# ブレイシズのカギカッコ{}で、キーバリューを指定せずに定義すると、set(集合型)になる
print(a, type(a))

print('**********************************************************************')

b = {2, 3, 3, 6, 7}
print(a)
print(b)

z = a - b
print(z)

y = b - a
print(y)

print('**********************************************************************')

# a にもb にもある値を出力す場合アンパサンド＆ を使用する
## a + bはエラーが返ってくるので注意
## x = a + b
x = a & b
print(x)

# a または b はパイプ ｜ を使用する

w = a | b
print(w)

print('**********************************************************************')

# 排他的集合（a,bどちらかには歩けどもｍ重複はしていないもの）を出力する場合は ＾ を使用する
v = a ^ b
print(v)