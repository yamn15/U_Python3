print('**********************************************************************')

### edditor端っこに表示されている数字の左側をクリックすると「ブレークポイント」を設定できる
### クリックすると、赤丸が表示される
### ブレークポイントをつけてから、エディタ内の虫のアイコンをクリック
####### デバッグカラムの上部▶アイコンを押すと、デバッグの進め方を指定するミニメニューバーが出てくる
### 続行(F5)：プログラムをはじめから終わりまで一気に実行する
### ステップオーバー(F10)：
### ステップインする(F11)：
### ステップアウトする(shift + F11)：
###### https://www.atmarkit.co.jp/ait/articles/1707/21/news030_3.html


# xを定義
x = -10
# x = 10
# x = 0

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

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')


