# print ("Inicio")
# condicion = True
# if condicion:
#     # Bloque de código
#     print ("Cumple condición")
# print ("Fin")

# print ("Inicio")
# numero = 4
# if numero % 2 == 0: # Si el módulo de 2 es 0
#     print ("El número es par")
# print ("Fin")

# print ("Inicio")
# condicion = False
# if condicion:
#     # Bloque de código
#     print ("Cumple condición")
# else:
#     # Bloque de código
#     print ("No cumple condición")
# print ("Fin")

# print ("Inicio")
# numero = 3
# if numero % 2 == 0: # Si el módulo de 2 es 0
#     print ("El número es par")
# else:
#     print ("El número es impar")
# print ("Fin")

# print ("Inicio Anidado")
# condicion_1 = True
# condicion_2 = False
# if condicion_1:
#     print ("Cumple condición 1")
#     if condicion_2:
#         print ("Cumple condición 2")
#     else:
#         print ("No cumple condición 2")
# else:
#     print ("No cumple condición 1")
# print ("Fin")

# print ("Inicio Par, Impar o Cero")
# numero = 0  
# if numero > 0 or numero < 0:
#     if numero % 2 == 0: # Si el módulo de 2 es 0
#         print ("El número es par")
#     else:
#         print ("El número es impar")
# else:
#     print ("El número es cero")
# print ("Fin")

# print ("Inicio ELIF")
# condicion_1 = False
# condicion_2 = True
# if condicion_1:
#     print ("Cumple condición 1")
# elif condicion_2:
#     print ("Cumple condición 2")
# else:
#     print ("No cumple condición 1 ni 2")
# print ("Fin")

# numero = 0
# if numero == 0:
#     print("es cero")
# elif numero % 2 == 0:
#     print("es par")
# else:
#     print("es impar")

# print ("Inicio Ternario")
# condicion = True
# resultado = "Cumple" if condicion else "No cumple"
# print (resultado)
# print ("Fin")

# print ("Inicio Ternario Par, Impar")
# numero = 3
# #resultado = "El número es par" if numero % 2 == 0 else "El número es impar"
# resultado = ("El número es par" 
#              if numero % 2 == 0 
#              else "El número es impar")
# print (resultado)
# print ("Fin")

# print ("Truthiness Enteros")
# dividendo = int(input("Dividendo: "))
# divisor = int(input("Divisor: "))
# print (dividendo,divisor)
# if divisor: #divisor != 0
#     print (dividendo / divisor)
# else:
#     print ("No se puede dividir entre cero")
# print ("Fin")

# print ("Truthiness Flotantes")
# dividendo = float(input("Dividendo: "))
# divisor = float(input("Divisor: "))
# print (dividendo,divisor)
# if divisor: #divisor != 0.0
#     print (dividendo / divisor)
# else:
#     print ("No se puede dividir entre cero")
# print ("Fin")

# print ("Truthiness Cadenas")
# cadena = input("Cadena: ")
# print (cadena)
# if cadena: # len(cadena) != 0 or cadena != "" 
#     print ("La cadena no está vacía")
# else:
#     print ("La cadena está vacía")
# print ("Fin")


# print ("Truthiness Listas")
# lista = list(input("Lista: "))
# print (lista)
# if lista: # len(lista) != 0 or lista != []
#     print ("La lista no está vacía")
# else:
#     print ("La lista está vacía")
# print ("Fin")

# print ("Truthiness Conjuntos")
# conjunto = set(input("Conjunto: "))
# print (conjunto)
# if conjunto: # len(conjunto) != 0 or conjunto != set()
#     print ("El conjunto no está vacío")
# else:
#     print ("El conjunto está vacío")
# print ("Fin")

# print ("Truthiness Diccionarios")
# diccionario = {}
# clave = input("Clave: ")
# valor = input("Valor: ")
# if clave:
#   diccionario = {clave:valor}
# print (diccionario)
# if diccionario: # diccionario != {}
#     print ("El diccionario no está vacío")
# else:
#     print ("El diccionario está vacío")
# print ("Fin")


# entero = int(input("Entero: "))
# resultado = "Diferente de 0" if entero else "Igual a 0"
# print (resultado)
# flotante = float(input("Flotante: "))
# resultado = "Diferente de 0.0" if flotante else "Igual a 0.0"
# print (resultado)
# cadena = input("Cadena: ")
# resultado = "No está vacía" if cadena else "Está vacía"
# print (resultado)

#Tienes un dispositivo que mide la temperatura y si la temperatura es mayor a 30°C enciende un ventilador y si es menor a 20°C lo apaga
# temperatura = float(int(input("ingrese la tempreratura: ")))
# if temperatura > 30:
#     print("Ventilador encendido")
# elif temperatura < 20:
#     print("ventilador apagado")
# else:
#     print("Temperatura normal")

# cesta = ['🍎','🍑','🍓','🍉']
# print (cesta)
# if '🍎' in cesta:
#     print (f"Hay {cesta.count('🍎')} manzanas")
# else:
#     cesta.extend(['🍎','🍎'])
#     print (cesta)

cesta = ['🍑','🍓','🍉']
print (cesta)
resultado = f"Hay {cesta.count('🍎')} manzanas" if '🍎' in cesta else cesta.extend(['🍎','🍎'])
print (resultado)
print (cesta)