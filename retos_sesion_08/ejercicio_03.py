
entrada = input("Escribe una pregunta: ")

pregunta = (entrada,)

pregunta_concatenada = ('¿',) + pregunta + ('?',)

print("Pregunta formateada:", pregunta_concatenada)

pregunta_doble = pregunta_concatenada * 2

print("Pregunta repetida 2 veces:", pregunta_doble)