#Demonstração de lista por idade...
def apresentar():
    print("Minha idade  é", myage,"anos.")
    return
def conferir(x):
    if x >= 18:
        print("Honda Civic, Gol, Corolla")
    else: 
        print("Xuxa, Peppa, Galinha Pintadinha")    
    return    

myage = int(input("Digite sua idade."))

apresentar()
conferir(myage)