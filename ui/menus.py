import os
import ui.customerPeliculas as cus
import ui.customergeneros as cug
import ui.customeractores as cua
import ui.customerfomatos as cuf
import funciones.peliculas as pe

MenuGeneros = ('1. Crear Genero\n2. Listar Generos\n3. Ir a Menu Principal')
MenuActores = ('1. Crear Actor\n2. Listar Actor\n3. Ir a Menu Principal')
MenuFormatos = ('1. Crear Formatos\n2. Listar Formatos\n3. Ir a Menu Formatos')
Informes = ('1. Listar las peliculas de un genero especifico\n2. Listar las peliculas donde el protagonista sea Silvester Stallone\n3. Buscar pelicula y mostrar la sipnosis y los actores\n 4. Menu principal')
MenuPeliculas = ('1. Agregar pelicula\n2. Editar pelicula\n3. Eliminar pelicula\n4. Eliminar Actor\n5. Buscar pelicula\n6 listar todas peliculas\n7. Menu principal')

def Administradorgeneros():
    isActive = True 
    while(isActive):
        os.system('cls')
        print("")
        print(" GESTOR DE GENEROS ")
        print("-------------------------------------")
        print(MenuGeneros)
        try:
            print("")
            opc = int(input("opción: "))
        except ValueError:
            print("opción no válida...")
            os.system("pause")
        else:
            if(opc == 1):
                pass
                cug.agregarGenero()
            elif(opc == 2):
                cug.listarGenero()
            elif(opc == 3):
                os.system('pause')
                isActive = False

def AdministadorActores():
    isActive = True 
    while(isActive):
        os.system('cls')
        print("")
        print(" GESTOR DE ACTORES ")
        print("-------------------------------------")
        print(MenuActores)
        try:
            print("")
            opc = int(input("opción: "))
        except ValueError:
            print("opción no válida...")
            os.system("pause")
        else:
            if(opc == 1):
                cua.agregarActor()
            elif(opc == 2):
                pass
            elif(opc == 3):
                os.system('pause')
                isActive = False

def AdministradorFormatos():
    isActive = True 
    while(isActive):
        os.system('cls')
        print("")
        print(" GESTOR DE FORMATOS ")
        print("-------------------------------------")
        print(MenuFormatos)
        try:
            print("")
            opc = int(input("opción: "))
        except ValueError:
            print("opción no válida...")
            os.system("pause")
        else:
            if(opc == 1):
                cuf.agregarFormato()
            elif(opc == 2):
                pass
            elif(opc == 3):
                os.system('pause')
                isActive = False

def GestorPeliculas():
    isActive = True 
    while(isActive):
        os.system('cls')
        print("")
        print(" GESTOR DE PELICULAS ")
        print("-------------------------------------")
        print(MenuPeliculas)
        try:
            print("")
            opc = int(input("opción: "))
        except ValueError:
            print("opción no válida...")
            os.system("pause")
        else:
            if(opc == 1):
                cus.agregarPelicula()
                os.system('pause')
            elif(opc == 2):
                pe.searchCustomer()
                os.system('pause')
            elif(opc == 3):
                cus.EliminarPelicula()
                os.system('pause')
            elif(opc == 4):
                pass
            elif(opc == 5):
                pass
            elif(opc == 6):
                pass
            elif(opc == 7):
                os.system('pause')
                isActive = False

def GestorInformes():
    isActive = True 
    while(isActive):
        os.system('cls')
        print(Informes)
        try:
            print("")
            opc = int(input("opción: "))
        except ValueError:
            print("opción no válida...")
            os.system("pause")
        else:
            if(opc == 1):
                pass
            elif(opc == 2):
                pass
            elif(opc == 3):
                pass
            elif(opc == 4):
                os.system('pause')
                isActive = False
