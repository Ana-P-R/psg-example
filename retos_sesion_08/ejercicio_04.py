notas = (10, 61, 00, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)
suma_notas = sum(notas)
canitdad_notas = len(notas)
promedio= suma_notas/canitdad_notas
print ("El Promedio de notas es: ",promedio)
resultados = ("Reprobado", "Aprobado")

print("El alumno esta:", resultados[promedio >= 51])
