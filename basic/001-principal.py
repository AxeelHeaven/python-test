nombre = "Axel"
edad = 17

if edad >= 18:
    print(nombre + " es mayor de edad.")
else:
    print(nombre + " es menor de edad.")



def saludo(nombre, ocupacion, mayoriaEdad = True):
    print(f'Mi nombre es {nombre}, soy {ocupacion} y soy {"mayor" if True else "menor" } de edad.')

saludo(nombre, "programador")
saludo("Monica", "Ingeniero")
saludo("Karla", "estudiante", False)