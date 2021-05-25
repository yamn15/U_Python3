# コマンドライン引数
print('********************************************************************')
print('(1)')

# sysをインポートする
import sys

## Termonalで、ファイル名 + Option1 + Option2 と書いて実行してみる
print(sys.argv)

### Terminalで記載したOption1 Option2がListとして出力される


print('********************************************************************')
print('(2)')

import sys

## Terminal上で、実行ファイル名の後ろに、任意の文字列を書いて出力する
for i in sys.argv:
    print(i)

### 実行ファイル名、任意の文字列がprintされる
