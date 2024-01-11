import os

MenuGeneros = ['1. Crear Genero','2.Listar Generos','3.Ir a Menu Principal']
MenuActores = ['1. Crear Actor','2. ListarActor','3.Ir a Menu Principal']
MenuFormatos = ['1. AgregarPelicula','2. EditarPelicula','3. EliminarPelicula','4. EliminarActor','5.BuscarPelicula','6. Listar todas las peliculas','7. Menu principal']
Informes = ['1. Listar las peliculas de un genero especifico','2. Listar las peliculas donde el protagonista sea Silvester Stallone','3. Buscar pelicula y mostrar la sipnosis y los actores']
MenuPeliculas = []
isActive = True 

def Administradorgeneros():
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
                print("Hasta pronto...")
                os.system('pause')
                isActive = False

def AdministadorActores():
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
                print("Hasta pronto...")
                os.system('pause')
                isActive = False

def AdministradorFormatos():
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
                print("Hasta pronto...")
                os.system('pause')
                isActive = False

def GestorPeliculas():
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
                pass
            elif(opc == 2):
                pass
            elif(opc == 3):
                pass
            elif(opc == 4):
                print("Hasta pronto...")
                os.system('pause')
                isActive = False

def GestorInformes():
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
                print("Hasta pronto...")
                os.system('pause')
                isActive = False
