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

        print('\nIngrese el número del tipo de lista en el que desee cargar el catálogo: \n1 - LINKED_LIST \n2 - ARRAY_LIST')
        ed=int(input(''))

        if ed==1:
            estructuraDeDatos = "LINKED_LIST"
        elif ed==2:
            estructuraDeDatos = "ARRAY_LIST"

        print("\nCargando información de los archivos...")
        catalog = controller.initCatalog(estructuraDeDatos)
        controller.loadData(catalog)

        print("\nSe cargaron " + str(lt.size(catalog['videos'])) + " datos de video y " + str(lt.size(catalog['categories'])) + " de categorías.")

        video_uno=lt.getElement(catalog['videos'],1)
        titulo=str(video_uno['title'])
        canal=str(video_uno['channel_title'])
        trendingdate=str(video_uno['trending_date'])
        pais=str(video_uno['country'])
        views=str(video_uno['views'])
        likes=str(video_uno['likes'])
        dislikes=str(video_uno['dislikes'])
        ID=str(video_uno['category_id'])

        print("\nInformación del primer video cargado \n" + "Título: " + titulo + "\nTítulo del canal: " + canal + "\nTrending date: " + trendingdate + "\nPaís: " + pais + "\nVistas: " + views + "\nLikes: " + likes + "\nDislikes: " + dislikes+'\n')
        print(ID)
        print("\nLista de categorías " + "\nID - Nombre")
        n=1

        while n <= lt.size(catalog['categories']):
            x=lt.getElement(catalog['categories'],n)
            print(str(x['id']) + " - " + str(x['name']))
            n=n+1
        print('\n')


    elif int(inputs[0]) == 2:
        numeroDeElementos = int(input("\nIngrese el número de videos que desee: \n"))
        print('\nIngrese el número del algoritmo con el cual desea ordenar el catálogo por vistas: \n1 - shell \n2 - insertion \n3 - selection \n4 - merge \n5- quick')
        alg=int(input(''))
        if alg==1:
            algoritmo='shell'
        elif alg==2:
            algoritmo='insertion'
        elif alg==3:
            algoritmo='selection'
        elif alg==4:
            algoritmo='merge'
        elif alg==5:
            algoritmo='quick'
        
        print('Cargando...\n')
        print((controller.mejoresVideosPorViews(catalog,numeroDeElementos,algoritmo))[0])
        print('\n')

    elif int(inputs[0]) == 6:
        numero=int(input('Ingrese el número de videos: '))
        pais=input('Ingrese el país: ')
        categoria=input('Ingrese la categoría: ')
        print('\nCargando...\n')
        l=controller.Requerimiento1(pais,categoria,catalog,numero)
        n=1
        while n<=lt.size(l):
            v=lt.getElement(l,n)
            trending_date=v['trending_date']
            title=v['title']
            channel_title=v['channel_title']
            publish_time=v['publish_time']
            views=time=v['views']
            likes=v['likes']
            dislikes=v['dislikes']
            print('Puesto ' + str(n) + '\ntrending_date: ' + trending_date + '; title: ' + title +'; channel_title: '+channel_title + '; publish_time: ' +publish_time +'; views: '+views+'; likes: '+likes+ '; dislikes: ' + dislikes + '\n')
            n+=1

    elif int(inputs[0]) == 3:
        print("Requerimiento 3")
        categoria=input('Ingrese la categoría: ')
        final=controller.Requerimiento3(categoria,catalog)
        title=final[0]
        channel_title=final[1]
        category_id=final[2]
        dias=final[3]
        print('\ntitle: '+title+'; channel_title: '+channel_title+'; category_id: '+category_id+'; días: '+str(dias) +'\n')


    elif int(inputs[0]) == 4:
        print("Requerimiento 2")
        pais = input("Ingrese el país: ")

        v = controller.Requerimiento2(pais,catalog)
        channel_title= v['channel_title']
        title= v['title']
        country = v["country"]
        numero_de_dias = v["dias"]


        print('\ntitle: '+title+'; channel_title: '+channel_title+'; country: '+country+'; numero de dias: '+str(numero_de_dias) +'\n')


    elif int(inputs[0]) == 5:
        print("Requerimiento 4")

        tag = input("Ingrese el tag: ")
        numero_vid = int(input("Ingrese el número de videos: "))
        pais = input("Ingrese el país: ")

        lista_videos = controller.Requerimiento4(tag,numero_vid,pais, catalog)

        lista_videos = lt.subList(lista_videos,1,numero_vid)

        n = 1
        
        while n<=lt.size(lista_videos):
            v = lt.getElement(lista_videos,n)
            channel_title= v['channel_title']
            title= v['title']
            publish_time = str(v["publish_time"])
            views = str(v["views"])
            likes = str(v["likes"])
            dislikes = str(v["dislikes"])
            tags = v["tags"]


            print('\ntitle: '+title+'; channel_title: '+ channel_title +'; publish_time: '+ publish_time +'; views: '+views +'; likes: '+likes+'; dislikes: '+dislikes+'; tags: '+tags+'\n')

            n +=1




    else:
        sys.exit(0)
sys.exit(0)
