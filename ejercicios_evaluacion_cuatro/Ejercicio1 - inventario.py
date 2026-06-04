productos = {}

def agregar():
    '''Agrega productos a la lista de productos. 
    El formato es producto: stock : precio'''
    
    nombre = input("Introduzca el nombre del producto: ").strip().lower()
    stock = int(input("Ingrese el stock: "))
    precio = int(input("Ingrese el precio: "))

    productos[nombre] = [stock,precio]
    print("Producto agregado.")

def mostrar():
    '''Imprime la lista de productos en el inventario'''

    print("Listado de productos:")
    for nombre in productos:
        print(f"Nombre: {nombre}. Stock: {productos[nombre][0]}. Precio: {productos[nombre][1]}")

def buscar():
    '''Busca el nombre de un producto en el inventario'''

while True:
    print("Menú")
    print("1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Producto más caro")
    print("5. Salir")

    while True:
        
        try:
            op = int(input("Ingrese una opción: "))
            break
        except:
            print("Por favor introduzca un número válido.")

    if op == 1:
        agregar()

    elif op == 2:
        mostrar()

    elif op == 3:
        buscar()
    
    elif op == 4:
        precioalto()

    elif op == 5:
        print("Gracias por usar este software.")
        break
    
    else:
        print("Por favor introduzca una opción válida (1-5).")