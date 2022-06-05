## REEMPLAZAR EN SERVER
from importlib.resources import Package
import drda
import pandas
from constants import getConnection

class CaracteristicasService:
    def __init__(self):
        self.conn = getConnection()

    def set_connection(self, conn):
        self.conn = conn

    def get_caracteristicas(self, especie_id):
        cur = self.conn.cursor()

        cur.execute("SELECT DISTINCT caracteristica.NOMBRE " +
                    "FROM Caracteristica AS caracteristica, Valor AS valor " +
                    "WHERE valor.CARACTERISTICA_ID = caracteristica.CARACTERISTICA_ID AND "+ 
                    "valor.ESPECIE_ID = "+str(especie_id))

        result = cur.fetchall()
        if(len(result) > 0):
            print("Caracteristicas obtenidas")
            return result
        else:
            return None
