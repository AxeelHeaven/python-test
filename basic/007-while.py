opened = True

while opened:
    numero = int(input("Ingresa un numero par... \n"))

    if numero % 2 == 0:
        print(f"El numero {numero} si es par!!!!")
        opened = False
    else:
        print(f"Este numero no es par")