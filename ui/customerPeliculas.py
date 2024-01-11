import os
import funciones.peliculas as cp
import ui.customergeneros as cg

# peliculas = {}

# def generarPelicula():
#     cp.cf.checkfile(cp.peliculas)

def agregarPelicula():
    cp.cf.checkfile(cp.peliculas)
    id = int(input("Ingrese el id de la pelicula: "))
    nom = input("Ingrese el nombre de la pelicula: ")
    duracion = input("Ingrese la duracion de la pelicula: ")
    sipnosis = input("Ingrese la sipnosis de la pelicula: ")
    pelicula ={
        'id': id,
        'nombre':nom,
        'duracion':duracion,
        'sipnosis':sipnosis,
        'generos':'',
        'actores':'',
        'formato':''

    }
    
    cp.newpelicula(pelicula)
    os.system('pause')
    return pelicula

def EliminarPelicula():
    cp.DelPelicula()


    

