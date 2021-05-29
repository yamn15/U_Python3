def sing():
    return 'sing'

def cry():
    return 'cry'


## print('********************************************************************')
## print('(1)')
### ↑モジュール呼び出す際に、なぜか8,9行目も出力されてしまう。仕組みを要復習



## humanから、絶対パスを使用してutils2を使用する
# from lesson_package_6_68.tools_6_69 import utils2

## 相対パスを使用して、utils2を使用する
## '.'で、同一のディレクトリを示す。 '..'で一つ上のディレクトリを示す
### ただし、相対パスはあまりPythonでは使用されない。分かりにくいから。
### できる限りトップのディレクトリを指定して記述する
from ..tools_6_69 import utils2

def cry2():
    return utils2.say_twice('cry')