"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
import os
data = os.path.join(os.path.dirname(__file__), "../files/input/tbl0.tsv")
#data = r"C:\Users\Olga\Documents\GitHub\2024-2-LAB-02-pandas-Paolabustos0510\files\input\tbl0.tsv"
tbl_0 =pd.read_csv(data, sep="\t")


def pregunta_03():
    cantidad_registros_letra = ((tbl_0['c1'].value_counts().sort_index()))
    return (cantidad_registros_letra)
"""
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
