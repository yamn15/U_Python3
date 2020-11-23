print('**********************************************************************')

# while文の条件に合致する場合は、処理をループさせる
count1 = 0

while count1 < 5:
    print(count1)
    count1 += 1
# while文に合致しなかった際にelseの処理を行う
else:
    print('done')

## 処理の流れはデバッガを参照

print('**********************************************************************')

# while文の条件に合致する場合は、処理をループさせる
count2 = 0

while count2 < 5:
# while文の中でbreak条件に合致すると、elseも無視しwhile文の処理がすべて終了する
    if count2 == 1:
        break
    print(count2)
    count2 += 1
# while文に合致しなかった際にelseの処理を行う
## breakで処理をぬけなかった場合にelseの処理へ移る
else:
    print('done')

## 処理の流れはデバッガを参照

print('**********************************************************************')

