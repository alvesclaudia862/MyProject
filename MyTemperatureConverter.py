#Conversor de temperaturas
print("Converter de Celsius para Kelvin e Fahrenheit...")
celsius = int(input("Digite a temperatura:"))

kelvin = celsius + 273
fahrenheit = (9 /5 * celsius) - 32
print(f"A temperatura em kelvin será {kelvin}).")
print(f"A temperatura em fahrenheit será {fahrenheit}.")

# Seria possível utilizar as estruturas condicionais if/elif/else ou match/case,
# para personlizar este programa, de forma que ele ofereça as trê conversões?
# Por exemplo, ele poderia peguntar ao usuário qual a unidade de medida e qual 
# o valor de temperatura ele quer converter e a partir dai, realizar os cálculos
# necessários...

print("Qual conversão que deseja realizar?")
escolha = int(input("1. Celsius / 2. Kelvin / 3. Fahrenheit: "))
temperatura = int(input("Digite o valor da temperatura: "))

match temperatura:
    case 1:
        kelvin = temperatura + 273
        fahrenheit = (9/5 * temperatura) - 32
        print("A conversão de Celsius para Kelvin será {kelvin}.")
        print(f"A conversão de Celsius para Fahrenheit será {fahrenheit}.")
    case 2 :
        celsius = temperatura - 273
        fahrenheit = 1,8 * (temperatura) - 273 + 32
        print(f"A conversão de Kelvin para Celsius será {kelvin}.")
        print(f"A conversão de Kelvin para Fahrenheit será {fahrenheit} ")
    case 3 :
        celsius = 5/9 * (temperatura - 32)
        kelvin = (temperatura - 32) / 1.8 + 273
        print("A conversão de Fahrenheit para Celsius será {celsius}.")
        print("A conversão de Fahrenheit para Kelvin será {kelvin}.")