class Restaurant:

    # es el constructor, donde inicia la clase
    def __init__(self, nombre, categoria, precio):
        print("Ejecucion automatica...")
        self.nombre = nombre # Atributo
        self.categoria = categoria

        # PROTECTED con un _ se protege pero se puede usar/modificar en la clase .py
        # PRIVATED con dos __ se protege, no se puede usar/modificar en ninguna clase .py y unicamente se pueden modificar /usar mediante GETTER/SETTER
        self.__precio = precio 

    def mostrar(self):
        print(f"Nombre: {self.nombre}, y es comida {self.categoria}. Su precio promedio es {self.__precio} dolares.")

    # GETTER - SETTER de PRECIO

    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, precio):
        self.__precio = precio 



mexa = Restaurant("Tacos Julio", "Mexicana", 25)
print(f"{mexa.getPrecio()}")
mexa.setPrecio(15)
mexa.mostrar()


italiana = Restaurant("Pizza Mario", "Italiana", 92)
italiana.mostrar()