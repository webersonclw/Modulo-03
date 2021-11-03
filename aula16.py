lanche = ('Hamburguer', 'Suco', 'Pizza','Pudin''')
#Tuplas são imutaveis
for cont in range(0,len(lanche)):
    print(lanche[cont])
print(len(lanche))
for comida in lanche:
    print(f'eu vou comer {comida}')
print(lanche[2])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])