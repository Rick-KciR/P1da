lista = [1,2,3,4]

print(lista)

lista.append(5)

print(lista)

lista.insert(1, 2.5)

print(lista)

lista.insert(4, 3.5)

print(lista)

#extend
lista2 = [99,98,97]

lista.extend(lista2)

print(lista)

#pop

lista.pop()

print(lista)

lista.pop(1)

print(lista)

lista.remove(3.5)

print(lista)

lista.insert(2, 2)

print(lista)

print('Quantidade de 2  na lista: ', lista.count(2))

print('Índice do elemnto 99: ', lista.index(99))

#ordenando a lista
lista.insert(3, 100)
lista.insert(0, 25)

print(lista)

lista.sort()

print(lista)

lista.sort(reverse=True)

print(lista)

print(len(lista))

#sum: somando os elementos da lista

print(sum(lista))

#maior elemento da lista:

print('Maior elemento da lista: ', max(lista))

#menor elemento da lista

print('Menor elemento da lista: ', min(lista))