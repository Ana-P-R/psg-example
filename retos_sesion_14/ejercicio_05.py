def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in cadena if letra in vocales)

texto = input("Introduce una cadena de texto: ")
resultado = contar_vocales(texto)

print(f"La cadena tiene {resultado} vocales.")