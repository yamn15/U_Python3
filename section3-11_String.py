s = 'test'
print(s)

print('**********************************************************************')

#シングルクォートでも、ダブルクォートでも結果は同じ
print('hello')
print("hello")

print('**********************************************************************')

#ダブルクォートの中でシングルクォートは使える。逆もまたしかり
##シングル(ダブル)クォートの中でシングル(ダブル)クォートは使えない
###シングル(ダブル)クォートを使う場合は、バックスラッシュ(\)を入れる

print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")

print('**********************************************************************')

#出力で改行したいときは、\nをいれる
print('hello. How are you?')
print('hello. \nHow are you?')

#Windowsのパスのような文字列を出力するときは、row data(r)として出力すればいい
print('C:\name\name')
print(r'C:\name\name')

print('**********************************************************************')

#改行出力のバリエーション（ダブルクォートを6つ）
print("""
line1
line2
line3
""")

print('**********************************************************************')

#上下の空白改行を出力させない場合1
print("""line1
line2
line3""")

print('**********************************************************************')

#上下の空白改行を出力させない場合2
## \ は次の行からと指示できるプログラム
print("""\
line1
line2
line3\
""")

print('**********************************************************************')

#演算子を用いたstring
print('Hi.' * 3)
print('Hi.' * 3 + 'Mike')

#シングルクォートで囲む＝リテラル。+があってもなくても表示はできる
print('py' + 'thon')
print('py''thon')

#変数に入れたリテラルは ＋でつながなければならない
##＋がないとエラーになる
prefix = 'Py'
print(prefix + 'thon')

print('**********************************************************************')

#長めのstringを出力する際は ＋なしのリテラルを使うといいかも(1行が長いとプログラムが見えなくなるから)
s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

#パレンティス(丸かっこ()のこと)がなくても、バックスラッシュを使えば改行をしつつもひとまとまりの変数として定義できる
s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'\
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
print(s)



print('**********************************************************************')


