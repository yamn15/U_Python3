print('**********************************************************************')

### pythonでは改行後にスペースを4ついれる(インデント)のが習わし(暗黙の了解)
### インデントがずれると、エラーとなり処理を実行できない

# xを定義
x = -10
# x = 10
# x = 0


### xが0より小さいならnegativeと出力する
### if → 条件定義文の始まりの条件を定義
### else →条件定義文における最後の条件を定義
### elif →最後の条件の間に設定する中間の条件。何個も作成可能
### if文は上から条件文を実行していく。条件に合致するプログラムを見つけたら、処理が確定する

# xが上記の条件に合致しない場合はpositiveと出力する
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10000000')
elif x == 10:
    print('10')
else:
    print('positive')

print('**********************************************************************')

### if文の中にif文を組み込むこともできる

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')
