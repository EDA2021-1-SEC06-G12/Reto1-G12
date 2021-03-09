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

def Requerimiento1(pais,categoria,catalog,num):
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
