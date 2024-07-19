#Sistema de avaliação de serviço
print("Avaliação de serviços prestados: ")
servico = input("O serviço foi prestado (sim/não)? ")
avaliacao = int(input("Qual a  nota da avaliação (1/5)? "))

if servico == "sim" and avaliacao == 1:
    print("O serviço foi péssimo! ")
elif servico == "sim" and avaliacao == 2:
    print("O serviço foi ruim! ")
elif servico == "sim" and avaliacao == 3:
    print("O serviço foi razoável! ")
elif servico == "sim" and avaliacao == 4:
    print("O serviço foi razoável!")
elif servico == "sim" and avaliacao == 5:
   print("O serviço foi razoável!")
else: 
   if servico == "não" and avaliacao == 0:
       reclamacao = input("Digite a sua reclamação: ")
   else:
     print("As suas avaliações não fazem sentido!")  