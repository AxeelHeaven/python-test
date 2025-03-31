# input sirve para obtener un mensaje escrito en consola
ocupacion = str(input("Cual es tu ocupación: ")).lower()

descuento = 0

administrador = False

if ocupacion == "estudiante":
    descuento = 25
elif ocupacion == "jubilado":
    descuento = 50

if descuento != 0:
    print(f"Tu descuento es del {descuento}%")
else:
    print("Tu no tienes ningun descuento!")