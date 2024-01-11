import os
import funciones.peliculas as cp

# peliuclas = {}

# def generarPelicula():
#     cp.cf.checkfile(cp.peliculas)

def agregarActor(pelicula):
    cp.cf.checkfile(cp.peliculas)
    id = int(input("Ingrese el id de la pelicula: "))
    nom = input("Ingrese el nombre del actor: ")
    actor ={
        'id': id,
        'nombre':nom,
    }
    print(actor)
    pelicula.update({actor ['id']:pelicula})
    cp.newpelicula(pelicula)
    os.system('pause')
