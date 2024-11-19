import random

def simular_clima(dias, temp_inicial, prob_lluvia_inicial):
    # Inicializar variables
    temperatura = temp_inicial
    prob_lluvia = prob_lluvia_inicial
    temp_max = temperatura
    temp_min = temperatura
    dias_lluvia = 0
    
    for dia in range(1, dias + 1):
        print(f"Día {dia}:")
        # Verificar si llueve
        if random.random() < prob_lluvia:
            print("¡Está lloviendo!")
            dias_lluvia += 1
            temperatura -= 1  # La temperatura baja si llueve
        else:
            print("No hay lluvia.")
        
        # Mostrar la temperatura del día
        print(f"Temperatura: {temperatura}°C")
        
        # Ajustar la temperatura aleatoriamente (con un 10% de probabilidad de cambiar en ±2°C)
        if random.random() < 0.1:
            cambio_temp = random.choice([-2, 2])
            temperatura += cambio_temp
            print(f"¡La temperatura ha cambiado en {cambio_temp}°C!")
        
        # Actualizar la temperatura máxima y mínima
        temp_max = max(temp_max, temperatura)
        temp_min = min(temp_min, temperatura)
        
        # Ajustar la probabilidad de lluvia según la temperatura
        if temperatura > 25:
            prob_lluvia += 0.2
            print(f"Probabilidad de lluvia aumentó a {prob_lluvia*100:.1f}% debido a la alta temperatura.")
        elif temperatura < 5:
            prob_lluvia -= 0.2
            print(f"Probabilidad de lluvia disminuyó a {prob_lluvia*100:.1f}% debido a la baja temperatura.")
        
        # Limitar la probabilidad de lluvia entre 0 y 1
        prob_lluvia = max(0, min(prob_lluvia, 1))
        
        print('-' * 30)
    
    # Resultado final
    print(f"\nResumen de la predicción de clima:")
    print(f"Temperatura máxima: {temp_max}°C")
    print(f"Temperatura mínima: {temp_min}°C")
    print(f"Cantidad de días con lluvia: {dias_lluvia} de {dias} días.")
    

# Ejemplo de uso:
dias_prediccion = int(input("Ingrese el número de días de la predicción: "))
temp_inicial = float(input("Ingrese la temperatura inicial en grados Celsius: "))
prob_lluvia_inicial = float(input("Ingrese la probabilidad inicial de lluvia (0 a 1): "))

simular_clima(dias_prediccion, temp_inicial, prob_lluvia_inicial)