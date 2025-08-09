def calculadora():
    print("____Calculadora____ ")
    print("Escribe 'salir' en cualquier momento para terminar.\n")

    while True:
        try:
            entrada1 = input("Ingresa el primer numero: ")
            if entrada1.lower() == "salir":
                print("Saliendo de la calculadora.")
                break

            entrada2 = input("Ingresa el segundo numero: ")
            if entrada2.lower() == "salir":
                print("Saliendo de la calculadora.")
                break

            num1 = float(entrada1)
            num2 = float(entrada2)

            # Operaciones
            suma = num1 + num2
            resta = num1 - num2
            multiplicacion = num1 * num2

            try:
                division = num1 / num2
            except ZeroDivisionError:
                division = "Error: No se puede dividir entre cero."

            # Resultados
            print("\n--- Resultados ---")
            print(f"{num1} + {num2} = {suma}")
            print(f"{num1} - {num2} = {resta}")
            print(f"{num1} * {num2} = {multiplicacion}")
            print(f"{num1} / {num2} = {division}\n")

        except ValueError:
            print("Error: Debes ingresar solo números o 'salir'.\n")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}\n")

calculadora()
