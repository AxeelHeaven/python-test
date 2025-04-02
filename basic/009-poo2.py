class Restaurant:

    # es el constructor, donde inicia la clase
    def __init__(self, nombre, categoria, precio):
        print("Ejecucion automatica...")
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio

    def mostrar(self):
        print(f"Nombre: {self.nombre}, y es comida {self.categoria}. Su precio promedio es {self.precio} dolares.")



mexa = Restaurant("Tacos Julio", "Mexicana", 2)
mexa.mostrar()


italiana = Restaurant("Pizza Mario", "Italiana", 5)
italiana.mostrar()