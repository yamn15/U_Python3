
print('******************************************************************')

#ブレイシズのカギカッコ{}にstringを代入
print ('a is {} ' .format('a'))

print ('a is {} ' .format('test'))

print ('a is {} {} {} ' .format(1, 2, 3))

#インデックスの指定
print ('a is {0} {1} {2} ' .format(1, 2, 3))

print ('a is {2} {1} {0} ' .format(1, 2, 3))

print ('My name is {0} {1} ' .format('Yamato', 'Kawamura'))

print ('My name is {0} {1} . Watashiha {1} {0}' .format('Yamato', 'Kawamura'))

print('******************************************************************')

#変数を指定することもできる
print ('My name is {name} {family} . Watashiha {family} {name}' .format(name ='Yamato' , family = 'Kawamura'))

print('******************************************************************')

#型の変換
##通常単純に1を出力したらinteger
print(1)
print(1, type(1))


##''で囲んで1を出力したらstring
print('1')
print('1', type('1'))

##明示的にstrで囲めば、stringになる
print(str(1))
print(str(1), type(str(1)))

x = str(1)
type(x)
print(type(x))

print('******************************************************************')

print(3.14)
print(3.14, type(3.14))

print(str(3.14))
print(str(3.14), type(str(3.14)))

print('******************************************************************')

print(True)
print(True, type(True))

print(str(True))
print(str(True), type(str(True)))

print('******************************************************************')





