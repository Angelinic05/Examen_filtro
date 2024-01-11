import os
import funciones.peliculas as cp


peliuclas = {}

def generarPelicula():
    cp.cf.checkfile(cp.peliculas)

# def BuscarPelicula():
#     data = cp.
def agregarPelicula():
    print("aaaaaaaaaaa")
    cp.cf.checkfile(cp.peliculas)
    id = int(input("Ingrese el id de la pelicula: "))
    nom = input("Ingrese el nombre de la pelicula: ")
    duracion = input("Ingrese la duracion de la pelicula: ")
    sipnosis = input("Ingrese la sipnosis de la pelicula: ")
    pelicula ={
        'id': id,
        'nombre':nom,
        'duracion':duracion,
        'sipnosis':sipnosis
    }
    print(pelicula)
    cp.newpelicula()
    os.system('pause')
    

