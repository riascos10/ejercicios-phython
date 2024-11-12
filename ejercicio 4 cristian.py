def es_numero_armstrong(numero):
 
    num_str = str(numero)
    num_digitos = len(num_str)
    
    
    suma = sum(int(digito) ** num_digitos for digito in num_str)
    
   
    if suma == numero:
        print(f"{numero} es un número de Armstrong.")
    else:
        print(f"{numero} no es un número de Armstrong.")

# Ejemplo de uso
es_numero_armstrong(153)
es_numero_armstrong(9474)
es_numero_armstrong(123)
