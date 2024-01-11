import os
import funciones.peliculas as cp

# peliuclas = {}

# def generarPelicula():
#     cp.cf.checkfile(cp.peliculas)

def agregarGenero(pelicula):
    cp.cf.checkfile(cp.peliculas)
    id = int(input("Ingrese el id de la pelicula: "))
    nom = input("Ingrese el nombre del genero: ")
    genero ={
        'id': id,
        'nombre':nom,
    }
    print(genero)
    pelicula.update({genero ['id']:pelicula})
    cp.newpelicula(pelicula)
    os.system('pause')
