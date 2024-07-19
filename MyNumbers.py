#Informe se os números estão em ordem crescente ou decrescente
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))

if x < y and y < z:
    print("Estão em ordem crescente! ")
elif x > y and y > z:
    print("Estão em ordem decrescente! ")
else:
    print("Estão misturados...")
