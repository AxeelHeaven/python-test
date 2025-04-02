# AQUI COMIENZO A USAR snake_case PARA PROGRAMAR es mejor.

import os

CARPETA = "basic/contactos/"
EXTENSION = ".txt"

def app():

    crear_directorio()

    mostrar_opciones()

    # aqui preguntaremos que opcion va elegir
    while True:
        opcion = int(input("\nElija una opción: "))

        if opcion == 1:
            agregar_contacto()
            break
        elif opcion == 2:
            editar_contacto()
            break
        elif opcion == 3:
            mostrar_contactos()
            break
        elif opcion == 4:
            buscar_contacto()
            break
        elif opcion == 5:
            eliminar_contacto()
            break
        elif opcion == 6:
            print("\n\nSaliste de la aplicación.\n")
            break
        else:
            print("Esta opcion no es valida")

def eliminar_contacto():
    print("\nIngresa el nombre del contacto que desee eliminar.")
    nombre = input("Nombre del contacto: ")

    if not existe_contacto(nombre):
        print("\n\nESTE CONTACTO NO EXISTE!")
        return app()
    
    os.remove(CARPETA + nombre + EXTENSION)
    print("\nContacto eliminado.\n")

def buscar_contacto():
    print("\nEscribe el nombre del contacto que desee buscar.")
    nombre = input("Nombre del contacto: ")

    if not existe_contacto(nombre):
        print("\n\nESTE CONTACTO NO EXISTE!")
        return app()
 
    print("\r\n")

    with open(CARPETA + nombre + EXTENSION) as contacto:
        for linea in contacto:
            if not linea.strip():
                continue
            print(linea.rstrip())   

    print("\r\n")
    contacto.close()

def mostrar_contactos():
    files = os.listdir(CARPETA)
    files = [i for i in files if i.endswith(EXTENSION)]

    for file in files:
        with open(CARPETA + file) as contacto:
            for linea in contacto:
                if not linea.strip():
                    continue
                print(linea.rstrip())
            print("\r\n")
            contacto.close()

def editar_contacto():
    print("\nEscribe el nombre del contacto que desee editar.")
    nombre = input("Nombre del contacto: ")

    if not existe_contacto(nombre):
        print("\n\nESTE CONTACTO NO EXISTE!")
        return app()
    
    nuevo_nombre = input("Nuevo nombre del contacto: ")
    numero = input("Nuevo nuevo telefonico: ")
    ocupacion = input("Nueva ocupación: ")
    
    with open(CARPETA + nombre + EXTENSION, "w") as file:
        file.write("Nombre: " + nuevo_nombre + "\r\n")
        file.write("Numero: " + numero + "\r\n")
        file.write("Ocupacion: " + ocupacion + "\r\n")

    file.close()

    # Renombramos el archivo 
    os.rename(CARPETA + nombre + EXTENSION, CARPETA + nuevo_nombre + EXTENSION)

    print("\nContacto editado correctamente.\n")
    return app()

def agregar_contacto():
    print("\nEscribe los datos para agregar un nuevo contacto.")
    nombre = input("Nombre del contacto: ")

    # verificacion si existe
    if existe_contacto(nombre):
        print("\n\nESTE USUARIO YA EXISTE!")
        return app()
    
    numero = input("Numero telefonico: ")
    #while len(numero) != 10:
    #    numero = input("Numero telefonico: ")
    ocupacion = input("Ocupación: ")

    with open(CARPETA + nombre + EXTENSION, "w") as file:
        file.write("Nombre: " + nombre + "\r\n")
        file.write("Numero: " + numero + "\r\n")
        file.write("Ocupacion: " + ocupacion + "\r\n")

    file.close()

    print("\nContacto creado correctamente.\n")
    return app()

def crear_directorio():
    # Si no existe la carpeta se va crear
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

def mostrar_opciones():
    print(f"\nSeleccionar la opcion para lo que desee.")
    print(f"1.- Agregar nuevo contacto.")
    print(f"2.- Editar contacto existente.")
    print(f"3.- Ver contactos.")
    print(f"4.- Buscar contacto.")
    print(f"5.- Eliminar contacto")
    print(f"6.- Salir de la aplicación")

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


app()