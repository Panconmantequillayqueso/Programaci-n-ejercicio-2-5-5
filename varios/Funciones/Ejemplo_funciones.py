# Funciones 
import Funciones as fn
# Para evitar tanta repetición usamos funciones


# Las funciones pueden ser con o sin parametros, con o sin retorno

#Linea principal

fn.sumarDosNumeros()

num1=int(input("numero 1: "))
num2=int(input("NUmero 2:"))

res = fn.sumar(num1,num2)
print(res)
