import os
import funciones.peliculas as cp


def agregarFormato(pelicula):
    cp.cf.checkfile(cp.peliculas)
    id = int(input("Ingrese el id de la pelicula: "))
    nom = input("Ingrese el nombre del formato: ")
    formato ={
        'id': id,
        'nombre':nom,
    }
    print(formato)
    pelicula.update({formato ['id']:pelicula})
    cp.newpelicula(pelicula)
    os.system('pause')
