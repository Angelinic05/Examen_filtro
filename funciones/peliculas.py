import os
import funciones.corefile as cf

MY_DATA = 'Examen_filtro/data/peliculas.json'
peliculas = {}

def newpelicula (customer) -> dict:
    peliculas.update(customer)
    cf.addData(customer["id"],peliculas)
