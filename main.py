import os
import ui.menus as menu
import funciones.peliculas as pe
import funciones.corefile as cf
MenuPeliculasBlock = ('1. Administrador de generos\n2. Administador de actores\n3. Administrador de formatos\n4. Gestor de informes\n5. Gestor de peliculas\n6. salir')

isActive = True
if __name__ == '__main__':

    while(isActive):
        os.system('cls')
        print("")
        print(" SISTEMA DE INFORMACION DE PELICULAS ")
        print("-------------------------------------")
        print(MenuPeliculasBlock)
        try:
            print("")
            opc = int(input("opción: "))
        except ValueError:
            print("opción no válida...")
            os.system("pause")
        else:
            if(opc == 1):
                menu.Administradorgeneros() 
            elif(opc == 2):
                menu.AdministadorActores()
            elif(opc == 3):
                menu.AdministradorFormatos()
            elif(opc == 4):
                menu.GestorInformes()
            elif(opc == 5):
                menu.GestorPeliculas()
            elif(opc == 6):
                print("Hasta pronto...")
                os.system('pause')
                isActive = False