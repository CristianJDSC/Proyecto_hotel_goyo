from time import sleep
import pickle
from enum import Enum
import re
from time import sleep

class Categoria(Enum):
    SENCILLA = "Sencilla"
    DOBLE = "Doble"
    SUITE = "Suite"
    PRESIDENCIAL = "Presidencial"


class Estado(Enum):
    OCUPADO = "Ocupada"
    LIBRE = "Libre"
    RESERVADO = "Reservada"

def ValidarEnteros(frase):
    while True:
        valor=input(frase); 
        if valor.isdigit():
            return int(valor)
        else:
            print()
            print("ERROR: Debe introducir un numero entero"); print()

def validarDatos(frase, patron):
    while True:
        dato=input(frase)
        if re.match(patron, dato) is not None:
            return dato
        else:
            print()
            print("ERROR: Debe introducir el dato solicitado de forma correcta"); print()

def Mostrar_Habitaciones(habitaciones,usuario):
    for i in range(len(habitaciones)):
        print(f"- Numero: {habitaciones[i][0]}")
        print(f"  Categoria: {habitaciones[i][1]}")
        print(f"  Estado: {habitaciones[i][4]}")
                
        if habitaciones[i][4]!=Estado.LIBRE.value:
            print(f"  Fecha de entrada: {habitaciones[i][2]}")
            print(f"  Fecha de salida: {habitaciones[i][3]}")
        if usuario:
            print(f"  Nombre del usuario: {habitaciones[i][5]}")
            print(f"  Apellido del usuario: {habitaciones[i][6]}")
            print(f"  CI del usuario: {habitaciones[i][7]}")
        print()

#Buscar habitaciones por numero o categoria
def Busqueda_Habitacion(habitaciones, objetivo, tipo):      #El tipo viene siendo lo que se quiere buscar (numero o categoria)
    found=False
    for i in range(len(habitaciones)):
        if objetivo==habitaciones[i][tipo]:
            if found==False:
                print("Las habitaciones encontradas son:"); print()
            print(f"- Numero: {habitaciones[i][0]}")
            print(f"  Categoria: {habitaciones[i][1]}")
            print(f"  Estado: {habitaciones[i][4]}")
                        
            if habitaciones[i][4]!=Estado.LIBRE.value:
                print(f"  Fecha de entrada: {habitaciones[i][2]}")
                print(f"  Fecha de salida: {habitaciones[i][3]}")
            print()
            found=True
            
    if found==False:
        print()
        print("La habitacion introducida no se encuentra registrada"); print()
    else:
        sleep(3)
    
    
def Ordenamiento(habitaciones, tipo):
    for i in range(len(habitaciones)):
        key = habitaciones[i]
        k = i - 1
        while k >= 0 and habitaciones[k][tipo] > key[tipo]:
            habitaciones[k + 1] = habitaciones[k]
            k -= 1
        habitaciones[k + 1] = key
    return habitaciones

def Mostrar_Habitaciones_Disponibles(habitaciones):
    found=False
    print("Categorías de habitaciones disponibles:")
    for categoria in Categoria:
        for i in range(len(habitaciones)):
            if categoria.value==habitaciones[i][1] and habitaciones[i][4]==Estado.LIBRE.value:
                print(f"- {categoria.value}")
                found=True
                break
    if found==False:
        print()
        print("No hay habitaciones disponibles")
        sleep(3)
        return found
    else:
        print()
        return found
    

def Ingresar_Usuario(matriz_habitaciones,estado):
    categoria_elegida = input("Ingrese la categoría de habitación que desea: ").capitalize(); print()
    habitaciones_disponibles_num = []
    for i in range(len(matriz_habitaciones)):
        if matriz_habitaciones[i][1] == categoria_elegida and matriz_habitaciones[i][4] == Estado.LIBRE.value:
            habitaciones_disponibles_num.append(matriz_habitaciones[i][0])
    
    if len(habitaciones_disponibles_num) == 0:
        print()
        print("No hay habitaciones disponibles en esa categoría.")
        sleep(3)
        return
    
    print("Habitaciones disponibles:")
    for habitacion in habitaciones_disponibles_num:
        print(f"- {habitacion}")
    print()
    
    while True:
        num_habitacion=ValidarEnteros("Ingrese el número de habitación que desea: "); print()
        if num_habitacion not in habitaciones_disponibles_num:
            print("ERROR: Debe introducir el numero de una de las habitaciones disponibles"); print()
        else:
            for i in range(len(matriz_habitaciones)):
                if matriz_habitaciones[i][0] == num_habitacion:
                    matriz_habitaciones[i][5]= validarDatos("Ingrese su nombre: ",r'^[a-zA-Z]{1,}+$')
                    matriz_habitaciones[i][6]= validarDatos("Ingrese su apellido: ",r'^[a-zA-Z\s]{1,}+$')
                    matriz_habitaciones[i][7]= validarDatos("Ingrese su cédula de identidad: ",r'^[0-9]{8}+$')
                    matriz_habitaciones[i][2]= validarDatos("Ingrese la fecha de entrada (dd/mm/yyyy): ",r'([0-9]{2})/([0-9]{2})/([0-9]{4}+$)')
                    matriz_habitaciones[i][3]= validarDatos("Ingrese la fecha de salida (dd/mm/yyyy): ",r'([0-9]{2})/([0-9]{2})/([0-9]{4}+$)')
                    matriz_habitaciones[i][4]= estado
                    print("Habitación asignada con éxito.")
                    sleep(3)
                    return


