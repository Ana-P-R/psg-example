# Diccionario original 
habitats_amenazados = {
    "Polo Norte": {
        "especies": {"Oso polar", "Morsa", "Ballena"},
        "amenazas": ["Derretimiento de hielo", "Cambio climAtico", "ContaminaciOn por plasticos"],
        "prioridad": "Critica"},
    "Amazonas": {
        "especies": {"Tigre", "Mono", "Guacamayo"},
        "amenazas": ["Deforestación", "Agricultura intensiva", "Mineria ilegal"],
        "prioridad": "Alta"}
}
print("DICCIONARIO INICIAL")
print("=== POLO NORTE ===")
print("Especies:", habitats_amenazados.get("Polo Norte").get("especies"))
print("Amenazas:", habitats_amenazados.get("Polo Norte").get("amenazas"))
print("Prioridad:", habitats_amenazados.get("Polo Norte").get("prioridad"))

# Amazonas
print("\n=== AMAZONAS ===")
print("Especies:", habitats_amenazados.get("Amazonas").get("especies"))
print("Amenazas:", habitats_amenazados.get("Amazonas").get("amenazas"))
print("Prioridad:", habitats_amenazados.get("Amazonas").get("prioridad"))
print("---------------------------------------------------------------------------------")
habitats_amenazados.update({
  "Africa Central": {
        "especies": {"Gorila de montaña", "Chimpancé", "Elefante africano", "Leopardo"},
        "amenazas": ["Caza furtiva", "Enfermedades", "Expansión humana"],
        "prioridad": "Media-Alta"},
    "Gran Barrera de Coral": {
        "especies": {"Tortuga verde", "Dugongo", "Pez payaso", "Tiburón de arrecife"},
        "amenazas": ["Blanqueamiento de coral", "Contaminación", "Sobrepesca"],
        "prioridad": "Alta"}
})
print("AÑADIENDO AL DICCIONARIO")
print("=== POLO NORTE ===")
print("Especies:", habitats_amenazados.get("Polo Norte").get("especies"))
print("Amenazas:", habitats_amenazados.get("Polo Norte").get("amenazas"))
print("Prioridad:", habitats_amenazados.get("Polo Norte").get("prioridad"))

# Amazonas
print("\n=== AMAZONAS ===")
print("Especies:", habitats_amenazados.get("Amazonas").get("especies"))
print("Amenazas:", habitats_amenazados.get("Amazonas").get("amenazas"))
print("Prioridad:", habitats_amenazados.get("Amazonas").get("prioridad"))

# Africa Central
print("\n=== AFRICA CENTRAL ===")
print("Especies:", habitats_amenazados.get("Africa Central").get("especies"))
print("Amenazas:", habitats_amenazados.get("Africa Central").get("amenazas"))
print("Prioridad:", habitats_amenazados.get("Africa Central").get("prioridad"))

# Gran Barrera de Coral
print("\n=== GRAN BARRERA DE CORAL ===")
print("Especies:", habitats_amenazados.get("Gran Barrera de Coral").get("especies"))
print("Amenazas:", habitats_amenazados.get("Gran Barrera de Coral").get("amenazas"))
print("Prioridad:", habitats_amenazados.get("Gran Barrera de Coral").get("prioridad"))
print("---------------------------------------------------------------------------------")

existe_amazonas = "Amazonas" in habitats_amenazados
print(f"¿Existe el hábitat 'Amazonas' en el diccionario? {existe_amazonas}")
print("---------------------------------------------------------------------------------")

habitats_amenazados["Amazonas"]["especies"].add("Anaconda")

print("DICCIONARIO FINAL")
# Polo Norte
print("\n=== POLO NORTE ===")
print("Especies:", habitats_amenazados.get("Polo Norte").get("especies"))
print("Amenazas:", habitats_amenazados.get("Polo Norte").get("amenazas"))
print("Prioridad:", habitats_amenazados.get("Polo Norte").get("prioridad"))

# Amazonas
print("\n=== AMAZONAS ===")
print("Especies:", habitats_amenazados.get("Amazonas").get("especies"))
print("Amenazas:", habitats_amenazados.get("Amazonas").get("amenazas"))
print("Prioridad:", habitats_amenazados.get("Amazonas").get("prioridad"))

# Africa Central
print("\n=== AFRICA CENTRAL ===")
print("Especies:", habitats_amenazados.get("Africa Central").get("especies"))
print("Amenazas:", habitats_amenazados.get("Africa Central").get("amenazas"))
print("Prioridad:", habitats_amenazados.get("Africa Central").get("prioridad"))

# Gran Barrera de Coral
print("\n=== GRAN BARRERA DE CORAL ===")
print("Especies:", habitats_amenazados.get("Gran Barrera de Coral").get("especies"))
print("Amenazas:", habitats_amenazados.get("Gran Barrera de Coral").get("amenazas"))
print("Prioridad:", habitats_amenazados.get("Gran Barrera de Coral").get("prioridad"))
