#Dados banacários do Cliente...
print("Qual operação você deseja execuatar? ")
print("1. Saldo, 2.Depósito, 3. Saque")
operacao = int(input("Digite uma das opções. "))
saldo = 0
match operacao:
    case 1:
        print(f"O saldo atual é {saldo}")
    case 2:
        deposito = float(input("Digite o valor de depósito: ")) 
        saldo = saldo + deposito
    case 3: 
        saque =int(input("Digite o valor a ser sacado:"))
        if saque > saldo:
             print("Não poderá fazer saque maior que o salário!")
        else:
            saldo = saldo - saque
    case _:
        print("Operação inexistente!")             
        