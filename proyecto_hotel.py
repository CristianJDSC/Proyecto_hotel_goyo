from time import sleep
import pickle
from enum import Enum

class Categoria(Enum):
    SENCILLA = "Sencilla"
    DOBLE = "Doble"
    SUITE = "Suite"
    PRESIDENCIAL = "Presidencial"


class Estado(Enum):
    OCUPADO = "Ocupado"
    LIBRE = "Libre"
    RESERVADO = "Reservado"

        
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
        print("8.-", "Actualizar los datos de una habitación:")
        print("9.-", "")
        print()
        opcion=str(input("Ingrese la opción que desee ejecutar: ")); print()
        
        #OPCIÓN 1
        if opcion=="1":
            
            print("Habitaciones:")
            print()
            
            for i in range(len(matriz_habitaciones)):
                print(f"Numero: {matriz_habitaciones[i][0]}")
                print(f"Categoria: {matriz_habitaciones[i][1]}")
                if matriz_habitaciones[i][4]!=Estado.LIBRE.value:
                    print(f"Fecha de entrada: {matriz_habitaciones[i][2]}")
                    print(f"Fecha de salida: {matriz_habitaciones[i][3]}")
                print(f"Estado: {matriz_habitaciones[i][4]}")
                print()
    
main()