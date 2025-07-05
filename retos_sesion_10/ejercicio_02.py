prendas_deportivas_org= ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
prendas_formales_org = ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]
#convercion a conjuntos
prendas_deportivas = set(prendas_deportivas_org)
prendas_formales = set(prendas_formales_org)

#Combinacion
convinacion_estilos = prendas_deportivas.union(prendas_formales)

print("Prendas deportivas:", prendas_deportivas)
print("Prendas formales:", prendas_formales)
print("Combinacion de estilos:", convinacion_estilos)
