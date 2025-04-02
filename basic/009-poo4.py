class Restaurant:
    
    def __init__(self, nombre, categoria, precio):
        print("Ejecucion automatica...")
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio 

    def mostrar(self):
        print(f"Nombre: {self.nombre}, categoria {self.categoria}, precio {self.__precio}.")

    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, precio):
        self.__precio = precio 

#   CREAMOS CLASE PARENT

class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca

    # Metodo unico en la clase Hotel
    def getAlberca(self):
        return self.alberca


hotel = Hotel("Hotel Frambuesa", "5 Estrellas", 250, True)
hotel.mostrar()
print(f"Tiene alberca=? {"Si" if hotel.getAlberca() else "No"}")