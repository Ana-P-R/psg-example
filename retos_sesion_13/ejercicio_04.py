while True:
    frase = input("Ingresa una frase (escribe 'salir' para terminar): ")
    
    if 'salir' in frase.lower():
        print("Programa terminado.")
        break

    frase_min = frase.lower()
    if frase_min == frase_min[::-1]:
        print(f"✅ '{frase}' SÍ es un palíndromo.")
    else:
        print(f"❌ '{frase}' NO es un palíndromo.")