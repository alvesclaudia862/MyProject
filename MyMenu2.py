print("Vamos montar um cardápio personalizado? ")

breakfast = []
lunch = []
dinner = []

print("Café da manhã:")
for x in range(0, 3):
    opcao = input(f"Digite a {x+1} opção:")
    breakfast.append(opcao)
    if opcao == "leite" or opcao =="queijo" or opcao == "pão":
        print("Alimento não recomendado!")
print("Eis, as opções escohidas: ", breakfast)        

print("Almoço:")
for x in range (0, 4):
    opcao = input (f"Digite a opção {x+1}: ")
    lunch.append(opcao)
    if opcao == "camarão" or opcao == "pimenta":
        print("Alimento não recomendado!")
print("Eis, as opções escolhidas:", lunch)        

print("janta:")
for x in range (0, 4):
    opcao = input(f"Digite a opção{x+1}:")
    dinner.append(opcao)
    if opcao == "camarão" or opcao == "pimenta":
        print ("Alimento não recomendado!")
print("Eis, as apções escolhidas:", dinner)        