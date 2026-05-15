usuario1 = None
usuario2 = None
usuario3 = None
contraseña1 = None
contraseña2 = None
contraseña3 = None

while True:
    print("1) Iniciar sesión")
    print("2) Registrar usuario")
    print("3) Salir")

    opcion = int(input("Seleccione una opción (1-3): "))

    if opcion == 1:
        if usuario1 == None and usuario2 == None and usuario3 == None:
            print("¡Debe registrar un usuario!")
        else:

            ingresoUsuario = input("Ingrese su usuario: ")
            ingresoContraseña = input("Ingrese la contraseña: ")

            if ingresoUsuario == usuario1 and ingresoContraseña == contraseña1:
                print(f"Bienvenido, {usuario1}")
            elif ingresoUsuario == usuario2 and ingresoContraseña == contraseña2:
                    print(f"Bienvenido, {usuario2}")
            elif ingresoUsuario == usuario3 and ingresoContraseña == contraseña3:
                    print(f"Bienvenido, {usuario3}")
            else:
                print("Error, usuario o contraseña inválidos")
                break



            while True:
                print("1) Realizar llamada")
                print("2) Enviar correo electrónico")
                print("3) Cerrar sesión")

                opcion1 = int(input("Seleccione una opción (1-3): "))

                if opcion1 == 1:
                    celular = input("Ingrese un número de celular: ")

                elif opcion1 == 2:
                    email = input("Ingrese un correo electrónico: ")
                
                    mensaje = input("Ingrese el mensaje: ")

                elif opcion1 == 3:
                    print("Cerrando sesión...")
                    break

                else:
                    print("¡Ingrese una opción válida!")
                




    elif opcion == 2: #Registro de usuarios

        while True:    
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

            #Si todos los usuarios están registrados
            
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