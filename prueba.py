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
peliculas = {}
for i in range(1,3,1):
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
    peliculas.update({pelicula['id']:peliculas})
    print(peliculas)
# idg = int(input("Ingrese el id de la pelicula: "))
# nomg = input("Ingrese el nombre de la pelicula: ")
# genero ={
#     'id': idg,
#     'nombre':nomg,
# }

# # cp.newpelicula(pelicula)
# # os.system('pause')
# pelicula.update({genero ['id']:pelicula})
# print(pelicula)
# ida = int(input("Ingrese el id de la pelicula: "))
# noma = input("Ingrese el nombre de la pelicula: ")
# actor ={
#     'id': id,
#     'nombre':nom,
# }
# # print(pelicula)
# # peliculas.update({pelicula['id']:peliculas})
# # # cp.newpelicula(pelicula)
# # # os.system('pause')
# # print(peliculas)
# pelicula.update({actor ['id']:pelicula})
# print(pelicula)
id = int(input("pelicula a buscar"))
for i,j in peliculas.items():
    for key,item in j.items():
        print(f"{key}:{item}")
        if (id == item):
            print (item)