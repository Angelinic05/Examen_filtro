import os
import ui.customerMenu as cus

MenuGeneros = ('1. Crear Genero\n2. Listar Generos\n3. Ir a Menu Principal')
MenuActores = ('1. Crear Actor\n2. ListarActor\n3. Ir a Menu Principal')
MenuFormatos = ('1. AgregarPelicula\n2. EditarPelicula\n3. EliminarPelicula\n4. EliminarActor\n5.BuscarPelicula\n6. Listar todas las peliculas\n7. Menu principal')
Informes = ('1. Listar las peliculas de un genero especifico\n2. Listar las peliculas donde el protagonista sea Silvester Stallone\n3. Buscar pelicula y mostrar la sipnosis y los actores\n 4. Menu principal')
MenuPeliculas = ('1. Agregar pelicula\n2. Editar pelicula\n3. Eliminar pelicula\n4. Eliminar Actor\n5. Buscar pelicula\n6 listar todas peliculas\n7. Menu principal')

def Administradorgeneros():
    isActive = True 
    while(isActive):
        os.system('cls')
        print(MenuGeneros)
        try:
            print("")
            opc = int(input("opción: "))
        except ValueError:
            print("opción no válida...")
        else:
            if(opc == 1):
                pass
            elif(opc == 2):
                pass
            elif(opc == 3):
                os.system('pause')
                isActive = False

def AdministadorActores():
    isActive = True 
    while(isActive):
        os.system('cls')
        print(MenuActores)
        try:
            print("")
            opc = int(input("opción: "))
        except ValueError:
            print("opción no válida...")
        else:
            if(opc == 1):
                pass
            elif(opc == 2):
                pass
            elif(opc == 3):
                os.system('pause')
                isActive = False

def AdministradorFormatos():
    isActive = True 
    while(isActive):
        os.system('cls')
        print(MenuFormatos)
        try:
            print("")
            opc = int(input("opción: "))
        except ValueError:
            print("opción no válida...")
        else:
            if(opc == 1):
                pass
            elif(opc == 2):
                pass
            elif(opc == 3):
                os.system('pause')
                isActive = False

def GestorPeliculas():
    isActive = True 
    while(isActive):
        os.system('cls')
        print(MenuPeliculas)
        try:
            print("")
            opc = int(input("opción: "))
        except ValueError:
            print("opción no válida...")
        else:
            if(opc == 1):
                cus.agregarPelicula
                os.system('pause')
            elif(opc == 2):
                pass
            elif(opc == 3):
                pass
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
