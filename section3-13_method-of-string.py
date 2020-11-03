
print('******************************************************************')

s = 'My name is Mike. Hi Mike.'
print(s)

# 引数に「.」を付けることで、メソッドの選択肢が表示される
## メソッドを変数に入れて実行
### x.startwith変数が指定の文字列からから始まっているか否かを出力するメソッド
#### 今回の場合、変数sの先頭を見て判断する
##### 半角スペースが入っているだけでFalseが出力された。逆に半角スペースを潰したらTrueになった
##### もちろん指定の文字列以外でもFalse
is_start = s.startswith('My')
print(is_start)

is_start = s.startswith('X')
print(is_start)

print('**************************************************************')

# x.fiindは、xの中から指定の文字列を探すメソッド
# インデックスを返す。半角スペースもインデックスに数えられる
print(s.find('Mike'))

# x.rfiindは、xの中の後ろから指定の文字列を探すメソッド
print(s.rfind('Mike'))

# x.countは、xの中に指定の文字列が何個入っているかを数えるメソッド
print(s.count('Mike'))

print('**************************************************************')

# x.capitalizeは、xの中の先頭のみ大文字にして、ほか全てを小文字にするメソッド
print(s.capitalize())

# x.titleは、xの中の全ての単語の先頭を大文字にするメソッド
print(s.title())

# x.upperは、xの中の全ての単語を大文字にするメソッド
print(s.upper())

# x.lowerは、xの中の全ての単語を小文字にするメソッド
print(s.lower())

# x.replaceは、xの中の任意の単語を任意の文字にするメソッド
print(s.replace('Mike', 'Nancy'))








