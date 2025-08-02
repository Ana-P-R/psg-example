def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

calificaciones = [50, 75, 80, 91, 70]

promedio = calcular_promedio(calificaciones)
print("El promedio de las calificaciones es:", promedio)