camarotes_disponibles = 120
capacidad_maxima = 90
historial_reservas = 0

menu = True
print("¡Bienvenido al sistema de gestión de camarotes del Crucero Atlántico!")

while menu:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1.- Camarotes disponibles.")
    print("2.- Reservar camarote.")
    print("3.- Cancelar camarote.")
    print("4.- Historial de reservas.")
    print("5.- Salir.")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        print("Camarotes disponibles:", camarotes_disponibles)
        
    elif opcion == "2":
        try:
            reservar = int(input("Ingresa la cantidad de camarotes a reservar: "))
            if reservar <= 0:
                print("Error: La cantidad debe ser mayor a 0.")
            elif reservar > camarotes_disponibles:
                print("Error: No hay suficiente capacidad disponible.")
            else:
                camarotes_disponibles = camarotes_disponibles - reservar
                historial_reservas = historial_reservas + reservar
                print("Reserva realizada con éxito.")
        except:
            print("Ha ocurrido un error, debes ingresar un número entero.")
            
    elif opcion == "3":
        try:
            cancelar = int(input("Ingresa la cantidad de camarotes a cancelar: "))
            if cancelar <= 0:
                print("Error: La cantidad a cancelar debe ser mayor a 0.")
            elif (camarotes_disponibles + cancelar) > capacidad_maxima:
                print("Error: No puede superar la capacidad máxima del crucero (90 camarotes).")
            else:
                camarotes_disponibles = camarotes_disponibles + cancelar
                historial_reservas = historial_reservas - cancelar
                print("Cancelación realizada con éxito.")
        except:
            print("Ha ocurrido un error, debes ingresar un número entero.")
            
    elif opcion == "4":
        print("Historial de reservas (total acumulado en sesión):", historial_reservas)
        
    elif opcion == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break
        
    else:
        print("Opción no válida. Intenta nuevamente.")


