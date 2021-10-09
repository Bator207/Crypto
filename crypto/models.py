import sqlite3
from sqlite3.dbapi2 import OperationalError
from flask.helpers import flash

class DBManager():
    def __init__(self, bbdd):
        self.ruta_bbdd = bbdd

    # Funcion que sirve para crear una consulta a la BBDD que devuelta una entrada o varias
    def consultaSQL(self, consulta, params=[]):
        # posible error de conexion BBDD
        conexion = sqlite3.connect(self.ruta_bbdd)
        cursor = conexion.cursor()
        # posible error al ejecutar consulta
        cursor.execute(consulta, params)
        # comprobar si la tabla tiene valores
        claves = cursor.description
        resultado = []
        for fila in cursor.fetchall():
            d = {}
            for tclave, valor in zip(claves, fila):
                d[tclave[0]] = valor
            resultado.append(d)
        conexion.close()
        return resultado