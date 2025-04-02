def app():
    # Para abrir el archivo y w para crearlo
    archivo = open("file.txt", "w") # Ver como funciona open: https://www.w3schools.com/python/ref_func_open.asp

    for i in range(0, 10):
        archivo.write(f"Esta es la linea {i}\n")

    # Cerrar el archivo para evitar uso de memoria
    archivo.close()

app()