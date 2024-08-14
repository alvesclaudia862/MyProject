#Demonstração de 11 jogadores....

print("Essa é a escalação do jogo de hoje...")
jogadores = ["1. Felipe",
              "2. João",
              "3. Léo",
              "4. Erick",
              "5. Everton",
              "6. Cosme",
              "7. Hudson",
              "8. Edson",
              "9. Lucio",
              "10. Bené",
              "11. Luiz"]
for x in jogadores:
    print (x)

print("Substitua o jogador Cosme. ")
del(jogadores[5])
print("Substitua o jogador Edson. ")
del(jogadores[7])
print("Substitua o jogador Léo. ")
del(jogadores[2])

novo = input("insira um novo jogador: ")
jogadores.insert():
print("Conferindo a nova escalação")

print("Escalação atualizada após o intervalo")
for x in jogadores:
    print(x)