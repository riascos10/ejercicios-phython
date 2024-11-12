def convertir_a_milisegundos(dias, horas, minutos, segundos):
    # Convertir los días, horas, minutos y segundos a milisegundos
    milisegundos = (dias * 24 * 60 * 60 * 1000) + (horas * 60 * 60 * 1000) + (minutos * 60 * 1000) + (segundos * 1000)
    return milisegundos

# Ejemplo de uso
dias = 1
horas = 2
minutos = 30
segundos = 45

resultado = convertir_a_milisegundos(dias, horas, minutos, segundos)
print(f"{dias} días, {horas} horas, {minutos} minutos, {segundos} segundos equivalen a {resultado} milisegundos.")
