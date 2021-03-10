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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shes
from DISClib.Algorithms.Sorting import insertionsort as inss
from DISClib.Algorithms.Sorting import selectionsort as sels
from DISClib.Algorithms.Sorting import mergesort as mrge
from DISClib.Algorithms.Sorting import quicksort as quck
from DISClib.DataStructures import listiterator as it
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def initCatalog():
    return {
            'videos': lt.newList(datastructure='ARRAY_LIST', cmpfunction=cmpVideosbyViews),
            'categories': lt.newList(datastructure='ARRAY_LIST')
            }

def addVideo(catalog,video):
    lt.addLast(catalog['videos'],video)

def addCategory(catalog,category):
    lt.addLast(catalog['categories'],category)

# Funciones de consulta

def categoriaporID(name,catalog):
    categorias=catalog['categories']
    i=1
    while i<=lt.size(categorias):
        c=lt.getElement(categorias,i)
        if name.lower() in (c['name']).lower():
            return c['id']
        i+=1


def lporcyp(ID,pais,lista):
    v=it.newIterator(lista)
    final=lt.newList(datastructure='ARRAY_LIST')
    while it.hasNext(v):
        x=it.next(v)
        if x['country']==pais and x['category_id']==ID:
            lt.addLast(final,x)
    if lt.isEmpty(final)==True:
        return None
    else:
        return final



def lporcategoria(ID,lista):
    final=lt.newList()
    i=it.newIterator(lista)
    while it.hasNext(i):
        v=it.next(i)
        if v['category_id']==ID:
            lt.addFirst(final,v)
    if lt.isEmpty(final)==True:
        return None
    else:
        return final


def lporpais(pais,lista):
    final=lt.newList()
    i=it.newIterator(lista)
    while it.hasNext(i):
        v=it.next(i)
        if v['country'].lower()==pais.lower():
            lt.addFirst(final,v)
    if lt.isEmpty(final)==True:
        return None
    else:
        return final


def lporcategoriaypais(categoria,pais,lista):
    categorias=catalog['categories']
    n=1
    ide=0
    final=lt.newList()
    while n<=lt.size(categorias):
        c=lt.getElement(categorias,n)
        if categoria.lower() in c['name'].lower():
            ide=c['id']
        n+=1

    if ide==0:
        return None
    else:
        i=1
        while i<=lt.size(lista):
            v=lt.getElement(lista,i)
            if v['category_id']==ide and pais.lower()==v['country'].lower():
                lt.addFirst(final,v)
            i+=1
        if lt.size(final)==0:
            return None
        else:
            return final



def lportyp(tag,pais,lista):
    i=it.newIterator(lista)
    final=lt.newList()
    while it.hasNext(i):
        x=it.next(i)
        if tag in x['tags'] and pais.lower()==x['country']:
            lt.addLast(final,x)
    if lt.isEmpty(final)==True:
        return None
    else:
        return final

def maxtrending(lista):
    parcial=1
    total=1
    title=''
    i=2
    while i<=lt.size(lista):
        v=lt.getElement(lista,i)['title']
        ant=lt.getElement(lista,i-1)['title']
        if v==ant:
            parcial+=1
        else:
            if parcial>total:
                total=parcial
                title=v
            parcial=1
        i+=1
    return title,total

"""def maxdias(lista):
    title=''
    mayortotal=0
    mayorparcial=1
    n=2
    while n<=lt.size(lista):
        vid=lt.getElement(lista,n)
        ant=lt.getElement(lista,n-1)
        if vid['title']==ant['title']:
            if vid['trending_date']!=ant['trending_date']:
                mayorparcial+=1
        else:
            if mayorparcial>mayortotal:
                mayortotal=mayorparcial
                title=ant['title']
                channel_title=ant['channel_title']
                category_id=ant['category_id']
                country=ant['country']

            mayorparcial=0
        n+=1

    if mayorparcial>mayortotal:
        mayortotal=mayorparcial
        title=ant['title']
        channel_title=ant['channel_title']
        category_id=ant['category_id']
        country=ant['country']

    return title,channel_title,category_id,country,mayortotal"""

