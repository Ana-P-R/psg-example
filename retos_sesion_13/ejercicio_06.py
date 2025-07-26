while True:
    num = int(input("Ingresa un número (0 para salir): "))
    
    if num == 0:
        print("Programa terminado.")
        break
    
    if num % 7 == 0:
        print(f"{num} es múltiplo de 7.")
    else:
        print(f"{num} NO es múltiplo de 7.")