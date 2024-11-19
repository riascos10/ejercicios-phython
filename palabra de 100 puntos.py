# Diccionario con el valor de cada letra
abecedario = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
    'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
    'n': 14, 'ñ': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19,
    's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24, 'x': 25,
    'y': 26, 'z': 27
}

print("Bienvenido al programa 'La palabra de 100 puntos'")
print("Introduce palabras para calcular su puntaje. Escribe una palabra que sume exactamente 100 puntos para finalizar.\n")

while True:
    # Solicitar palabra al usuario
    palabra = input("Introduce una palabra: ").lower()
    
    # Calcular el puntaje de la palabra
    puntaje = 0
    for letra in palabra:
        if letra in abecedario:
            puntaje += abecedario[letra]
        else:
            print(f"Caracter inválido encontrado: '{letra}'. Se omitirá en el cálculo.")
    
    # Mostrar el puntaje de la palabra
    print(f"Puntaje de '{palabra}': {puntaje}")
    
    # Verificar si el puntaje es 100
    if puntaje == 100:
        print("¡Felicidades! Has ingresado una palabra de 100 puntos.")