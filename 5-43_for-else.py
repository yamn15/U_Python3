print('**********************************************************************')

# forループが終わった際に最後にelseの処理を行う
for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
else:
    print('I ate all!')

print('**********************************************************************')

# forループの場合でも、breakは使用可能。
## forの中のif文に合致した場合、break処理により、forループが終了する（elseが実行されない）
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
      print('stop eating')
      break
    print(fruit)
else:
    print('I ate all!')

