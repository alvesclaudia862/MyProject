#Demonstração do uso de funções...
def adicao(x,y):
    return x + y
def subtracao(x, y):
    return x - y
def multiplicacao(x,y):
    return x * y
def divisao(x, y):
    return x / y

print("Digite dois valores inteiros...")
n1 = int(input("x: "))
n2 =  int(input("y: "))
op = input("Qual operação (+, -, * ou /)?")

if op == "+":
    z = adicao(n1,n2)
    print("Resultado da soma:", z)
elif op == "-":
    z = subtracao(n1, n2) 
    print("Resultado da subtração:", z)   
else:
    print("Opção digitada inexistente! ")    
if op == "*":
    z = multiplicacao(n1,n2)
    print("Resultado da multiplicação:", z)
elif op == "/":
    z = divisao(n1,n2)
    print("Resultado da divisão:", z)