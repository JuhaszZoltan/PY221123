from random import randint
# import random

# előállít egy véletlen számot [10; 99] között:
rnd_num:int = randint(10, 99)
print(rnd_num)

f31:int = randint(100, 999)
print(f31)

f32:float = randint(0, 250) / 10
print(f32)

f33:float = randint(150, 250) / 10
print(f33)

f34:int = randint(0, 49) * 2
print(f34)

f35:int = randint(20, 40) * 5
print(f35)

print(f'''
{randint(1, 6)}|{randint(1, 6)}
{randint(1, 6)}|{randint(1, 6)}
{randint(1, 6)}|{randint(1, 6)}
''')

a:int = randint(10, 50)
b:int = randint(10, 50)
pred:int = int(input(f'{a} + {b} = '))

if pred == a+b: print('valóban')
else: print(f'nem, az összeg {a + b}')