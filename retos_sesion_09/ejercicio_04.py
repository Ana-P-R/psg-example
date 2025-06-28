lista_productos=["Oreo", "Bon Bon Bum", "Chizitos", "Galletas Monolito","Pilfrut"]
lista_precios=[2.50, 0.70, 1.0, 1.20,1.50]
print(lista_productos)
print(lista_precios)
#agregacion de productos
lista_productos.append("Gomitas")
lista_precios.append(2.80)
lista_productos.append("Pipocas")
lista_precios.append(1.20)

#elminacion de producto
index = lista_productos.index("Bon Bon Bum")
lista_productos.pop(index)
lista_precios.pop(index)

print(lista_productos)
print(lista_precios)

#costo de oreo y chizito
precio_oreo = lista_precios[lista_productos.index("Oreo")]
precio_chizitos = lista_precios[lista_productos.index("Chizitos")]
print("Precio de Oreo:", precio_oreo)
print("Precio de Chizitos:", precio_chizitos)

#precio maximo y precio minimo
precio_maximo = max(lista_precios)
producto_mas_caro = lista_productos[lista_precios.index(precio_maximo)]
precio_minimo = min(lista_precios)
producto_mas_barato = lista_productos[lista_precios.index(precio_minimo)]
print("El producto más caro:", producto_mas_caro, "-", precio_maximo)
print("El producto más barato:", producto_mas_barato, "-", precio_minimo)
#cantidad total de productos
total_productos = len(lista_productos)
print("El total de productos es:", total_productos)
#suma de precios de los productos
total_precio = sum(lista_precios)
print("El costo total de todos los productos:", total_precio)

#ordenado del mas barato al mas caro
ordenados = sorted(zip(lista_precios, lista_productos)) 
lista_precio_ordenada, lista_productos_ordenada = zip(*ordenados)
lista_precio = list(lista_precio_ordenada)
lista_productos = list(lista_productos_ordenada)
print("Productos:", lista_productos)
print("Precios:", lista_precio)

#Eliminacion de todos los productos
lista_productos.clear()
lista_precios.clear()
print("Productos:", lista_productos)
print("Precios:", lista_precios)