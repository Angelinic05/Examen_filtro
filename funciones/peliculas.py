import os
import funciones.corefile as cf

peliculas = {}

def validarArchivo():
    if(cf.checkfile()):
        print('ok')
        os.system('pause')
    else:
        cf.newfile(peliculas)

def newpelicula (customer) -> dict:
    peliculas.update(customer)
    cf.addData(customer["id"],peliculas)

def searchCustomer()->dict:
    id=input('Ingrese el Nro Id a Buscar :')
    return peliculas.get(id,{})

def delPelicula():
    id=input('Ingrese el Nro Id a Borrar :')
    cf.Eliminar(id,peliculas)

def modifyCustomer(llave:str,pelicula:dict):
    for key,item in pelicula.items():
        if ((key != 'edad') and (key != 'cc')):
            if (bool(input(f"Desea editar el campo {key} Enter(Si)")) == False):
                pelicula[key]= input(f"Ingrese {key.capitalize()} del cliente : ")
        elif key == 'edad':
            validateAge = True
            while (validateAge):
                try:
                    pelicula["edad"]= int(input(f"Ingrese {key.capitalize()}  del cliente : "))
                except ValueError:
                    print("El valor ingresado es invalido")
                else:
                    validateAge = False
    peliculas[llave].update(peliculas)
    cf.NewFile(peliculas)
           
