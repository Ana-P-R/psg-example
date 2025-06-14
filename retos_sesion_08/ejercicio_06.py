def coordenadas(punto1, punto2):
 
    x1, y1 = punto1
    x2, y2 = punto2    
   
    x_medio = (x1 + x2) / 2
    y_medio = (y1 + y2) / 2
    
    return (x_medio, y_medio)
punto1 = (-20, -20)
punto2 = (40, 20)

punto_medio = coordenadas(punto1, punto2)

print("Coordenadas del punto medio:", punto_medio)