alimentos = ['Tomate', 'Batata', 'Uva', 'Banana', 'ovos', 'pão', 'pizza']

print(alimentos[2:5])
print(alimentos[::2])#pulando de 2 em 2
print(alimentos[-3:])#pegando os 3 ultimos

for alimento in alimentos[:5]:
    print(alimento)