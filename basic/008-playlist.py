playlist = {
    'canciones': []
}

def app():
    while True:
        playlist['nombre'] = input("Ingresa el nombre de la playlist: ")
        if playlist['nombre'].strip() != "":
            break

    print("\n\nPara terminar agregar canciones coloca 'listo'.")

    while True:
        nomCancion = input("Nombre de la canción para agregar? ")

        if nomCancion.lower() == "listo":
            print(f"\n\nHas terminado de agregar canciónes. Un total de {len(playlist['canciones'])}\n{playlist}")
            break
        elif nomCancion.strip() != "":
            playlist['canciones'].append(nomCancion)
            print(f"Has agregado la cancion '{nomCancion}' correctamente.\n")


app()