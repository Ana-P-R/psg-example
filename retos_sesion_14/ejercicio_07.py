# Inicializamos el estado
tablero = [[" " for _ in range(3)] for _ in range(3)]
turno_actual = "X"
juego_terminado = False

def mostrar_tablero():
    for fila in tablero:
        print(fila)
    print()

def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return tablero[0][i]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return tablero[0][2]
    return None

def tablero_lleno():
    return all(casilla != " " for fila in tablero for casilla in fila)

def jugar():
    global turno_actual, juego_terminado

    print("¡Bienvenido a Tres en Raya!")
    mostrar_tablero()

    while not juego_terminado:
        print(f"Turno de '{turno_actual}'")
        try:
            fila = int(input("Ingresa la fila (0-2): "))
            columna = int(input("Ingresa la columna (0-2): "))

            if not (0 <= fila < 3 and 0 <= columna < 3):
                print("❌ Posición fuera de rango. Intenta de nuevo.\n")
                continue

            if tablero[fila][columna] != " ":
                print("❌ Esa casilla ya está ocupada. Intenta otra.\n")
                continue

            tablero[fila][columna] = turno_actual
            mostrar_tablero()

            ganador = verificar_ganador()
            if ganador:
                print(f"🎉 ¡Jugador '{ganador}' ha ganado!")
                juego_terminado = True
            elif tablero_lleno():
                print("🤝 ¡Empate!")
                juego_terminado = True
            else:
                turno_actual = "O" if turno_actual == "X" else "X"

        except ValueError:
            print("❌ Entrada no válida. Por favor ingresa números enteros.\n")


jugar()