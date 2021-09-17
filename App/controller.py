﻿"""
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
from DISClib.Algorithms.Sorting import selectionsort as merge

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de artistas

def initCatalog(tipo):

    catalog = model.newCatalog(tipo)
    return catalog


# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)

def loadArtists(catalog):
    """
    Carga los artistas del archivo.
    """
    artistsfiles = cf.data_dir + "Artists-utf8-large.csv"
    input_file = csv.DictReader(open(artistsfiles, encoding="utf-8"))
    for artist in input_file:
        model.addArtist(catalog, artist)



def loadArtworks(catalog):
    """
    Carga las obras del archivo.
    """
    artworksfiles = cf.data_dir + "Artworks-utf8-large.csv"
    input_file = csv.DictReader(open(artworksfiles, encoding="utf-8"))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

##crea una lista de artistas nacidos entre dos fechas dadas por parametro

def listarArtistas(catalog, inicio, fin):
    
    model.ordenarArtistas(catalog["artists"])

    rango_artistas = lt.newList(datastructure="SINGLE_LINKED")

    i = 1
    c = False
    while i<=lt.size(catalog["artists"]) and not c:

        artista = lt.getElement(catalog["artists"], i)
        if int(artista["BeginDate"]) > fin:
            c = True
        
        if int(artista["BeginDate"]) >= inicio and int(artista["BeginDate"]) <= fin:
            lt.addLast(rango_artistas, artista)
        i+=1

    return rango_artistas
        
def compareBeginDate(artist1, artist2):
    
    return (int(artist1["BeginDate"])>int(artist2["BeginDate"]))
# Funciones de ordenamiento

def sortArtworksByDateAcquired(catalog, size, alg):

    return model.sortByDate(catalog, size, alg)

# Funciones de consulta sobre el catálogo