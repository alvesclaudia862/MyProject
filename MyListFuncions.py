#Demonstração de funções em listas...
#len():retorna a quantidade de elementos
#max():retorna o maior valor de um conjunto de elementos 
#min(): retorna o menor valor de um conjunto de elementos
#sorted(): reordena os elementos presentes em ordem crescente.
#sum(): retorna o somatório de todos os elementos

numeros = [7, 2, 9, 6, 5, 0, 3, 8, 1, 4]
palavras = ["olá", "alô", "hei", "uau", "ops"]

print("Quantas variáveis possui:")
print("Números:", len(numeros))
print("Palavras:", len(palavras))

print("Vamos reordenar estas listas?")
print(sorted(numeros))
print(sorted(palavras))

print("O somatório de números:", sum(numeros))
print("Qual é o maior valor?", max(numeros))
print("Qual é a primeira palavra?", min(palavras))