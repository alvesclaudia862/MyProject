#Demonstração de tarefas...
print("Vou montar a lista de afazeres....")
tarefas = ["lavar roupas", "lavar louças", "passar roupas", "cuidar do cachorro", "lavar tapetes"]
print("Esta é a minha lista de afazeres:", tarefas)

resposta = input("A primeira tarefa já foi executada (S/N)?")
if resposta == "S":
    print("Vou tirar a primeira tarefa da lista") 
    del(tarefas[0])
    novo = input("Insira uma nova tarefa.")
    tarefas.append(novo)
    print("Conferindo a lista:", tarefas)