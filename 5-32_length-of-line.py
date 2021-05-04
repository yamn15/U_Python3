print('**********************************************************************')

# 長い１文を単純に改行するだけではエラーが返ってくる
# s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' + 
#       'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
# print(s)

print('**********************************************************************')

# 長い１文を改行したい場合は、バックスラッシュ\を打てばいい
s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' \
       'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
print(s)

x = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1+ 1 \
    + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
print(x)

print('**********************************************************************')

# パレンティスの丸かっこでも改行対応可能
s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
       'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

x = (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1+ 1 
    + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1)
print(x)



## pythonでは1行の長さが80文字以上であれば、次の行に改行するべきという考え方がある