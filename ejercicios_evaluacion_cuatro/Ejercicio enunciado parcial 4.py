usuarios = {}

ingresar_usr = (

    nombre = input("Ingrese el nombre del usuario: ").strip
    
    while True
        genero = input("Ingrese el género del usuario(F o M): ").lower().strip()
        if genero == "f" or genero == "m":
            break
        else:
        print(Ingrese una opción válida (F-M))

    while True:
        print("Ingrese la contraseña del nuevo usuario.")
        print("La contraseña debe tener mínimo 8 caracteres, un número, una letra y no puede tener espacios.")
        contraseña = input("Ingrese la nueva contraseña del usuario:")

        for i in contraseña:
            if "a" <= i <= "z":
                tieneletra == True
                break
            else:
                tieneletra == False

         for i in contraseña:
            if "0" <= i <= "9":
                tienenumero == True
                break
            else:
                tienenumero == False
        
        if len(contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres")
        elif "" in contraseña:
            print("No se pueden incluir espacios en la contraseña")
        elif tieneletra == False:
            print("La contraseña debe contener al menos una letra")
        elif tienenumero == False:
            print("La contraseña debe contener al menos un número")
        else:
            break
    
    usuarios[nombre] = [genero,contraseña]
    print("Usuario agregado")


buscar_usr = (
    waldo = input("Ingrese el nombre del usuario a buscar: ")
    usuarios
)

borrar_usr = (

)

salir = (
    print("¡Gracias por usar este software!")
    break
)

#Código principal


while True:
    print("*****Menú*****")
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

    op = int(input("Ingrese una opción: "))

    if op == 1:
        ingresar_usr()
    elif op == 2:
        buscar_usr()
    elif op == 3:
        borrar_usr()
    elif op == 4:
        salir()
    else:
    print("Ingrese una opción válida")