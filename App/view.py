"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import model
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
assert cf

default_time = 1000
sys.setrecursionlimit(default_time*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenida/o")
    print("1- Cargar información en el catálogo")
    print("2- Consultar el número que se desee de videos con más views que son tendencia en el país y categoría de interés")
    print("3- Consultar el video que ha estado trending por más días en el país que se desee")
    print("4- Consultar el video que ha estado trending por más días en la categoría que se desee")
    print("5- Consultar el número que se desee de videos con más views que son tendencia en el país y tag de interés")
    print("0- Salir")


catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
    if int(inputs[0]) == 1:
        print("\nCargando información de los archivos...")
        catalog = controller.initCatalog()
        controller.loadData(catalog)
        print("\nSe cargaron " + str(lt.size(catalog['videos'])) + " datos de video y " + str(lt.size(catalog['categories'])) + " de categorías.")
        v=lt.firstElement(catalog['videos'])
        print("\nInformación del primer video cargado \n" +"Título: "+v['title']+"\nTítulo del canal: "+v['channel_title']+"\nTrending date: "+v['trending_date']+"\nPaís: "+v['country']+"\nVistas: "+v['views']+ "\nLikes: "+v['likes']+"\nDislikes: "+v['dislikes']+'\n')
        print("\nLista de categorías " + "\nID - Nombre")
        i=it.newIterator(catalog['categories'])
        while it.hasNext(i):
            x=it.next(i)
            print(str(x['id']) + " - " + str(x['name']))
        print('\n')

    elif int(inputs[0])==2:
        categoria=input('Ingrese la categoría: ')
        pais=input('Ingrese el país: ')
        num=int(input('Ingrese el número de videos: '))
        v=controller.R1(categoria,pais,num,catalog)
        print('\n'+v+'\n')


    elif int(inputs[0]) == 3:
        pais = input('Ingrese el país: ')
        v = controller.Requerimiento2(pais,catalog)
        channel_title= v['channel_title']
        title= v['title']
        country = v["country"]
        numero_de_dias = v["dias"]
        print('\ntitle: '+title+'; channel_title: '+channel_title+'; country: '+country+'; numero de dias: '+str(numero_de_dias) +'\n')
   

    elif int(inputs[0]) == 4:
        categoria=input('Ingrese la categoría: ')
        final=controller.Requerimiento3(categoria,catalog)
        title=final[0]
        channel_title=final[1]
        category_id=final[2]
        dias=final[3]
        print('\ntitle: '+title+'; channel_title: '+channel_title+'; category_id: '+category_id+'; días: '+str(dias) +'\n')

    elif int(inputs[0])==5:
        tag=input('Ingrese el tag: ')
        pais=input('Ingrese el país: ')
        num=int(input('Ingrese el número de videos: '))
        x=controller.R4(tag,pais,num,catalog)
        print('\n'+x+'\n')

    elif int(inputs[0])==8:
        pais=input('Ingrese el país: ')
        x=controller.R2(pais,catalog)
        print(x)

    elif int(inputs[0])==9:
        categoria=input('Ingrese la categoría: ')
        x=controller.R3(categoria,catalog)
        print(x)

    else:
        sys.exit(0)
sys.exit(0)


"""   elif int(inputs[0])==9:
        categoria=input('Ingrese la categoría: ')
        vid=controller.Requerimiento3(categoria,catalog)
        title=vid[0]
        channel_title=vid[1]
        category_id=vid[2]
        dias=vid[3]
        print('\ntitle: ' + title +'; channel_title: '+channel_title+'; category_id: '+str(category_id)+'; días: '+str(dias)+'\n')

    elif int(inputs[0])==7:
        categoria=input('Ingrese la categoría: ')
        pais=input('Ingrese el país: ')
        num=int(input('Ingrese el número de videos: '))
        x=controller.Requerimiento1(categoria,pais,num,catalog)
        print('\n'+x+'\n')

    elif int(inputs[0])==8:
        pais=input('Ingrese el país: ')
        x=controller.R2(pais,catalog)
        print(x)

    elif int(inputs[0])==9:
        categoria=input('Ingrese la categoría: ')
        x=controller.R3(categoria,catalog)
        print(x)"""