# 集合内包表記
print('*******************************************************************************')
print('(1)')

# iにrange関数を使用して数字を入れ、集合を作成するプログラム

s = set()
for i in range(10):
    s.add(i)

print(s)


print('*******************************************************************************')
print('(2)')

# (1)を集合内包表記を使用して記述

s2 = {i for i in range(10)}
print(s2)


print('*******************************************************************************')
print('(3)')

# iにrange関数を使用して数字を入れ、集合を作成するプログラム
## if文を追加した場合

s3 = set()
for i in range(10):
    if i % 2 == 0:
        s3.add(i)

print(s3)


print('*******************************************************************************')
print('(4)')

# (4)を集合内包表記を使用して記述

s4 = {i for i in range(10) if i % 2 == 0}
print(s4)