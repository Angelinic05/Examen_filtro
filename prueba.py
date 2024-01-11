import funciones.peliculas as cp
import os
# peliculas = {}
# pelicula = {'id':'00',
#             'nombre':'mohana'
# }

# peliculas.update({pelicula['id']:peliculas})
# print(peliculas)

# for i,j in peliculas.items():
#     for key,item in j.items():
#         print(f"{key}:{item}")

# print(pelicula.get('00').get('mohana'))
cp.cf.newfile(cp.peliculas)
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
cp.newpelicula(pelicula)
os.system('pause')