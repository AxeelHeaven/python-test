def app():

    # Para abrir el archivo
    # R para leer los archivos

    with open("basic/file.txt", "r") as file:
        for contenido in file:
            print(contenido.rstrip()) # Para quitar saltos de linea: .rstrip()

    # Cuando usamos with open, no es necesario cerrarlo.

app()