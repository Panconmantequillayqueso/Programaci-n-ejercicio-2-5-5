# Funciones
# Para evitar tanta repetición usamos funciones

def sumarDosNumeros(): 
    '''Esta función permite sumar dos números
        ingresados dentro de la función.
        Este mensaje se llama dotstring
    '''
    num1 = int(input("Ingrese número 1: "))
    num2 = int(input("Ingrese número 2: "))

    suma = num1 + num2
    print(f"la suma de {num1} + {num2} es = {suma}")

def sumar (a,b) : 
    '''Esta función permite sumar dos números ingresados por parámetros'''
    suma = a + b 
    return suma

# Las funciones pueden ser con o sin parametros, con o sin retorno

