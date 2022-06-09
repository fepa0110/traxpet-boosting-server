import string
import drda
import pandas
from constants import getConnection
class ModelService:
    def __init__(self):
        self.conn = getConnection()

    def set_connection(self, conn):
        self.conn = conn

    def get_model_filename_by_especie_id(self, especie_id):
        cur = self.conn.cursor()

        cur.execute("SELECT model.FILENAME " +
                    "FROM MODELO AS model " +
                    "WHERE model.ESPECIE_ID = "+str(especie_id)+ 
                    " AND model.ACTIVO = 1")

        result = cur.fetchall()
        if(len(result) > 0):
            return result[0][0]
        else:
            return None
        
    def get_model_by_especie_id(self, especie_id):
        cur = self.conn.cursor()

        cur.execute("SELECT * " +
                    "FROM MODELO AS model " +
                    "WHERE model.ESPECIE_ID = "+str(especie_id)+ 
                    " AND model.ACTIVO = 1")

        result = cur.fetchall()
        if(len(result) > 0):
            return result[0]
        else:
            return None
        
    def get_total_models(self):
        cur = self.conn.cursor()

        cur.execute("SELECT COUNT(model.modelo_id) FROM MODELO AS model ")

        result = cur.fetchall()
        if(len(result) > 0):
            return result[0][0]
        else:
            return None
        
    def get_max_id(self):
        cur = self.conn.cursor()

        cur.execute("SELECT MAX(model.modelo_id) FROM MODELO AS model ")

        result = cur.fetchall()
        if(len(result) > 0):
            return result[0][0]
        else:
            return None
        
    def create_model(self, nuevo_modelo_id, filename, especie_id):
        cur = self.conn.cursor()

        query = "INSERT INTO MODELO(MODELO_ID, FILENAME, ESPECIE_ID, ACTIVO) " +\
            "VALUES ("+str(nuevo_modelo_id)+", '"+filename+"',"+str(especie_id)+",1)"
        
        print(query)
        
        cur.execute(query)

    def deshabilitar_modelo_id(self, modelo_id):
        cur = self.conn.cursor()

        query = "UPDATE MODELO SET ACTIVO = 0 WHERE MODELO_ID = {}".format(str(modelo_id))
        
        print(query)
        
        cur.execute(query)
