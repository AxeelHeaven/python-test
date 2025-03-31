meses = ["Enero", "Febreiro", "Marzo", "Abril", "Mayo", "Junio",]

# Los meses van del 0 al size-1
print(f"El segundo mes del año es {meses[1]}")

# Para modificar la lista seria
meses[1] = "Febrero"

# Para agregar un mes seria
meses.append("Julio")

# Para eliminar el mes seria
del meses[0]

# Para eliminar el ultimo elemento de la lista seria
meses.pop() # tambien podemos agregar el valor [1] par eliminar cierta posicion

# Para eliminar por elemento
meses.remove("Marzo")

# Ordenar los meses del A-Z
meses#.sort()
print(meses)