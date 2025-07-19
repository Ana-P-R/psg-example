edad = int(input("Ingrese la edad del cliente: "))
compra = float(input("Ingrese el monto de la compra: "))

if edad > 60 and compra > 1000:
    descuento = 0.20
elif 18 <= edad <= 60 and compra > 500:
    descuento = 0.10
else:
    descuento = 0.02

monto_descuento = compra * descuento
total_a_pagar = compra - monto_descuento


print(f"Descuento aplicado: {descuento * 100} %")
print(f"Monto de descuento: $ {monto_descuento}")
print(f"Total a pagar: $ {total_a_pagar}")