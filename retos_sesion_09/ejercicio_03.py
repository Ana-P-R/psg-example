lista_personas = ["Ana", "Luis", "Noemi", "Kevin", "Elena", "Jose", "Pedro", "Zulema", "Ruth", "Diego"]
print (lista_personas)
sublista = lista_personas[5:10:2]
print("Sublista:", sublista)
# busca el valor 
valor = "Jose"
print (valor, lista_personas.index(valor))
# ordenar sublista de a-z
sublista.sort()
print("Sublista ordenada A-Z:", sublista)
#ordenar de la Z-A lista origunal
lista_personas.sort(reverse=True)
print("Lista original ordenada Z-A:", lista_personas)