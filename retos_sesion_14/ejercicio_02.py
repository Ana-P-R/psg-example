def operacion(numero1,numero2,operacion):
    if(operacion == "+"):
        return(numero1+numero2)
    elif(operacion == "-"):
        return(numero1-numero2)
    elif(operacion == "*"):
        return(numero1*numero2)
    elif(operacion == "/"):
        if numero1 != 0:  
            return numero1 / numero2
        else:
            return "Error: No se puede dividir entre cero."
resultado= operacion(10,5,"+")
print (resultado)