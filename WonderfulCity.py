#Cidade maravilhosa...
def usuario(nome, cidade):
  if cidade == "Rio de Janeiro":
   print(f"Olá, {nome}! Seja bem-vinda à Cidade Maravilhosa!")
  else:
    print(f"Olá,{nome} ! Você está em {cidade}.")

nome = input("Digite seu nome: ")
cidade =input("Digite a cidade de onde você está digitando: ")

usuario(nome, cidade)