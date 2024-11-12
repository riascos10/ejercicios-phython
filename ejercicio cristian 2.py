def invertir_cadena(cadena):
    # Variable para almacenar la cadena invertida
    cadena_invertida = ""
    
    # Recorremos la cadena de atrás hacia adelante
    for i in range(len(cadena) - 1, -1, -1):
        # Añadimos el carácter actual al principio de la cadena invertida
        cadena_invertida += cadena[i]
    
    return cadena_invertida

# Ejemplo de uso
texto = "Hola Mundo"
resultado = invertir_cadena(texto)
print(f"Texto original: {texto}")
print(f"Texto invertido: {resultado}")
