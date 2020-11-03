print('******************************************************************')

# リストの定義
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)

print('******************************************************************')

# リストのインデックス指定
print(s[0])

print('******************************************************************')

# リスト内の値の変更
s[0] = 'x'
print(s)

print('******************************************************************')

# リストのスライス指定
print(s[2:5])

print('******************************************************************')

# リスト内の値をスライスで変更
s[2:5] = ['C', 'D', 'E']
print(s)

print('******************************************************************')

# リスト内の値を削除する
s[2:5] = []
print(s)

print('******************************************************************')

#リスト内の値全削除する
s[:] = []
print(s)

print('******************************************************************')

# 値を定義する
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)

## x.append() メソッドでリストに値を追加する
n.append(100)
print(n)

## なんで↓の書き方はNoneが出力される？
print(n, n.append(100))

print('******************************************************************')

## x.insert() メソッドでリストの先頭に値を追加する
n.insert(0, 200)
print(n)
## なんで↓の書き方はNoneが出力される？
print(n, n.insert(0, 200))

print('******************************************************************')

# x.pop()リストから値を取り出す
## インデックス指定なしは、末尾が取り出される?
n.pop()
print(n)
## 末尾をリストから取り出したうえで、リストを返している。取り出した値も出力される
print(n, n.pop())

## インデックス指定してリストから値を取り出し
n.pop(0)
###その結果のリストを出力
print(n)

## インデックス指定してリストから取り出したうえで、リストを返している。取り出した値も出力される
print(n, n.pop(0))

print('******************************************************************')

# 削除したい場合はdelを使用する
del n[0]
print(n)

# delは変数自体も消すことができるので要注意
## 出力でnがないというエラーが返ってくるので要注意

### del n
### print(n)

print('******************************************************************')

n = [1, 2, 2, 2, 3]
print(n)

# x.removeでリストの中身を部分削除できる
n.remove(2)
print(n)

print('******************************************************************')

n.remove(2)
print(n)

print('******************************************************************')

n.remove(2)
print(n)

# x.removeで、すでにない値を指定するとエラーが返ってくる
## n.remove(2)
## print(n)

print('******************************************************************')

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(a)
print(b)

print('******************************************************************')

# リストの結合
print(a + b)

# 結合した後も、結合前のリストを個別で出力できる
print(a)
print(b)

print('******************************************************************')

# リストに、別のリストを付け足す
a += b
print(a)

print('******************************************************************')

# メソッドでリストにほかのリストの中身を追加する
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)





