import os
import funciones.peliculas as cp
import funciones.corefile as cf
peliculas = {}
def agregarGenero():
    cp.cf.checkfile(cp.peliculas)
    id = input("Ingrese el id del genero: ")
    nom = input("Ingrese el nombre del genero: ")
    genero ={
        'id': id,
        'nombre':nom,
    }
    print(genero)
    cf.addData(id,nom)
    os.system('pause')
    return genero

def listarGenero():
    cf.readfile()
    os.system('pause')
