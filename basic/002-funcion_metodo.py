blocked = ["carajo", "repampanos"]

def transformarTexto(mensaje):

    for palabra in blocked:
        # cambiamos el mensaje, pero tenemos que ponerlo todo en mayuscula para que lo reconozca y asi remplazar.
        # '*' * len(palabra) - Esta parte es para contar la cantidad de caracteres de la palabra y lo multplicamos por *
        mensaje = mensaje.upper().replace(palabra.upper(), '*' * len(palabra))
        
    # capitalize - pone la primera letra en mayuscula y las demas en minisculas.
    return mensaje.capitalize()


print(transformarTexto("HOLA CARAJO, COMO REPAMPANOS ESTA EL CHAT."))