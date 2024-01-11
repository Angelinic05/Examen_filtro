import os
import funciones.peliculas as cp
import funciones.corefile as cf
# peliuclas = {}

# def generarPelicula():
#     cp.cf.checkfile(cp.peliculas)

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

def listarGenero(genero: dict):
    cf.readfile()
    print(genero)
    os.system('pause')
    # for i,j in peliculas.items():
    #     for key,item in j.items():
    #         print(f"{key}:{item}")