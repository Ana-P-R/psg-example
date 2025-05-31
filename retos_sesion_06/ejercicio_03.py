print("Se utiliza el operador XNOR")
print ("TARJETA  | HUELLA   | PUERTA  ")
print ("------------------------------")
# Caso 1: Ninguna credencial
Tarjeta = False
Huella= False
Puerta = (Tarjeta or Huella) and not (Tarjeta and Huella)
print(Tarjeta,"  | ",Huella,"  | ", Puerta)

# Caso 2: Solo huella 
Tarjeta = False
Huella = True
Puerta = (Tarjeta or Huella) and not (Tarjeta and Huella)
print(Tarjeta,"  | ",Huella,"   | ", Puerta)

# Caso 3: Solo tarjeta
Tarjeta = True
Huella = False
Puerta = (Tarjeta or Huella) and not (Tarjeta and Huella)
print(Tarjeta,"   | ",Huella,"  | ", Puerta)

# Caso 4: Ambas credenciales
Tarjeta = True
Huella = True
Puerta = (Tarjeta or Huella) and not (Tarjeta and Huella)
print(Tarjeta,"   | ",Huella,"   | ", Puerta)