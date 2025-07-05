tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

#Conversion
fisica = set(tienda_fisica)
online = set(tienda_online)

# Compras en ambos canales
ambos_canales = fisica & online
print(f"a. Los clientes {ambos_canales} compraron de manera vitual y fisica")

# Compras entienda fisica
solo_fisica = fisica - online
print(f"b. Los clientes {solo_fisica} compraron solo de manera física")

# Compras online
solo_online = online - fisica
print(f"c. Los clientes {solo_online} compraron solo de manera online")