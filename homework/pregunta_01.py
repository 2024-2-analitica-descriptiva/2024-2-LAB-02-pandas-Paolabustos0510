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

def pregunta_01():
    cantidad_filas_tbl_0 = tbl_0.shape[0]
    return (cantidad_filas_tbl_0)

    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
