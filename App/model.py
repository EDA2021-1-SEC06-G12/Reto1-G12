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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def initCatalog(dataStructure):
    return {
            'videos': lt.newList(dataStructure),
            'categories': lt.newList(dataStructure)
            }


# Funciones para agregar informacion al catalogo
def addVideo(catalog,video):
    lt.addLast(catalog['videos'],video)

def addCategory(catalog,category):
    lt.addLast(catalog['categories'],category)

def cmpVideosbyViews(video1,video2):
    return(int(video1["views"])<int(video2["views"]))

def sortVideos(catalog, size, algorithm):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()

    if algorithm == "shell":
        start_time = time.process_time()
        shes.sort(sub_list, cmpVideosbyViews)
        stop_time = time.process_time()

    elif algorithm == "selection":
        start_time = time.process_time()
        sels.sort(sub_list, cmpVideosbyViews)
        stop_time = time.process_time()

    elif algorithm == "insertion":
        start_time = time.process_time()
        inss.sort(sub_list, cmpVideosbyViews)
        stop_time = time.process_time()
    
    elapsed_time_mseg = round((stop_time - start_time)*1000,2)
    return elapsed_time_mseg
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento