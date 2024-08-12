#Revisão geral de algoritmos & lógica de programação...
print("O que você achou dos nossos seviços?")
print("1. Péssimo, 2. Ruim, 3. Razoável, 4. Bom, 5. Ótimo...")
avaliacao = int(input("Digite uma opção: "))

match avaliacao:
    case 1:
        print("O serviço precisa melhorar muito!")
        print ("Avaliação : reprovado!")
    case 2:
        print ("O serviço precisa melhorar em alguns quesitos ...")
        print("Avaliação: reprovado!")
    case 3:
        print ("Nem bom, nem ruim...")
        print("Avaliação: reuperação.")
    case 4:
        print ("Aceitável no geral, embora possa melhorar.")
        print("Avaliação: Aprovado!")
    case 5:
        print ("Perfeito,melhor que isso estraga")
        print("Avaliação: Aprovada!")
    case _:
        print("A opção digitada não está correta!")   
 
print("Obrigada pela atenção!")