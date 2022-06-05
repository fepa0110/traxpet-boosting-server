import drda
import pandas
from constants import getConnection
class ModelService:
    def __init__(self):
        self.conn = getConnection()

    def set_connection(self, conn):
        self.conn = conn

    def get_model_by_especie_id(self, especie_id):
        cur = self.conn.cursor()

        cur.execute("SELECT model.modelo_id, model.FILENAME " +
                    "FROM MODELO AS model " +
                    "WHERE model.ESPECIE_ID = "+str(especie_id))

        result = cur.fetchall()
        if(len(result) > 0):
            print("Modelo obtenido")
            return result[0]
        else:
            return None