def Egresar_Usuario(matriz_habitaciones, estado):
    habitaciones_ocupadas=[]
    habitaciones_ocupadas_num=[]
    for i in range(len(matriz_habitaciones)):
        if matriz_habitaciones[i][4] == estado:
            habitaciones_ocupadas.append(matriz_habitaciones[i])
            habitaciones_ocupadas_num.append(matriz_habitaciones[i][0])
    
    if len(habitaciones_ocupadas) == 0:
        print(f"No hay habitaciones {estado.lower()}s.")
        sleep(3)
        return
    
    print(f"Habitaciones {estado.lower()}s:"); print()
    Mostrar_Habitaciones(habitaciones_ocupadas,True)
    print()
    
    while True:
        if estado==Estado.OCUPADO.value:
            num_habitacion=ValidarEnteros("Ingrese el número de habitación que desea egresar: "); print()
        elif estado==Estado.RESERVADO.value:
            num_habitacion=ValidarEnteros("Ingrese el número de habitación de la que desea cancelar la reservacion: "); print()
        if num_habitacion not in habitaciones_ocupadas_num:
            print(f"ERROR: La habitación no existe o no se encuentra {estado.lower()}."); print()
        else:
            for i in range(len(matriz_habitaciones)):
                if matriz_habitaciones[i][0] == num_habitacion:
                    if matriz_habitaciones[i][4] == estado:
                        matriz_habitaciones[i][2] = ""
                        matriz_habitaciones[i][3] = ""
                        matriz_habitaciones[i][4] = Estado.LIBRE.value
                        matriz_habitaciones[i][5] = ""
                        matriz_habitaciones[i][6] = ""
                        matriz_habitaciones[i][7] = ""
                        print("Habitación liberada con éxito.");
                        sleep(3)
                        return
                    
