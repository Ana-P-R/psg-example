def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
n = int(input("Ingrese el valor de n para calcular el n-ésimo número de Lucas: "))
print(f"El número de Lucas en la posición {n} es: {lucas(n)}")