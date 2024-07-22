"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import fileinput
from collections import OrderedDict



def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/  214
    """
    files = "data.csv"
    f=fileinput.input(files=files)
    acumulador=0
    for line in f:
        fila=line.split()
        acumulador+=int(fila[1])
    
    return acumulador

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.
    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    """
    files = "data.csv"
    f=fileinput.input(files=files)
    diccionario= {}
    lista= []

    for line in f:
        fila=line.split()
        if fila[0] in diccionario:
            diccionario[fila[0]] += 1
        else:
            diccionario[fila[0]]= 1    
    orderDiccionario= OrderedDict(sorted(diccionario.items()))
    for key in orderDiccionario:
        lista.append((key, orderDiccionario[key]))
    return lista
def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.
    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
    files = "data.csv"
    f=fileinput.input(files=files)
    diccionario= {}
    lista= []

    for line in f:
        fila=line.split()
        if fila[0] in diccionario:
            diccionario[fila[0]] += int(fila[1])
        else:
            diccionario[fila[0]]= int(fila[1]) 
    orderDiccionario= OrderedDict(sorted(diccionario.items()))
    for key in orderDiccionario:
        lista.append((key, orderDiccionario[key]))
    return lista

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.
    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    files = "data.csv"
    f=fileinput.input(files=files)
    diccionario= {}
    lista= []

    for line in f:
        fila=line.split()
        mes= fila[2].split("-")[1]
        if mes in diccionario:
            diccionario[mes] += 1
        else:
            diccionario[mes]= 1
    orderDiccionario= OrderedDict(sorted(diccionario.items()))
    for key in orderDiccionario:
        lista.append((key, orderDiccionario[key]))
    return lista

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.
    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    """
    files = "data.csv"
    f=fileinput.input(files=files)
    diccionario= {}
    lista= []

    for line in f:
        fila=line.split()
        if fila[0] in diccionario:
            max= diccionario[fila[0]][0]
            min= diccionario[fila[0]][1]
            if int(fila[1]) > max:
                diccionario[fila[0]][0] = int(fila[1])
            if int(fila[1]) < min:
                diccionario[fila[0]][1] = int(fila[1])
        else:
            diccionario[fila[0]]= [int(fila[1]), int(fila[1])]
    orderDiccionario= OrderedDict(sorted(diccionario.items()))
    for key in orderDiccionario:
        lista.append((key, orderDiccionario[key][0], orderDiccionario[key][1]))
    return lista
    return


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.
    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    """
    files = "data.csv"
    f=fileinput.input(files=files)
    diccionario= {}
    lista= []

    for line in f:
        fila=line.split()
        texto= fila[4].split(",")
        for codigos in texto:
            codigo= codigos.split(":")
            letras = codigo[0]
            numero = codigo[1]
            if letras in diccionario:
                max= diccionario[letras][1]
                min= diccionario[letras][0]
                if int(numero) > max:
                    diccionario[letras][1] = int(numero)
                if int(numero) < min:
                    diccionario[letras][0] = int(numero)
            else:
                diccionario[letras]= [int(numero), int(numero)] 
    orderDiccionario= OrderedDict(sorted(diccionario.items()))
    for key in orderDiccionario:
        lista.append((key, orderDiccionario[key][0],orderDiccionario[key][1] ))
    return lista
    return


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.
    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    """
    files = "data.csv"
    f=fileinput.input(files=files)
    diccionario= {}
    lista= []

    for line in f:
        fila=line.split()
        if int(fila[1]) in diccionario:
            diccionario[int(fila[1])].append(fila[0])
        else:
            diccionario[int(fila[1])]= [fila[0]]
    orderDiccionario= OrderedDict(sorted(diccionario.items()))
    for key in orderDiccionario:
        lista.append((key, orderDiccionario[key]))
    return lista
    return


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.
    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]
    """
    files = "data.csv"
    f=fileinput.input(files=files)
    diccionario= {}
    lista= []

    for line in f:
        fila=line.split()
        if int(fila[1]) in diccionario:
            if fila[0] not in diccionario[int(fila[1])]:
                diccionario[int(fila[1])].append(fila[0])
        else:
            diccionario[int(fila[1])]=[fila[0]] 
    orderDiccionario= OrderedDict(sorted(diccionario.items()))
    for key in orderDiccionario:
        orderDiccionario[key].sort()
        lista.append((key, orderDiccionario[key]))
    return lista
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    files = "data.csv"
    f=fileinput.input(files=files)
    diccionario= {}
    lista= {}

    for line in f:
        fila=line.split()
        texto= fila[4].split(",")
        for codigos in texto:
            codigo= codigos.split(":")
            letras = codigo[0]
            numero = codigo[1]
            if letras in diccionario:
                diccionario[letras]+= 1
            else:
                diccionario[letras]= 1
    orderDiccionario= OrderedDict(sorted(diccionario.items()))
    for key in orderDiccionario:
        lista[key]= orderDiccionario[key]
    return lista
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.
    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    files = "data.csv"
    f=fileinput.input(files=files)
    lista= []

    for line in f:
        fila=line.split()
        len_col3= len(fila[3].split(","))
        len_col4= len(fila[4].split(","))
        lista.append((fila[0], len_col3, len_col4))
    return lista
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.
    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    files = "data.csv"
    f=fileinput.input(files=files)
    diccionario= {}
    lista= {}

    for line in f:
        fila=line.split()
        letras= fila[3].split(",")
        for letra in letras:
            if letra in diccionario:
                diccionario[letra] += int(fila[1])
            else:
                diccionario[letra]= int(fila[1]) 
    orderDiccionario= OrderedDict(sorted(diccionario.items()))
    for key in orderDiccionario:
        lista[key]= orderDiccionario[key]
    print(lista)
    return lista

    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.
    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }
    """
    files = "data.csv"
    f=fileinput.input(files=files)
    diccionario= {}
    lista= {}

    for line in f:
        fila=line.split()
        texto= fila[4].split(",")
        suma= 0
        for codigos in texto:
            codigo= codigos.split(":")
            letras = codigo[0]
            numero = int(codigo[1])
            suma+= numero
        if fila[0] in diccionario:
            diccionario[fila[0]]+= suma
        else:
            diccionario[fila[0]]= suma 
            
    orderDiccionario= OrderedDict(sorted(diccionario.items()))
    for key in orderDiccionario:
        lista[key]= orderDiccionario[key]
    return lista
    return