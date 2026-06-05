alumnos = {
    
}

def agregar_alumnos():
    '''Agrega alumnos al diccionario alumnos'''
    while True:
        nombre = input("Ingrese el nombre del alumno: ")
        if len(nombre) == 0 or nombre == "":
            print("El nombre no puede estar vacio")
        else:
            break
    
    while True:
        try:
            cantidadNotas = int(input("Ingrese la cantidad de notas del alumno: "))
        except:
            print("Ingrese un número entero diferente a cero.")

        if cantidadNotas <= 0:
            print("Cantidad inválida. Por favor ingrese al menos una nota.")
        else:
            break

    


while True:
    print("Menú")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Ver promedios")
    print("4. Mejor alumno")
    print("5. Cantidad de aprobados")
    print("6. Salir")

    while True:
        try: 
            op = int(input("Ingrese una opción: "))
            break
        except:
            print("Ingrese un número válido.")

    if op == 1:
        agregar_alumnos()
    elif op == 2:
        mostrar_alumnos()
    elif op == 3:
        ver_promedios()
    elif op == 4:
        mejor_alumno()
    elif op == 5:
        cantidad_aprobados()
    elif op == 6:
        print("Gracias por usar este software.")
        break
    else:
        print("Ingrese un número del 1 al 6.")
