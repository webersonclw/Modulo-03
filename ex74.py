from random import  randint
numeros = (randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:  ', end='')
for n in numeros:
    print(f'{n} ', end= '')
print(f'\nO maior numero foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')
