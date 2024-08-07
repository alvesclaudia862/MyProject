#Demonstração de uso de funções...
def apresentar():
    print("Meu nome é", myname ,".")
    print("Minha altura é de", myheigh, "metros")
    print("Minha idade  é", myage,"anos.")
    return
def conferir(x):
    if x >= 18:
        print("Você é maior de idade!")
    else:
        print("Ops, menor de idade não pode!")
    return

myname = str(input("Digite o seu nome: "))
myheigh = float (input("Digite a sua altura: "))
myage = int(input("Digite a sua idade: "))

apresentar()
conferir(myage)
