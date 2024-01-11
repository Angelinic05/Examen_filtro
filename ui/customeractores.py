import os
import funciones.peliculas as cp
import funciones.corefile as cf
# peliuclas = {}

# def generarPelicula():
#     cp.cf.checkfile(cp.peliculas)

def agregarActor():
    cp.cf.checkfile(cp.peliculas)
    id = int(input("Ingrese el id del actor: "))
    nom = input("Ingrese el nombre del actor: ")
    actor ={
        'id': id,
        'nombre':nom,
    }
    print(actor)
    cf.addData(id,nom)
    os.system('pause')