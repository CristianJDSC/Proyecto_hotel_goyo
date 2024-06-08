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

def main():
    matriz_habitaciones=[   [102,Categoria.DOBLE.value,"07/05/2024","12/05/2024",Estado.OCUPADO.value,"Victor","Pedrerol","30678939"],
                            [403,Categoria.PRESIDENCIAL.value,"","",Estado.LIBRE.value,"","",""],
                            [203,Categoria.SENCILLA.value,"23/03/2024","30/03/2024",Estado.OCUPADO.value,"Maria","Fernandez","25103737"],
                            [103,Categoria.SENCILLA.value,"11/04/2024","16/04/2024",Estado.RESERVADO.value,"Eduardo","Berbesi","29008834"],
                            [301,Categoria.DOBLE.value,"29/04/2024","03/05/2024",Estado.RESERVADO.value,"Marco","Rivas","12036531"],
                            [401,Categoria.SUITE.value,"12/12/2023","17/12/2023",Estado.OCUPADO.value,"Fabiana","Gonzalez","31224676"],
                            [201,Categoria.DOBLE.value,"","",Estado.LIBRE.value,"","",""],
                            [402,Categoria.PRESIDENCIAL.value,"18/07/2024","23/07/2024",Estado.RESERVADO.value,"Camila","Lopez","26335445"],
                            [101,Categoria.SENCILLA.value,"","",Estado.LIBRE.value,"","",""],
                            [302,Categoria.SUITE.value,"","",Estado.LIBRE.value,"","",""],
                            [303,Categoria.PRESIDENCIAL.value,"31/05/2024","05/06/2024",Estado.OCUPADO.value,"Javier","Parra","28984213"],
                            [202,Categoria.SUITE.value,"01/06/2024","06/06/2024",Estado.RESERVADO.value,"Carlos","Pineda","27556212"],
        ]
    
    

    with open('d:data_habitaciones.bin', 'wb') as file:
        pickle.dump(matriz_habitaciones, file)
    
main()