carros = ['Ferrari', 'Fusca', 'Civic']
print(carros)
print(carros[2])#possição da lista
print(carros[0].title())#letra maiuscula
print("Eu gostaria de ter uma " + carros[0].title())

carros[1] = 'mustang'#mudar algum elemento da lista
print(carros)

carros.append('BMW')#acresentar um elemento no final da lista
print(carros)

carros.insert(1, 'jeep')#iserir um elemto em uma pocissão especifica
print(carros)

del carros[1]#deleta o elemento de uma pocissão especifica
print(carros)

carros.pop()#deleta o ultimo elemento da lista
print(carros)

carros.sort()#organizar em ordem alfabetica
print(carros)


