#Demonstrativo de dia da semana 
print("Digite o dia da semana")
print("1. segunda")
print("2. terça")
print("3. quarta")
print("4. quinta")
print("5. sexta")
print("6. sábado")
print("7. domingo")
semana = int(input())



match semana:
    case 1:
        print("Aula de tênis")
    case 2:
        print("Fazer ioga")
    case 3:
        print("Fazer curso de Python") 
    case 4:
        print("Fazer compras")   
    case 5:
        print("Dia de fazer as unhas")
    case _:
        print("Verificar sua agenda")