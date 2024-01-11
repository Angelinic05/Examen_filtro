import os
import funciones.peliculas as cp
import funciones.corefile as cf

def agregarFormato():
    cp.cf.checkfile(cp.peliculas)
    id = input("Ingrese el id del formato: ")
    nom = input("Ingrese el nombre del formato: ")
    formato ={
        'id': id,
        'nombre':nom,
    }
    print(formato)
    cf.addData(id,nom)
    os.system('pause')
