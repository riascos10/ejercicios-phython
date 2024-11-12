def obtener_parametros(url):
    # Primero, verificamos si la URL tiene parámetros (es decir, si contiene un '?')
    if '?' not in url:
        return {}

    # Obtenemos la parte de los parámetros (todo después del '?')
    parte_parametros = url.split('?')[1]

    # Separamos los diferentes parámetros por el símbolo '&'
    parametros = parte_parametros.split('&')

    # Creamos un diccionario para almacenar los parámetros y sus valores
    resultado = {}

    # Recorremos todos los parámetros obtenidos
    for param in parametros:
        # Separamos cada parámetro en clave y valor por el símbolo '='
        if '=' in param:
            clave, valor = param.split('=', 1)
            resultado[clave] = valor

    return resultado

# Ejemplo de uso
url = "https://example.com/page?nombre=Juan&edad=30&ciudad=Madrid"
parametros = obtener_parametros(url)
print(parametros)