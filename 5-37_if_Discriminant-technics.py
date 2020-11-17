print('**********************************************************************')

is_ok = True

# 変数がboolen型でTrueが入っているので、if文でis_okがTrueかFalseか判断する指揮を入れずとも問題ない
## 復習
if is_ok:
    print('OK!')

print('**********************************************************************')

# 変数がTrueになる構造のバリュエーション1
## intの 1 はTrueと判定される
is_ok = 1
print(type(is_ok))
if is_ok:
    print('OK!')
else:
    print('NO!')

# 変数がTrueになる構造のバリュエーション2
## intの 0 はFalseと判定される
is_ok = 0
print(type(is_ok))
if is_ok:
    print('OK!')
else:
    print('NO!')

print('**********************************************************************')

# 変数がTrueになる構造のバリュエーション3
## intの 256 はTrueと判定される
### pythonでは、if文に指定した変数に値が入っていれば、条件式を書かずにTrueと判定される
is_ok = 256
print(type(is_ok))
if is_ok:
    print('OK!')
else:
    print('NO!')

print('**********************************************************************')

### pythonでは、if文に指定した変数に値が入っていれば、条件式を書かずにTrueと判定される
#### 値が入っているか入っていないかを確認するために、よく使われる。strやlistと相性がいい

# is_okに値が入っていないのでfalse
is_ok = ''
print(type(is_ok))
if is_ok:
    print('OK!')
else:
    print('NO!')

# is_okに値が入っているのでTrue
is_ok = 'abcdefghijklmn'
print(type(is_ok))
if is_ok:
    print('OK!')
else:
    print('NO!')

print('**********************************************************************')

#Listでも有効に使用できる
# is_okに値が入っていないのでfalse
is_ok = []
print(type(is_ok))
if is_ok:
    print('OK!')
else:
    print('NO!')

# is_okに値が入っているのでTrue
is_ok = [1, 2, 3, 4]
print(type(is_ok))
if is_ok:
    print('OK!')
else:
    print('NO!')

## 下記のような冗長な書き方をしなくてもよい。
is_ok = [1, 2, 3, 4]
print(type(is_ok))
if len(is_ok) > 0:
    print('OK!')
else:
    print('NO!')

print('**********************************************************************')

# 以下Falseと判定されるパターン
## False
##0  <- 整数のゼロ
## 0.0 <- float
## '', [], (), {}, set()など中身が空の場合