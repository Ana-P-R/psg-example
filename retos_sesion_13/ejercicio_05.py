for fila in range(8):  
    for columna in range(8):  
        if (fila + columna) % 2 == 0:  
            print('#', end='  ')  
        else:  
            print('*', end='  ')  
    print()  # Salto de línea