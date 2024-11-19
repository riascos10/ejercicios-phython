def encontrar_diferencias(cadena1, cadena2):
    """
    Compara dos cadenas de texto de igual longitud y encuentra los caracteres diferentes entre ellas.
    
    Args:
    cadena1 (str): La primera cadena de texto.
    cadena2 (str): La segunda cadena de texto.

    Returns:
    list: Lista con los caracteres que difieren entre las dos cadenas.
    """
    # Comprobar que las cadenas tengan la misma longitud
    if len(cadena1) != len(cadena2):
        raise ValueError("Las cadenas deben tener la misma longitud.")

    # Lista para almacenar las diferencias
    diferencias = []

    # Comparar las cadenas carácter por carácter
    for i in range(len(cadena1)):
        if cadena1[i] != cadena2[i]:  # Si los caracteres no coinciden
            diferencias.append(cadena1[i])  # Añadir el carácter de la primera cadena

    return diferencias

# Ejemplo de uso
def main():
    """
    Función principal para probar la función encontrar_diferencias.
    """
    # Ejemplo 1
    cadena1 = "Me llamo mouredev"
    cadena2 = "Me 1lemo mouredov"
    diferencias = encontrar_diferencias(cadena1, cadena2)
    print(f"Diferencias entre las cadenas:\n{diferencias}\n")
    # Salida esperada: ["e", "o"]

    # Ejemplo 2
    cadena1 = "Me llamo Brais Moure"
    cadena2 = "Me llamo brais moure"
    diferencias = encontrar_diferencias(cadena1, cadena2)
    print(f"Diferencias entre las cadenas:\n{diferencias}\n")
    # Salida esperada: [" ", "b", "m"]

# Llamada a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()