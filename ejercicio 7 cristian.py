def mostrar_con_marcado(texto):
    # Dividimos el texto en palabras
    palabras = texto.split()
    
    # Encontramos la longitud de la palabra más larga para el ancho del marco
    max_longitud = max(len(palabra) for palabra in palabras)
    
    # Imprimir la fila superior del marco
    print("*" * (max_longitud + 4))  # +4 por los márgenes (espacios a los lados)
    
    # Imprimir cada palabra dentro del marco
    for palabra in palabras:
        # Imprimimos la palabra con asteriscos a los lados y espacios de relleno
        print("* " + palabra.ljust(max_longitud) + " *")
    
    # Imprimir la fila inferior del marco
    print("*" * (max_longitud + 4))  # +4 por los márgenes

# Ejemplo de uso
texto = input("Introduce un texto: ")
mostrar_con_marcado(texto)

