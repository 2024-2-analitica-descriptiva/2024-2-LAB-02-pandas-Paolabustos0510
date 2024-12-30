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


def pregunta_07():
    suma_c2 = tbl_0.groupby('c1')['c2'].sum()
    return (suma_c2)



    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: c2, dtype: int64
    """
