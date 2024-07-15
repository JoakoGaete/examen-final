
import random  
import csv  

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]  
sueldos = []  

def asignar_sueldos_aleatorios():  
    for i in range(10):  
        sueldo = random.randint(300000, 2500000)  
        sueldos.append(sueldo)  

def clasificar_sueldos():  
    sueldos_800k = []  
    sueldos_2m = []  
    sueldos_mayores_2m = []  

    for i in range(10):  
        if sueldos[i] < 800000:  
            sueldos_800k.append((trabajadores[i], sueldos[i]))  
        elif 800000 <= sueldos[i] < 2000000:  
            sueldos_2m.append((trabajadores[i], sueldos[i]))  
        else:  
            sueldos_mayores_2m.append((trabajadores[i], sueldos[i]))  

    print("Sueldos menores a $800.000     TOTAL:", len(sueldos_800k))  
    for nombre, sueldo in sueldos_800k:  
        print(nombre, sueldo)  

    print("\nSueldos entre $800.000 y $2.000.000     TOTAL:", len(sueldos_2m))  
    for nombre, sueldo in sueldos_2m:  
        print(nombre, sueldo)  

    print("\nSueldos mayores a $2.000.000     TOTAL:", len(sueldos_mayores_2m))  
    for nombre, sueldo in sueldos_mayores_2m:  
        print(nombre, sueldo)  

    total_sueldos = sum(sueldos)  
    print("\nTOTAL SUELDOS: $", total_sueldos)  

def ver_estadisticas():  
    print("Sueldo más alto:", max(sueldos))  
    print("Sueldo más bajo:", min(sueldos))  
    print("Promedio de sueldos:", sum(sueldos) / len(sueldos))   

def reporte_sueldos():  
    with open('reporte_sueldos.csv', mode='w', newline='') as file:  
        writer = csv.writer(file)  
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Liquido'])  
        for i in range(10):  
            descuento_salud = sueldos[i] * 0.07  
            descuento_afp = sueldos[i] * 0.12  
            sueldo_liquido = sueldos[i] - descuento_salud - descuento_afp  
            writer.writerow([trabajadores[i], sueldos[i], descuento_salud, descuento_afp, sueldo_liquido])
  

while True:  
    print("\n----------------------------")  
    print("1. Asignar sueldos aleatorios")  
    print("2. Clasificar sueldos")  
    print("3. Ver estadísticas")  
    print("4. Reporte de sueldos")  
    print("5. Salir del programa")
    print("------------------------------") 

    opcion = input("Seleccione una opción: ")  

    if opcion == '1':  
        asignar_sueldos_aleatorios()
        print("Sueldos asignados correctamente ")  
    elif opcion == '2':  
        clasificar_sueldos()  
    elif opcion == '3':  
        ver_estadisticas()  
    elif opcion == '4':  
        reporte_sueldos()  
    elif opcion == '5':  
        print("Saliendo del programa...")
        print("Realizado por Joaquín Gaete")
        print("Rut 21.370.962-3")  
        break  
    else:  
        print("Opción no válida. Por favor, seleccione una opción válida.")