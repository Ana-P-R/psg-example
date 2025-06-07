print("1. Funcion expandtabs")# reemplazar los caracteres de tabulación (\t) por espacios
texto = "Nombre\tEdad\tCiudad"
print("Original:")
print(texto)

print("\nCon expandtabs(4):")
print(texto.expandtabs(4))

print("\nCon expandtabs(10):")
print(texto.expandtabs(10))

print("==================================")
print("2. Funcion center")#centra el texto 
texto = "Python"
print(texto.center(20))
print("==================================")
print("3. Funcion index")#
texto = "Aprendiendo Python"
posicion = texto.index("Python")
print(f"La palabra 'Python' comienza en el índice: {posicion}")
print("==================================")
print("4. Funcion isspace")#comprueba si todos los caracteres de una cadena son espacios en blanco.
texto1 = "   "
print(texto1.isspace())  # True

# Espacio, tabulación y salto de línea
texto2 = " \t\n"
print(texto2.isspace())  # True

# Cadena vacía
texto3 = ""
print(texto3.isspace())  # False

# Espacio con letra
texto4 = " a la "
print(texto4.isspace())  # False

print("==================================")
print("5. Funcion isspace")#verifica si todos los caracteres alfabéticos en una cadena están en mayúsculas
palabra = "HOLA"
print(palabra.isupper())  # True

palabra2 = "Hola"
print(palabra2.isupper())  # False