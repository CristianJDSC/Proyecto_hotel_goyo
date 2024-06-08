from time import sleep
import pickle
from enum import Enum
from time import sleep

class Categoria(Enum):
    SENCILLA = "Sencilla"
    DOBLE = "Doble"
    SUITE = "Suite"
    PRESIDENCIAL = "Presidencial"


class Estado(Enum):
    OCUPADO = "Ocupado"
    LIBRE = "Libre"
    RESERVADO = "Reservado"


def Mostrar_Habitaciones(habitaciones):
    for i in range(len(habitaciones)):
        print(f"Numero: {habitaciones[i][0]}")
        print(f"Categoria: {habitaciones[i][1]}")
        print(f"Estado: {habitaciones[i][4]}")
                
        if habitaciones[i][4]!=Estado.LIBRE.value:
            print(f"Fecha de entrada: {habitaciones[i][2]}")
            print(f"Fecha de salida: {habitaciones[i][3]}")
        print()

#Buscar habitaciones por numero o categoria
def Busqueda_Habitacion(habitaciones, objetivo, tipo):      #El tipo viene siendo lo que se quiere buscar (numero o categoria)
    found=False
    for i in range(len(habitaciones)):
        if objetivo==habitaciones[i][tipo]:
            if found==False:
                print("Las habitaciones encontradas son:"); print()
            print(f"Numero: {habitaciones[i][0]}")
            print(f"Categoria: {habitaciones[i][1]}")
            print(f"Estado: {habitaciones[i][4]}")
                        
            if habitaciones[i][4]!=Estado.LIBRE.value:
                print(f"Fecha de entrada: {habitaciones[i][2]}")
                print(f"Fecha de salida: {habitaciones[i][3]}")
            print()
            found=True
            
    if found==False:
        print("La habitacion introducida no se encuentra registrada"); print()
    
    
def Ordenamiento(habitaciones, tipo):
    for i in range(len(habitaciones)):
        key = habitaciones[i]
        k = i - 1
        while k >= 0 and habitaciones[k][tipo] > key[tipo]:
            habitaciones[k + 1] = habitaciones[k]

            k -= 1

        habitaciones[k + 1] = key

    return habitaciones

        
    '''matriz_habitaciones=[[101,Categoria.SENCILLA.value,"","",Estado.LIBRE.value,"","",""],
                            [102,Categoria.DOBLE.value,"07/05/2024","12/05/2024",Estado.OCUPADO.value,"Victor","Pedrerol","30678939"],
                            [103,Categoria.SENCILLA.value,"11/04/2024","16/04/2024",Estado.RESERVADO.value,"Eduardo","Berbesi","29008834"],
                            [201,Categoria.DOBLE.value,"","",Estado.LIBRE.value,"","",""],
                            [202,Categoria.SUITE.value,"01/06/2024","06/06/2024",Estado.RESERVADO.value,"Carlos","Pineda","27556212"],
                            [203,Categoria.SENCILLA.value,"23/03/2024","30/03/2024",Estado.OCUPADO.value,"Maria","Fernandez","25103737"],
                            [301,Categoria.DOBLE.value,"29/04/2024","03/05/2024",Estado.RESERVADO.value,"Marco","Rivas","12036531"],
                            [302,Categoria.SUITE.value,"","",Estado.LIBRE.value,"","",""],
                            [303,Categoria.PRESIDENCIAL.value,"31/05/2024","05/06/2024",Estado.OCUPADO.value,"Javier","Parra","28984213"],
                            [401,Categoria.SUITE.value,"12/12/2023","17/12/2023",Estado.OCUPADO.value,"Fabiana","Gonzalez","31224676"],
                            [402,Categoria.PRESIDENCIAL.value,"18/07/2024","23/07/2024",Estado.RESERVADO.value,"Camila","Lopez","26335445"],
                            [403,Categoria.PRESIDENCIAL.value,"","",Estado.LIBRE.value,"","",""],
        ]'''

def main():
    
    #Cargar archivo con la informacion de las habitaciones
    with open('d:data_habitaciones.bin', 'rb') as file:
        matriz_habitaciones = pickle.load(file)
    print(matriz_habitaciones)
    
    
    
    repeticion_menu=True
    while repeticion_menu:
        #Opciones del Menú
        print()
        print("MENÚ PRINCIPAL")
        print("1.-", "Revisar la disponibilidad de habitaciones del hotel")
        print("2.-", "Buscar una habitación")
        print("3.-", "Listado de habitaciones")
        print("4.-", "Ingresar usuario al hotel")
        print("5.-", "Egresar usuario del hotel")
        print("6.-", "Reservar habitacion")
        print("7.-", "Cancelar reserva de habitacion")
        print("8.-", "Actualizar los datos de una habitación")
        print("9.-", "")
        print()
        opcion=str(input("Ingrese la opción que desee ejecutar: ")); print()
        
        #OPCIÓN 1
        if opcion=="1":
            print("Las habitaciones son:"); print()
            Mostrar_Habitaciones(matriz_habitaciones)
        
        #OPCION 2
        elif opcion=="2":
            #Opciones de busqueda
            while repeticion_menu:
                print("MENÚ BUSQUEDA")
                print("1.-", "Buscar por numero de habitacion")
                print("2.-", "Buscar por categoria de habitacion")
                print("0.-", "Regresar")
                print()
                opcion=str(input("Ingrese la opción que desee ejecutar: ")); print()
                
                if opcion=="1":
                    while repeticion_menu:
                        try:
                            objetivo=int(input("Ingrese el numero de la habitacion: ")); print()
                            Busqueda_Habitacion(matriz_habitaciones,objetivo,0)
                            break
                        except Exception as E:
                            print("ERROR: Debe introducir un numero entero"); print()
                elif opcion=="2":
                    objetivo=str(input("Ingrese la categoria de la habitacion (Sencilla, Doble, Suite, Presidencial): ")); print()
                    Busqueda_Habitacion(matriz_habitaciones,objetivo.capitalize(),1)
                elif opcion=="0":
                    break
                else:
                    print("Opcion invalida. Intentelo de nuevo"); print()
                    sleep(3)

        #OPCION 3
        elif opcion=="3":
            #Opciones de ordenamiento
            while repeticion_menu:
                print("MENÚ LISTADO")
                print("1.-", "Mostrar por numero de habitacion de menor a mayor")
                print("2.-", "Mostar por categoria de habitacion")
                print("0.-", "Regresar")
                print()
                opcion=str(input("Ingrese la opción que desee ejecutar: ")); print()
                
                if opcion=="1":
                    print("Las habitaciones son:"); print()
                    matriz_ordenada=Ordenamiento(matriz_habitaciones,0)
                    Mostrar_Habitaciones(matriz_ordenada)
                elif opcion=="2":
                    print("Las habitaciones son:"); print()
                    matriz_ordenada=Ordenamiento(matriz_habitaciones,1)
                    Mostrar_Habitaciones(matriz_ordenada)
                elif opcion=="0":
                    break
                else:
                    print("Opcion invalida. Intentelo de nuevo"); print()
                    sleep(3)
    
main()
