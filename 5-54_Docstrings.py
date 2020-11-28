# 関数に対する説明の書き方
print('**********************************************************************')
print('(1)')

# funcのドキュメントは「""" """」ダブルクォーテーションで囲み、func内に書くのがpythonのルール。※インデントに注意
def example_func(param1, param2):
    """Example function with types documented in the docstring.
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter
    Returns:
        bool: The return value. True for success, False otherwise.
    """
    print(param1)
    print(param2)
    return True

# func.__doc__で、定義されたfuncのドキュメントを確認できる
print(example_func.__doc__)

print('**********************************************************************')

# help関数でもドキュメントを確認できる
help(example_func)

print('**********************************************************************')
