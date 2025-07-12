# Diccionario inicial del Arca 
arca_de_noe = {
    "🐶": 2,  
    "🐱": 2,  
    "🐯": 2,  
    "🐵": 2,  
    "🦄": 0,  
    "🦒": 1
}
print("Diccionario inicial")
print(arca_de_noe)

# Añadir 3 especies 
arca_de_noe.update({
    "🐘": 2,  
    "🦁": 2,  
    "🐍": 2  
})
print("Añadiendo al diccionario")
print(arca_de_noe)

#lista iterando el diccionario
iterador = iter(arca_de_noe.items())
print("Lista de animales:")
animal1 = next(iterador)
print(animal1, type(animal1))
animal2 = next(iterador)
print(animal2, type(animal2))
animal3 = next(iterador)
print(animal3, type(animal3))
animal4 = next(iterador)
print(animal4, type(animal4))
animal5 = next(iterador)
print(animal5, type(animal5))
animal6 = next(iterador)
print(animal6, type(animal6))
animal7 = next(iterador)
print(animal7, type(animal7))
animal8 = next(iterador)
print(animal8, type(animal8))
animal9 = next(iterador)
print(animal9, type(animal9))

# si existe el dragón
existe_dragon = "🐲" in arca_de_noe
print("¿Existe el dragón en el arca?", existe_dragon)

# Eliminar unicornio
del arca_de_noe["🦄"]
print("Eliminando unicornio del diccionario")
print(arca_de_noe)

# Modificar la cantidad de jirafas 
arca_de_noe["🦒"] = 2
print("Modificando la cantidad de jirafas")
print(arca_de_noe)

#Vaciar el arca después del diluvio
arca_de_noe.clear()

# diccionario final
print("Estado final del arca:")
print(arca_de_noe) 