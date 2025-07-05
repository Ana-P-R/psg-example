jane_postres = {"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
john_postres = {"Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"}
# Postres en común
postres_comunes = jane_postres.intersection(john_postres)
cantidad_comun = len(postres_comunes)
print(f"Los postres en común son: {postres_comunes}")
print(f"Tienen {cantidad_comun} postres en comun")

total_postres = len(jane_postres.union(john_postres))
print(f"Existe {total_postres} postres diferentes")

#compatibilidad
porcentaje_compatibilidad = (cantidad_comun / total_postres) * 100
print(f"Existe {porcentaje_compatibilidad} % de compatibilidad")

# si son compatibles
son_compatibles = len(jane_postres & john_postres) / len(jane_postres) > porcentaje_compatibilidad
print(f"Son compatibles? {son_compatibles}")

