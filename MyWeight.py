#Demonstração imc
peso = int(input("Digite o seu peso:"))
altura = int(input("Digite a sua altura: "))
imc = peso / (altura **2) 

print(f"O seu imc é {imc}.")
if imc > 25:
    print ("Você está acima do peso!")
elif imc < 18:    
    print ("Você está abaixo do peso!")
else:
    print("O seu peso está ok!")    