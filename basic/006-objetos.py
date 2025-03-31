producto = {
    'id': "0001",
    'nombre': "Jugo de Tomate",
    'precio': 520,
    'descripcion': "Es un jugo de tomate sin azucar.",
}

print(f"El precio del producto {producto['nombre']} es de ${producto['precio']}")


del producto['descripcion']

print(producto.get('id'))

print(producto)

