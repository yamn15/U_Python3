#Pythonは変数に整数を入力すると、自動でinteger型と判断してくれる
num = 1
print(num)

print('**************************************************************')

#Pythonは変数に文字を入力すると、自動でstrings型と判断してくれる
##文字列は、シングル or ダブルクォーテーションで囲まなければならない
name = 'mike'
print(name)

print('**************************************************************')

#Boolen型
is_ok = True

#type関数でtypeを表示できる
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

print('**************************************************************')

#タイプを無理やり変更する(関数の代入)
num = name
print(num, type(num))

print('**************************************************************')

#型変換
##Pythonは型変換が容易。バグにもつながりやすいが、プログラミングの柔軟性もある
num = 1
name = '1'

new_num = int(name)

print(new_num, type(new_num))

print('**************************************************************')

#型の宣言
##Python3.6からできるようになった。が、あまり使われていない

num: int = 1
name: str = '1'

new_num = int(name)

print(new_num, type(new_num))

num = name

print(num, type(num))

print('**************************************************************')

#変数宣言
##はじめを数字から始めてしまうとSyntax errorになる

num = 1

print(num)

#↓↓↓上記変数を1numで宣言し、1numをprintした場合のエラー↓↓↓
#PS C:\Users\yamato-kawamura\Desktop\programing\U_Python3> python secssion3_8_変数宣言.py
#  File "secssion3_8_変数宣言.py", line 60
#    1num = 1

print('**************************************************************')

##ifのようなPythonであらかじめ予約されている変数(構文ともいえる？)を自分の任意の変数として扱おうとした場合はエラーになる

