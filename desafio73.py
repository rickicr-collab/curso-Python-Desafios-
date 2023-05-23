# crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol.na ordem de colocação depois mostre:

# (A) - Apenas os 5 primeiros colocados 
# (B) - Os ultimos 4 colocados da tabela.
# (C) - Uma lista com os times em ordem alfabetica.
# (D) - Em que Posição na tabela está o time da chapecoense

times = ('Botafogo','Palmeiras','Fluminense','Cruzeiro',
         'Atletico-PR','Atletico-MG','Santos','Fortaleza',
         'Flamengo','São Paulo','Grêmio','Internacional',
         'Bragantino','Bahia','Goiás','Vasco da Gama',
         'Corinthians','Cuiabá','Coritiba','America-MG')
print('-=-' * 16)
print(f'os 5 primeiros colocados são {times[0:5]}')
print('-=-' * 16)
print(f'O ultimos 4 colocados na tabela são {times[-4:]}')
print('-=-' * 16)
print(f'Os times em lista alfabetica ordenada são: {sorted(times)}')
print('-=-' * 16)
