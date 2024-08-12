#Programa cliente de banco....
nome = input("Digite o nome do cliente: ")
nascimento = input("Digite sua data de nascimento: ")
cpf = input("Digite o seu cpf: ")
valor = input("Digite o valor inicial da sua conta R$: ")
pix = input("Digite o seu Pix: ")
conta = 2.000

print(f"O meu nome é {nome}")
print(f"minha data de nascimento é {nascimento}")
print(f"o meu cpf é {cpf}")
print(f"o valor inicial da minha conta é de R$ {valor} ")
print(f"o meu Pix é {pix}")

if conta > 2.000:
 print("Seu saldo está no azul! ")
elif conta < 2.000:
  print("Seu saldo está no vermelho! ")
else:   
  print("Sua conta está zerada!")
