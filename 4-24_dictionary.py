print('**********************************************************************')
# ディクショナリー(dict)にはブレイシズの波括弧(カーリーブラケット)を使用する
## key : valueで構成される
d = {'x' : 10, 'y': 20  }
print(d)
print(d, type(d))

## x（ｙ）の値のみ確認したいときは以下の構文を使用する
print(d['x'])
print(d['y'])

print('**********************************************************************')

# dictには値(int)を代入できる
d['x'] = 100
print(d)

# dictには値(str)を代入できる
d['x'] = 'test'
print(d)

# dictにはあとからkey,valueを追加できる
d['z'] = 200
print(d)

## keyはstrでもintでも機能する
d[1] = 10000
print(d)

print('**********************************************************************')

## key,valueは以下の形式でも定義できる1
dict (a=10, b=20)
print(dict)

## key,valueは以下の形式でも定義できる(使用頻度低いかも)
dict([('a', 10), ('b', 20)])
print(dict)

print('**********************************************************************')



