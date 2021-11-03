tabela = ('Atletico-MG', 'Palmeiras', 'Flamengo', 'Bragantino', 'Fortaleza',
          'Corinthians', 'Internacional', 'Fluminence', 'America-MG', 'Cuiba',
          'Atletico-GO', 'São Paulo', 'Ceara- SC', 'Athletico-PR', 'Santos',
          'Bahia', 'Sport Recife', 'Juventude', 'Gremio', 'Chapecoence')
#print(f'{tabela}')
print(('-=' * 15))
print(f'Lista de times do Brasileirão: {tabela}')
print(('-=' * 15))
print(f'Os 5 Primeiros são {tabela[0:5]}')
print(('-=' * 15))
print(f'Os 4 ultimos são {tabela[-4]}')
print(('-=' * 15))
print(f'Em ordem alfabetica é {sorted(tabela)}')
print(('-=' * 15))
print(f'O Gremio esta em {tabela.index("Gremio")+1}º colocado')