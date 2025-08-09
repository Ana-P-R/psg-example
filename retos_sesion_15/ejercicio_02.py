class FrutaNoValidaError(Exception):
    def __init__(self, fruta):
        super().__init__(f"❌ La fruta '{fruta}' no es válida.")
        self.fruta = fruta

# Frutas que si están permitidas
frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]

# Lista 
canasta = []

print("=== Canasta de Frutas ===")
print("Ingresa una fruta (una por una). Escribe 'salir' para terminar.")
print("Frutas permitidas:", " ".join(frutas_permitidas), "\n")

while True:
    fruta = input("Ingresa una fruta: ").strip()

    if fruta.lower() == "salir":
        print("\n✅ Has terminado de armar tu canasta.")
        break

    try:
        if fruta not in frutas_permitidas:
            raise FrutaNoValidaError(fruta)
        canasta.append(fruta)
        print(f"✔️  '{fruta}' añadida a la canasta.\n")
    except FrutaNoValidaError as e:
        print(e, "\n")
    except Exception as e:
        print(f"⚠️ Ocurrió un error inesperado: {e}\n")

#canasta final
print("🍓 Tu canasta de frutas contiene:")
print(" ".join(canasta) if canasta else "¡Está vacía!")
