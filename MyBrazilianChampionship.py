#Tabela de classificação campeonato brasileiro

print("Cadastro de classificação do campeonato brasileiro")
time = input("Digite o time: ")
posição = int(input("Digite a sua posição: "))

if posição == 1:
   print("Campeão!")
elif posição > 1 and posição <= 6 :
   print("Libertadores!")
elif posição > 7 and posição <= 12 :
   print("Sul-Americana!")
elif posição > 12 and posição <= 16:
   print("Sem classificação")
elif posição >= 17 and posição <=20:
   print("Rebaixado")
else:
   print("Digite a posição correta! ")
