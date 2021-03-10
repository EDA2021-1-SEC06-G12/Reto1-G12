"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    return model.initCatalog()

def loadData(catalog):
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)
    categoriesfile = cf.data_dir + "category-id.csv"
    i_file = csv.DictReader(open(categoriesfile, encoding='utf-8'), delimiter='\t')
    for category in i_file:
        model.addCategory(catalog,category)

def mejoresVideosPorViews(catalog, size):
    return model.sortVideos(catalog,size,cmpVideosbyViews)

def R1(categoria,pais,num,catalog):
    ID=model.categoriaporID(categoria,catalog)
    if ID==None:
        return 'Categoría no válida'
    else:
        l=model.lporcyp(ID,pais,catalog['videos'])
        if l==None:
            return 'País no válido.'
        else:
            l2=model.sortVideos(l,lt.size(l),model.cmpVideosbyViews)[1]
            if num>lt.size(l2):
                return 'El número ingresado excede la cantidad de videos que cumplen con los requisitos. Intente con un número igual o menor a '+str(lt.size(l))
            else:
                n=0
                c=''
                final=lt.subList(l2,1,num)
                i=it.newIterator(final)
                while it.hasNext(i):
                    n+=1
                    vid=it.next(i)
                    c=c+'\nPuesto '+str(n)+'\ntrending_date: '+vid['trending_date']+'; title: '+vid['title']+'; channel_title: '+vid['channel_title']+'; publish_time: '+vid['publish_time']+'; views: '+vid['views']+'; likes: '+vid['likes']+ '; dislikes: '+vid['dislikes']+'\n'
                return c


def R2(pais,catalog):
    l1=model.lporpais(pais,catalog['videos'])
    if l1==None:
        return 'No hay información para esta categoría.'
    else:
        orde=model.sortVideos(l1,lt.size(l1),model.cmpVideosbyTitle)[1]
        tupla=model.maxdias(orde)
        return tupla

def R3(categoria,catalog):
    ID=model.categoriaporID(categoria,catalog)
    if ID==None:
        return 'Categoría no válida'
    else:
        print(ID)
        l1=model.lporcategoria(ID,catalog['videos'])
        print(lt.firstElement(l1))
        l2=model.sortVideos(l1,lt.size(l1),model.cmpVideosbyTitle)[1]
        print(lt.firstElement(l2))
        tupla=model.maxdias(l2)
        return tupla
    


def R4(tag,pais,num,catalog):
    l1=model.lportyp(tag,pais,catalog['videos'])
    if l1==None:
        return 'No hay información para el país y/o tag ingresados.'
    else:
        orde=model.sortVideos(l1,lt.size(l1),model.cmpVideosbyLikes)[1]
        final=lt.subList(orde,1,num)
        i=it.newIterator(final)
        c=''
        n=0
        while it.hasNext(i):
            n+=1
            v=it.next(i)
            c=c+'\nPuesto '+str(n)+'\ntitle: '+v['title']+'; channel_title: '+v['channel_title']+'; publish_time: '+v['publish_time']+'; views: '+v['views']+'; likes: '+v['likes']+'; dislikes: '+v['dislikes']+'; tags: '+v['tags']+'\n'
        return c










def Requerimiento1(categoria,pais,num,catalog):
    l1=model.lporpais(pais,catalog['videos'])
    if l1==None:
            return 'No hay información para este país.'
    else:
        l2=lporcategoria(categoria,l1,catalog)
        if l2==None:
            return 'No hay información para esta categoría.'
        else:
            l3=model.sortVideos(l2,lt.size(l2),model.cmpVideosbyViews)
            if l3==None or num>lt.size(l3[1]):
                return 'El número ingresado excede la cantidad de videos disponibles.'
            else:
                lfinal=lt.subList(l3[1],1,num)
                i=1
                c=''
                while i<=num:
                    vid=lt.getElement(lfinal,i)
                    c=c+'\nPuesto '+str(i)+'\ntrending_date: '+vid['trending_date']+'; title: '+vid['title']+'; channel_title: '+vid['channel_title']+'; publish_time: '+vid['publish_time']+'; views: '+vid['views']+'; likes: '+vid['likes']+ '; dislikes: '+vid['dislikes']+'\n'
                    i+=1
                return c


#
 #  l1=model.lporcategoria(categoria,catalog['videos'],catalog)
  #  if l1==None:
   #     return 'No hay información para esta categoría.'
    #else:
     #   l2=model.lporpais(pais,l1)
      #  if l2==None:
       #     return 'No hay información para este país.'
        #else:
         #   l3=model.sortVideos(l2,lt.size(l2),model.cmpVideosbyViews)
          #  if l3==None or num>lt.size(l3[1]):
           #     return 'El número ingresado excede la cantidad de videos disponibles.'
            #else:
             #   lfinal=lt.subList(l3[1],1,num)
              #  i=1
               # c=''
                #while i<=num:
                 #   vid=lt.getElement(lfinal,i)
                  #  c=c+'\nPuesto '+str(i)+'\ntrending_date: '+vid['trending_date']+'; title: '+vid['title']+'; channel_title: '+vid['channel_title']+'; publish_time: '+vid['publish_time']+'; views: '+vid['views']+'; likes: '+vid['likes']+ '; dislikes: '+vid['dislikes']+'\n'
                   # i+=1
                #return c


def Requerimiento2(pais,catalog):
    l1=model.lporpais(pais,catalog['videos'])
    if l1==None:
        return 'No hay información para esta categoría.'
    else:
        l2=model.sortVideos(l1,lt.size(l1),model.cmpVideosbyTitleandDate)[1]
        tupla=model.maxdias(l2)
        return str(tupla)

def Requerimiento3(categoria,catalog):
    l1=model.lporcategoria(categoria,catalog['videos'],catalog)
    if l1==None:
        return 'No hay información para esta categoría.'
    else:
        l2=model.sortVideos(l1,lt.size(l1),model.cmpVideosbyTitleandDate)[1]
        tupla=model.maxdias(l2)
        return str(tupla)
        

def Req1(pais,categoria,catalog,num):
    return model.Req1(pais,categoria,catalog,num)


def Requerimiento2(pais,catalog):
    return model.Req2(pais,catalog)

def Requerimiento3(categoria,catalog):
    return model.Req3(categoria,catalog)

def Requerimiento4(tag,numero_vid,pais,catalog):
    return model.Req4(tag,numero_vid,pais,catalog)

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
