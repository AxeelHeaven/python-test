class Restaurant:

    def add(self, nombre):
        self.nombre = nombre # Atributo

    def mostrar(self):
        print(f"Nombre: {self.nombre}")



tacos = Restaurant()
tacos.add("Tacos Julio")
tacos.mostrar()


birria = Restaurant()
birria.add("Birria Sabrosito")
print(f"La mejor birria es {birria.nombre}")