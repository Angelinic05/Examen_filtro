import os
import funciones.corefile as cf

peliculas = {}

def validarArchivo():
    if(cf.checkfile()):
        print('ok')
        os.system('pause')
    else:
        cf.newfile(peliculas)

def newpelicula (customer) -> dict:
    peliculas.update(customer)
    cf.addData(customer["id"],peliculas)

def DelPelicula():
    id = input("Ingrese la id de la pelicula a eliminar: ")
    cf.eliminar(id,peliculas)


