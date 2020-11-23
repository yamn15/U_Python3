print('**********************************************************************')

# input('xxx')で指定した値が出力結果に表示され、そこに何らかの値を打ち込む。
# ユーザに値を都度入力させる際に使用する
## while文とよく一緒に使われる
while True:
    word = input('Enter1:')
    # 入力された値がif文に合致する場合は、breakする
    # 値はstrings型で入ってくる
    if word == 'ok':
        break
    # 入力された値がif文と合致しなかった場合は、printが出力されwhileループが続く
    print('next')

print('**********************************************************************')

# inputをint型に変えたい場合

while True:
    word = input('Enter2:')
    # intで入力したければ、型変換を行う。ただし、inputがintしか受け付けなくなるので要注意。
    num = int(word)
    if num == 100:
        break
    print('next')
