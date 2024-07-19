#Demonstração de média com duas notas escolares
print("Digite sua média")
nota1 = int(input("Digite a nota 1:"))
nota2 = int(input("Digite a nota 2:"))
média = (nota1 + nota2) / 2

if média < 4:
    print ("Você está Reprovado!")
elif média >= 6:
    print("Você está aprovado direto!")
else: 4 <= média < 6
print("Você está em recuperação! ")
nota_recuperação = int(input("Digite a nota da recuperação: "))
if nota_recuperação < 5:
    print("Reprovado na recuperação!")
else:
    print ("Aprovado na recuperação!")
