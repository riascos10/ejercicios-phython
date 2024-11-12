def dibujar_figura(figura, tamaño):
    if figura == "cuadrado":
        # Dibuja un cuadrado
        for i in range(tamaño):
            print("*" * tamaño)  # Imprime una línea de tamaño "tamaño"
    
    elif figura == "triangulo":
        # Dibuja un triángulo rectángulo
        for i in range(1, tamaño + 1):
            print("*" * i)  # Imprime i asteriscos en cada línea (1 a n)
    
    else:
        print("Figura no válida. Solo se puede dibujar 'cuadrado' o 'triangulo'.")

# Ejemplo de uso
figura = input("¿Qué figura quieres dibujar? ('cuadrado' o 'triangulo'): ").strip().lower()
tamaño = int(input("Introduce el tamaño del lado: "))

dibujar_figura(figura, tamaño)
