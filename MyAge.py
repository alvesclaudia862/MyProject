#Demonstração do uso de funções
def menor():
    print("Eis, os programas ideais para você: ")
    print("Teletubies, Pepa Pig e Galinha Pintadinha. ")
    print("Se passar das 10h, vai dormir!!! ")
    return
def maior():
    print("Eis, boas opções de  carro para comprar: ")
    print("Corolla, Civic, Gol.....")
    return

print("Digite a sua idade:")
idade = int(input())

if idade < 18:
    menor()
else:
    maior()
