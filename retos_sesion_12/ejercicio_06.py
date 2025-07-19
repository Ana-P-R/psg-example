entrada = input("Introduzca la Operación separando con coma: ")

partes = entrada.split(',')

if len(partes) == 3:
    num1 = partes[0]
    num2 = partes[1]
    operacion = partes[2]

    if num1 != "" and num2 != "":
        num1 = float(num1)
        num2 = float(num2)

        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: división por cero"
        else:
            resultado = "Operación no válida"
    else:
        resultado = "Números vacíos"
else:
    resultado = "Formato incorrecto"

print("-------------")
print("Resultado:", resultado)
