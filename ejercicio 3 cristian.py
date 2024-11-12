def comparar_cadenas(str1, str2):
    
    out1 = ""
    out2 = ""
    
   
    for char in str1:
        if char not in str2:
            out1 += char  # Si no está en str2, lo agregamos a out1
    
    # Recorremos todos los caracteres de str2 y comprobamos si están en str1
    for char in str2:
        if char not in str1:
            out2 += char  # Si no está en str1, lo agregamos a out2
    
   
    print("Out1 (caracteres en str1 pero no en str2):", out1)
    print("Out2 (caracteres en str2 pero no en str1):", out2)

# Ejemplo de uso
str1 = "abcdef"
str2 = "acdfgh"
comparar_cadenas(str1, str2)
