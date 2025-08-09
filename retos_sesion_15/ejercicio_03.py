# Excepción personalizada
class FondosInsuficientesError(Exception):
    def __init__(self, mensaje="Fondos insuficientes para realizar el retiro."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Función cajero
def cajero():
    saldo_disponible = 800  # Puedes cambiar el saldo inicial aquí

    try:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto > 1000:
            raise Exception("El monto excede el límite permitido por transacción (1000).")

        if monto > saldo_disponible:
            raise FondosInsuficientesError()

        saldo_disponible -= monto
        print(f"Retiro exitoso. Su nuevo saldo es: ${saldo_disponible}")

    except FondosInsuficientesError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Advertencia: {e}")

cajero()
