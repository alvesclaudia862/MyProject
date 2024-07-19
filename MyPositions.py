#Demosntração de funções em um jogo de futebol

print("Funções no jogo de futebol: ")
funcao = input("Digite a função: ")

if funcao == "goleiro" or funcao == "zagueiro" or funcao =="lateral":
    print("Desfesa! ")
elif funcao ==  "volante" or funcao == "meia" :
    print("Meio-Campo!")
elif funcao == "ponta" or funcao == "atacante" or funcao =="centroavante":
    print("Ataque")
else:
    print("Teimoso!")