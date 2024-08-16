#Demonstração de OOP em Python...
from abc import ABC, abstractmethod

class cliente:
    @abstractmethod
    def __init__ (self, titular, conta, saldo):
        self.titular = titular
        self._conta = conta
        self._saldo = saldo 

class cliente_fisico(cliente):
    def apresentar(self):
        print ("Olá! Eu sou:", self.titular) 
        print("Minha conta é:", self._conta)
        print("E quero saber o meu saldo. ")
        return
  
#Para criar uma instância baseada na classe Cliente ...
fulano = cliente_fisico("João", "423.050205-21", 25000.00)

#Executando o método da instância criada...
fulano.apresentar()

#Acessando os atributos das instâncias criadas...
print("De fato, você realmente é: ", fulano.titular)
print("No momento, a sua conta possui R$", fulano._saldo)