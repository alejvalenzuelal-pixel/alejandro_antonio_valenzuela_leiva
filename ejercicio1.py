chefs_maestros = 0
chefs_aprendiz = 0

cantidad_chefs = 0
while cantidad_chefs <= 0:
    try:
        cantidad_chefs = int(input("¿cuántos chefs desea registrar?:"))
        if cantidad_chefs <= 0:
            print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")
    except:
        print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")
        cantidad_chefs = 0
contador = 0
while contador < cantidad_chefs:
    print(" Registro final del Chef", contador + 1,)

    codigo_valido = False
    while codigo_valido == False:
        codigo = input("Ingresa el Código Culinario: ")
        if len(codigo) >= 6 and len(codigo) == len(codigo.replace(" ", "")):
            codigo_valido = True
        else:
            print("Código inválido. Debe tener al menos 6 caracteres y no incluir espacios.")
    experiencia = 0
    while experiencia <= 0:
        try:
            experiencia = int(input("Ingresa los años de experiencia culinaria: "))
            if experiencia <= 0:
                print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
        except:
            print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
            experiencia = 0
                        
    if experiencia > 8:
        chefs_maestros = chefs_maestros + 1
    else:
         chefs_aprendiz = chefs_aprendiz + 1
        
    contador = contador + 1
print(f"¡La escuela cuenta con {chefs_maestros} Chefs Maestros y {chefs_aprendiz} Chefs Aprendices! ¡A cocinar!")


              
"""Ejercicio 1 (40 puntos)
Desarrolla un programa en Python que administre los registros de chefs recién incorporados a la Escuela Internacional de Gastronomía. El programa debe validar correctamente todos los datos ingresados. Por ejemplo, si se solicita la experiencia culinaria del chef, el usuario solo debe poder ingresar números enteros positivos.

Requisitos del Sistema

1. Clasificación y Funcionalidades Principales
El sistema deberá:
•	Clasificar a los chefs según su experiencia culinaria.
•	Contabilizar cuántos son Chefs Maestros y cuántos Chefs Aprendices.
•	Mostrar un resumen de registro al finalizar.

2. Cantidad de Chefs
El programa debe pedir al usuario cuántos chefs desea registrar.
•	Este valor debe ser un número entero positivo.
•	Si el usuario ingresa un valor inválido, se debe mostrar el siguiente mensaje hasta re-cibir una entrada correcta:
“¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.”

3. Registro por Chef
Código Culinario:
•	Debe tener al menos 6 caracteres.
•	No debe incluir espacios.
•	Ejemplos válidos: CHEFMAS7, GASTRO01, COOKPRO3.




Experiencia Culinaria:
•	El usuario debe ingresar la experiencia culinaria del chef (entero positivo).
•	Si se ingresa un valor incorrecto, se mostrará el mensaje:
“¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.”

4. Clasificación del Chef
Dependiendo del nivel ingresado:
•	Si la experiencia es mayor a 8, el chef será un Chef Maestro.
•	Si la experiencia es menor o igual a 8, será un Chef Aprendiz.

5. Contadores Automáticos
El programa debe llevar un conteo durante el registro:
•	Número total de Chefs Maestros.
•	Número total de Chefs Aprendices.

6. Salida Final
Al finalizar el registro, el programa mostrará un resumen con el total de chefs registrados. Por ejemplo:

“¡La escuela cuenta con 5 Chefs Maestros y 3 Chefs Aprendices! ¡A cocinar!”























"""