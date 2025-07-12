alimentos = {
    "carne": ["gato", "perro"],
    "zanahoria": ["conejo"],
    "heno": ["conejo", "hamster"],}
print("DICCIONARIO INICIAL")
print(alimentos)
alimentos.update(
    pescado=["gato"],
    semillas=["loro", "perico"],
    croquetas=["perro"])
print("Aniadiendo elementos al Diccionario ")
print(alimentos)

existe_trigo = "trigo" in alimentos
print(f"¿Existe 'trigo' en el diccionario?: {existe_trigo}")
#eliminar
zanahoria = alimentos.pop('zanahoria')
print("Diccionario de alimentos actualizado:")
print(alimentos)