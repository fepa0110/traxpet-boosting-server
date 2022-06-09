import drda
import pandas
from constants import getConnection
class EspecieService:
    def __init__(self, conn=getConnection()):
        self.conn = conn

    def set_connection(self, conn):
        self.conn = conn

    def get_especie_id(self, especie_name):
        cur = self.conn.cursor()

        cur.execute("SELECT esp.ESPECIE_ID " +
                    "FROM ESPECIE AS esp " +
                    "WHERE UPPER(esp.NOMBRE) = UPPER('"+especie_name+"')")
        
        result = cur.fetchall()
        if(len(result) > 0):
            print(result[0][0])
            return result[0][0]
        else:
            return None
        
    def get_especie_nombre(self, especie_id):
        cur = self.conn.cursor()

        cur.execute("SELECT esp.nombre " +
                    "FROM ESPECIE AS esp " +
                    "WHERE esp.especie_id = "+str(especie_id))
        
        result = cur.fetchall()
        if(len(result) > 0):
            return result[0][0]
        else:
            return None

    def get_especies_activas(self):
        cur = self.conn.cursor()

        cur.execute("SELECT * " +
                    "FROM ESPECIE AS esp " +
                    "WHERE esp.deshabilitado = 0")

        result = cur.fetchall()
        if(len(result) > 0):
            return result
        else:
            return None
