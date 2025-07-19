
nombre = input("Nombre: ")
telefono = input("Telefono: ")

if nombre != "" and len(telefono) == 12 and telefono[0] == "+":
    print("-------------")
    print("Contacto guardado")
else:
    print("-------------")
    print("Datos incorrectos")
