# ラムダ
#
print('*********************************************')
print('(1)')

# 前提：先頭が大文字(capital)出なければならいルールの文字列
## 以下の文章は小文字が混ざっている
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

# sample_funcは実行ではなく、オブジェクトを渡す
change_words(l, sample_func)

# change_words(l, sample_func)の    処理スタート
## L10のchange_wordsに引数が渡される。

print('*********************************************')
print('(2)')

# lambdaを使用すれば、上記のプログラムをシンプルにできる

l2 = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words2(words, func):
    for word in words:
        print(func(word))

sample_func2 = lambda word: word.capitalize()

change_words2(l2, sample_func2)


print('*********************************************')
print('(3)')

# lambdaには下記の記述方法もある

l3 = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words3(words, func):
    for word in words:
        print(func(word))

change_words3(l3, lambda word: word.capitalize())

print('*********************************************')
print('(4)')

# lambdaは複数の処理を簡略化させたいときに使用される。特に関数を引数として使用する場合
## 以下は、冗長な構文

l4 = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words4(words, func):
    for word in words:
        print(func(word))

def sample_func4_1(word):
    return word.capitalize()

# 複数の処理を実行する場合はどんどん関数を増やす必要がある
def sample_func4_2(word):
    return word.lower()

change_words4(l4, sample_func4_1)
print('--------------------------')
change_words4(l4, sample_func4_2)

print('*********************************************')
print('(5)')

# lambdaを使用すれば、codeがシンプルになる

l5 = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words4(words, func):
    for word in words:
        print(func(word))

change_words4(l5, lambda word: word.capitalize())
print('--------------------------')
change_words4(l5, lambda word: word.lower())




