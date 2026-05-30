usuario1 = None
usuario2 = None
usuario3 = None
contraseña1 = None
contraseña2 = None
contraseña3 = None

while True: #Primer menú
    print("1) Iniciar sesión")
    print("2) Registrar usuario")
    print("3) Salir")

    while True: #Este corrobora que usen un int en la respuesta, y se repite si hay un error como poner una cadena
        try:
            opcion = int(input("Seleccione una opción (1-3): "))
            break
        except ValueError:
            print("Por favor ingrese un número del 1 al 3")

    if opcion == 1: # Iniciar sesión
        
        if usuario1 == None and usuario2 == None and usuario3 == None: #Corrobora que haya un usuario registrado
            print("¡Debe registrar un usuario!")
        else:
            ingresoUsuario = input("Ingrese su usuario: ")
            ingresoContraseña = input("Ingrese la contraseña: ")

            if ingresoUsuario == usuario1 and ingresoContraseña == contraseña1:
                print(f"Bienvenido, {usuario1}")
                ingresoCorrecto = True
            elif ingresoUsuario == usuario2 and ingresoContraseña == contraseña2:
                print(f"Bienvenido, {usuario2}")
                ingresoCorrecto = True
            elif ingresoUsuario == usuario3 and ingresoContraseña == contraseña3:
                print(f"Bienvenido, {usuario3}")
                ingresoCorrecto = True
            else:
                print("¡Usuario o contraseña incorrectos!")
                ingresoCorrecto = False
                
            while ingresoCorrecto == True: #Submenú de la opción 1
                print("1) Realizar llamada")
                print("2) Enviar correo electrónico")
                print("3) Cerrar sesión")

                while True:
                    try:
                        opcion1 = int(input("Seleccione una opción (1-3): "))
                        break
                    except ValueError:
                        print("Por favor ingrese un número del 1 al 3")

                if opcion1 == 1:
                    
                    while True:
                        
                        try:
                            celular = input("Ingrese un número de celular: ")
                        except ValueError:
                            print("Por favor introduzca un número válido.")
                    
                        if len(celular) == 9 and celular.startswith("9"): #Valida que el teléfono tenga 9 dígitos y comience con un 9
                            print("Número guardado")
                            break
                        else:
                            print("Por favor introduzca un número válido")

                elif opcion1 == 2:
                    mensaje = None
                    while mensaje == None:
                        email = input("Ingrese un correo electrónico: ")

                        for arroba in email: #Valida que haya un @ usando for
                            if arroba == "@":
                                print("Dirección de correo válida")
                                mensaje = input("Introduzca el mensaje: ")
                                print("Mensaje enviado")
                    
                        if mensaje == None:
                            print("Correo incorrecto, introduzca un formato de correo electrónico válido (debe incluir un @)")

                elif opcion1 == 3:
                    print("Cerrando sesión...")
                    break

                else:
                    print("¡Ingrese una opción válida!")
                
    elif opcion == 2: #Registro de usuarios

        while True: #Revisa que los usuarios estén registrados
            if usuario1 == None:
                usuario1 = input("Ingrese su nuevo nombre de usuario: ")
                contraseña1 = input("Ingrese su nueva contraseña: ")
                print("¡Usuario registrado!")
                break
            
            elif usuario2 == None:
                usuario2 = input("Ingrese su nuevo nombre de usuario: ")
                contraseña2 = input("Ingrese su nueva contraseña: ")
                print("¡Usuario registrado!")
                break
            
            elif usuario3 == None:
                usuario3 = input("Ingrese su nuevo nombre de usuario: ")
                contraseña3 = input("Ingrese su nueva contraseña: ")
                print("¡Usuario registrado!")
                break
            
            else:
                print("Todos los usuarios están registrados.")
                print("Seleccione un usuario a borrar (1-3)")
                print("Para retroceder seleccione 0.")

                borrarUsuario = int(input("Seleccione una opción válida (0-3): "))

                if borrarUsuario == 0:
                    break
                
                elif borrarUsuario == 1:
                    usuario1 = None
                    contraseña1 = None
                    print("¡Usuario 1 borrado!")

                elif borrarUsuario == 2:
                    usuario2 = None
                    contraseña2 = None
                    print("¡Usuario 2 borrado!")

                elif borrarUsuario == 3:
                    usuario3 = None
                    contraseña3 = None
                    print("¡Usuario 3s borrado!")

                else:
                    print("¡Seleccione una opción válida!")

    elif opcion == 3:
        print("Cerrando sesión...")
        break
    
    else:
        print("¡Ingrese una opcion válida!")