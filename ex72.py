cont = ('zero', 'um', 'dois', 'tres',
        'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze',
        'desesseis', 'desessete',
        'dezoito', 'desenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
        print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')
