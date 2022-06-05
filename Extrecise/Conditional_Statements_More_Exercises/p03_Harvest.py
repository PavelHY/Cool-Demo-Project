import math

vineyard_X = int(input())
grapes_Y = float(input())
needed_liters_of_wine = int(input())
workers_num = int(input())

debit_grapes = vineyard_X * grapes_Y   # obshto grozde
vine = 0.4 * debit_grapes / 2.5   # proizvedeno vino

if vine < needed_liters_of_wine:
    print(f'It will be a tough winter! More {math.floor(needed_liters_of_wine - vine)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(vine)} liters.')
    print(f'{math.ceil(vine - needed_liters_of_wine)} '
          f'liters left -> {math.ceil((vine - needed_liters_of_wine) / workers_num)} liters per person.')
