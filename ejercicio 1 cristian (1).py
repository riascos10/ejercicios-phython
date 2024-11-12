def calcular_area(poli, *args):
    if poli == "triangulo":
       
        base, altura = args
        area = 0.5 * base * altura
        print(f"El área del triángulo con base {base} y altura {altura} es: {area}")
        return area

    elif poli == "cuadrado":
    
        lado = args[0]
        area = lado ** 2
        print(f"El área del cuadrado con lado {lado} es: {area}")
        return area

    elif poli == "rectangulo":
      
        base, altura = args
        area = base * altura
        print(f"El área del rectángulo con base {base} y altura {altura} es: {area}")
        return area

    else:
        print("Polígono no soportado")
        return None

# Ejemplos de uso:
calcular_area("triangulo", 10, 5)
calcular_area("cuadrado", 4)
calcular_area("rectangulo", 8, 6)