def Actualizar_Categoria(habitaciones):
    print("Categorías disponibles de habitaciones:")
    for categoria in Categoria:
        for i in range(len(habitaciones)):
            if categoria.value==habitaciones[i][1]:
                print(f"- {categoria.value}")
                break
    
    habitaciones_modificables_num=[]
    categoria_elegida = input("Ingrese el tipo de categoria que desea modificar: ").capitalize(); print()
    for i in range(len(habitaciones)):
        if habitaciones[i][1] == categoria_elegida:
            habitaciones_modificables_num.append(habitaciones[i][0])
            
    if len(habitaciones_modificables_num) == 0:
        print()
        print("No hay habitaciones disponibles en esa categoría.")
        sleep(3)
        return
    
    print(f"Habitaciones con la categoria {categoria_elegida}:")
    for habitacion in habitaciones_modificables_num:
        print(f"- {habitacion}")
    print()
    
    while True:
        num_habitacion=ValidarEnteros("Ingrese el número de habitación que desea modificar: "); print()
        if num_habitacion not in habitaciones_modificables_num:
            print("ERROR: Debe introducir el numero de una de las habitaciones disponibles"); print()
        else:
            for i in range(len(habitaciones)):
                if habitaciones[i][0] == num_habitacion:
                    while True:
                        categoria_nueva=(input("Ingrese la categoria de la habitacion (Sencilla, Doble, Suite, Presidencial): ")).capitalize(); print()
                        if categoria_nueva not in Categoria:
                            print("ERROR: Debe introducir una de las categorias disponibles"); print()
                        else:
                            habitaciones[i][1]=categoria_nueva
                            print("La categoria ha sido modificada")
                            sleep(4)
                            return



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
    
    
    while True:
        #Opciones del Menú
        print()
        print("MENÚ PRINCIPAL")
        print("1.-", "Revisar la disponibilidad de habitaciones del hotel")
        print("2.-", "Buscar una habitación")
        print("3.-", "Listado de habitaciones")
        print("4.-", "Ingresar usuario al hotel")
        print("5.-", "Egresar usuario del hotel")
        print("6.-", "Reservas")
        print("7.-", "Modificar la categoria de una habitacion")
        print("0.-", "Salir")
        print()
        opcion=input("Ingrese la opción que desee ejecutar: "); print()
        
        #OPCIÓN 1
        if opcion=="1":
            print("Las habitaciones son:"); print()
            Mostrar_Habitaciones(matriz_habitaciones,False)
            sleep(7)
        
        #OPCION 2
        elif opcion=="2":
            #Opciones de busqueda
            while True:
                print("MENÚ BUSQUEDA")
                print("1.-", "Buscar por numero de habitacion")
                print("2.-", "Buscar por categoria de habitacion")
                print("0.-", "Regresar")
                print()
                opcion=str(input("Ingrese la opción que desee ejecutar: ")); print()
                
                if opcion=="1":
                    objetivo=ValidarEnteros("Ingrese el numero de la habitacion: ")
                    Busqueda_Habitacion(matriz_habitaciones,objetivo,0)
                elif opcion=="2":
                    while True:
                        objetivo=(input("Ingrese la categoria de la habitacion (Sencilla, Doble, Suite, Presidencial): ")).capitalize(); print()
                        if objetivo not in Categoria:
                            print("ERROR: Debe introducir una de las categorias disponibles"); print()
                        else:
                            Busqueda_Habitacion(matriz_habitaciones,objetivo,1)
                            sleep(4)
                            break
                elif opcion=="0":
                    break
                else:
                    print("Opcion invalida. Intentelo de nuevo"); print()
                    sleep(3)

        #OPCION 3
        elif opcion=="3":
            #Opciones de ordenamiento
            while True:
                print("MENÚ LISTADO")
                print("1.-", "Mostrar por numero de habitacion de menor a mayor")
                print("2.-", "Mostrar por categoria de habitacion")
                print("0.-", "Regresar")
                print()
                opcion=str(input("Ingrese la opción que desee ejecutar: ")); print()
                
                if opcion=="1":
                    print("Las habitaciones son:"); print()
                    matriz_ordenada=Ordenamiento(matriz_habitaciones,0)
                    Mostrar_Habitaciones(matriz_ordenada,False)
                    sleep(7)
                elif opcion=="2":
                    print("Las habitaciones son:"); print()
                    matriz_ordenada=Ordenamiento(matriz_habitaciones,1)
                    Mostrar_Habitaciones(matriz_ordenada,False)
                    sleep(7)
                elif opcion=="0":
                    break
                else:
                    print("Opcion invalida. Intentelo de nuevo"); print()
                    sleep(3)

        #OPCIÓN 4
        elif opcion=="4":
            if Mostrar_Habitaciones_Disponibles(matriz_habitaciones):
                Ingresar_Usuario(matriz_habitaciones,Estado.OCUPADO.value)

        #OPCIÓN 5
        elif opcion=="5":
            Egresar_Usuario(matriz_habitaciones,Estado.OCUPADO.value)

        #OPCIÓN 6
        elif opcion=="6":
            while True:
                print()
                print("MENÚ RESERVAS")
                print("1.-", "Asignar Reservacion")
                print("2.-", "Cancelacion de reservacion")
                print("0.-", "Regresar")
                print()
                opcion=str(input("Ingrese la opción que desee ejecutar: ")); print()

                if opcion=="1":
                    if Mostrar_Habitaciones_Disponibles(matriz_habitaciones):
                        Ingresar_Usuario(matriz_habitaciones,Estado.RESERVADO.value)
                elif opcion=="2":
                    Egresar_Usuario(matriz_habitaciones,Estado.RESERVADO.value)
                elif opcion=="0":
                    break
                else:
                    print("Opcion invalida. Intentelo de nuevo"); print()
                    sleep(3)
                    
        #OPCIÓN 7
        elif opcion=="7":
            Actualizar_Categoria(matriz_habitaciones)
            
        #OPCION SALIR
        elif opcion=="0":
            #Guardar los cambios realizados en el archivo
            with open('d:data_habitaciones.bin', 'wb') as file:
                pickle.dump(matriz_habitaciones, file)
            
            print("Ha salido con exito")
            break
        else:
            print("Opcion invalida. Intentelo de nuevo"); print()
            sleep(3)
main()