def maxdias(lista):
    title=''
    mayortotal=0
    mayorparcial=1
    n=2
    while n<=lt.size(lista):
        vid=lt.getElement(lista,n)
        ant=lt.getElement(lista,n-1)
        if vid['title']==ant['title']:
            mayorparcial+=1
        else:
            if mayorparcial>mayortotal:
                mayortotal=mayorparcial
                title=ant['title']
                channel_title=ant['channel_title']
                category_id=ant['category_id']
                country=ant['country']

            mayorparcial=0
        n+=1

    if mayorparcial>mayortotal:
        mayortotal=mayorparcial
        title=ant['title']
        channel_title=ant['channel_title']
        category_id=ant['category_id']
        country=ant['country']

    return title,channel_title,category_id,country,mayortotal



def mayortrending(lista):
    dic={}
    n=1
    while n<=lt.size(lista):
        video=lt.getElement(lista,n)
        if video['title'] in dic.keys():
            l=dic[video['title']]
            x=lt.isPresent(l,video['trending_date'])
            if x==0:
                lt.addLast(l,video['trending_date'])
            n+=1
        else:
            l=lt.newList()
            lt.addLast(l,video['trending_date'])
            dic[video['title']]=l
            n+=1
    
    mayor=0
    title=''
    for titulo in dic:
        lista=dic[titulo]
        num=lt.size(lista)
        if num>mayor:
            mayor=num
            title=titulo
    return title, mayor
    
def imprimir(titulo,catalog):
    videos=catalog['videos']
    m=0
    n=1
    l=[]
    p=[]
    while n<=lt.size(videos):
        x=lt.getElement(videos,n)
        nombre=x['title']
        if titulo in nombre:
            m+=1
            p.append(x['trending_date'])
            if x['trending_date'] not in l:
                l.append(x['trending_date'])
        n+=1
    print(m)
    print(l)
    print(len(l))
    print(len(p))

def Req2(pais,catalog):
    listapais = listaporpais(pais,catalog)
    tupla_titulo_dias = mayortrending(listapais)
    video = buscarportitulo_simplificado(tupla_titulo_dias[0],listapais)
    video["dias"] = tupla_titulo_dias[1]
    return video
    

def buscarportitulo_simplificado(titulo,lista):
    n=1
    centinela=True
    while n<=lt.size(lista) and centinela:
        video=lt.getElement(lista,n)
        if video['title']==titulo:
            centinela=False
        n+=1
    return video 


def ordenadaportitleydate(categoria,catalog):
    lista=listaporcategoria(categoria,catalog)
    x=sortVideos(lista,lt.size(lista),cmpVideosbyDate)[1]
    y=sortVideos(x,lt.size(lista),cmpVideosbyTitle)[1]
    return y


def Req3(categoria,catalog):
    lista=ordenadaportitleydate(categoria,catalog)
    title=''
    mayortotal=0
    mayorparcial=1
    n=2
    while n<=lt.size(lista):
        vid=lt.getElement(lista,n)
        ant=lt.getElement(lista,n-1)
        if vid['title']==ant['title']:
            if vid['trending_date']!=ant['trending_date']:
                mayorparcial+=1
        else:
            if mayorparcial>mayortotal:
                mayortotal=mayorparcial
                title=ant['title']
                channel_title=ant['channel_title']
                category_id=ant['category_id']

            mayorparcial=0
        n+=1

    if mayorparcial>mayortotal:
        mayortotal=mayorparcial
        title=ant['title']
        channel_title=ant['channel_title']
        category_id=ant['category_id']

    return title,channel_title,category_id,mayortotal


# Funciones para creacion de datos



# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosbyViews(video1,video2):
    return(int(video1["views"])>=int(video2["views"]))

def cmpVideosbyLikes(video1,video2):
    return(int(video1["likes"])>=int(video2["likes"]))

def cmpVideosbyTitle(video1,video2):
    return (video1['title'])>(video2['title'])

def cmpVideosbyTitleandDate(video1,video2):
    if (video1['video_id'])>(video2['video_id']):
        return True
    elif video1['title']==video2['title']:
        return video1['trending_date']>video2['trending_date']

def cmpVideosbyDate(video1,video2):
    return (video1['trending_date'])>=(video2['trending_date'])

# Funciones de ordenamiento

def sortVideos(lista,size,cmpfunction):
    if size <= lt.size(lista):
        sub_list = lt.subList(lista, 1, size)
        sub_list = sub_list.copy()
        start_time=time.process_time()
        mrge.sort(sub_list, cmpfunction)
        stop_time=time.process_time()
        elapsed_time_mseg = round((stop_time - start_time)*1000,2)
        return elapsed_time_mseg, sub_list
    else:
        return None


