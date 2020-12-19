# ラムダ
#
print('*********************************************')
print('(1)')

# 前提：先頭が大文字(capital)出なければならいルールの文字列
## 以下の文章は小文字が混ざっている
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri']

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
