# 例外処理、エラーハンドリング
print('********************************************************************')
print('(1)')

l = [1, 2, 3]
i = 5
# 下記を実行するとindexエラーが発生する
# l[i]


print('********************************************************************')
print('(2)')

l2 = [1, 2, 3]
i2 = 5

# 実行すると、Don't worryが出力される
## tryとexceptの間の処理でエラーが起こった場合にexceptの処理を実行する
try:
    l2[i2]
except:
    print("Don't worry")

# エラーで処理が止まらず、lastのprintが実行される
## exceptがない場合は、エラーで処理が止まる
print("last")


print('********************************************************************')
print('(3)')

l3 = [1, 2, 3]
i3 = 5

try:
    l3[i3]
# IndexErrorが発生した場合のみexcept処理を実行する
## except の後ろに条件を指定できる
except IndexError:
    print("Don't worry")

print("last")


print('********************************************************************')
print('(4)')

l4 = [1, 2, 3]
i4 = 5

try:
    l4[i4]
# asを使用すると、出力結果にエラーを表示できる
except IndexError as ex:
    print("Don't worry: {}".format(ex))

print("last")


print('********************************************************************')
print('(5)')

l5 = [1, 2, 3]
i5 = 5
# del l5

try:
    l5[i5]
# asでIndexErrorを指定しているので、変数がないというエラーは例外処理をできない
except IndexError as ex:
    print("Don't worry: {}".format(ex))

print("last")


print('********************************************************************')
print('(6)')

l6 = [1, 2, 3]
i6 = 5
del l6

try:
    l6[i6]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
# 例外処理の条件を追加する
except NameError as ex:
    print(ex)

print("last")


print('********************************************************************')
print('(7)')

l7 = [1, 2, 3]
i7 = 5

try:
    () + l7
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
# 指定している例外処理の条件以外のエラーをキャッチして、実行結果に出力する
# pythonでは、不確定のエラーを例外処理を行い、プログラムを続けるのは推奨されていない
except Exception as ex:
    print('other:{}'.format(ex))
print("last")

# 参考
## https://docs.python.org/3/library/exceptions.html

print('********************************************************************')
print('(8)')

l8 = [1, 2, 3]
i8 = 5

try:
    () + l8
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
# 例外処理が実行されようが、処理が正常であっても、最後には必ずfinallyの処理を実行する
finally:
    print('clean up')

print('********************************************************************')
print('(9)')

l9 = [1, 2, 3]
i9 = 5

# 例外処理が書かれていないので、エラーで処理は止まる
## しかし、finallyの処理のみ実行されてからエラーが吐き出される
try:
    l9[i9]
# except IndexError as ex:
#     print("Don't worry: {}".format(ex))
# except NameError as ex:
#     print(ex)
# except Exception as ex:
#     print('other:{}'.format(ex))
finally:
    print('clean up')

print('********************************************************************')
print('(10)')

l10 = [1, 2, 3]
i10 = 5

try:
    l10[i10]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
# 例外処理を設定しているなかで、処理が正常に終了した際にelseの処理を実行する
## finallyの処理がある場合、プログラムが正常の場合の処理をelseで実行するのと、
## finallyの後ろで正常の場合の処理を実行するのでは意味合いが変わってくる。そのため、elseという構文がある
else:
    print('done')
finally:
    print('clean up')
