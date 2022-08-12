import drda
import pandas
from constants import getConnection
class MascotasEntrenadasService:
    def __init__(self):
        self.conn = getConnection()

    def set_connection(self, conn):
        self.conn = conn

    def get_by_model_id(self, model_id):
        cur = self.conn.cursor()

        cur.execute("SELECT mascotasEntrenadas.orden, mascotasEntrenadas.mascota_id " +
                    "FROM MASCOTASENTRENADAS AS mascotasEntrenadas " +
                    "WHERE mascotasEntrenadas.modelo_id = "+str(model_id)+
                    " ORDER BY mascotasEntrenadas.orden ASC")

        result = cur.fetchall()
        if(len(result) > 0):
            print("{} mascotas entrenadas obtenidas".format(len(result)))
            return result
        else:
            return None

    def get_max_id(self):
            cur = self.conn.cursor()

            cur.execute("SELECT MAX(mascotas_entrenadas.mascota_entrenada_id) " +
                "FROM MASCOTASENTRENADAS AS mascotas_entrenadas ")

            result = cur.fetchall()
            if(len(result) > 0):
                return result[0][0]
            else:
                return None

    def create_mascota_entrenada(self, mascota_entrenada_id, orden, mascota_id, modelo_id):
            cur = self.conn.cursor()

            query = "INSERT INTO MASCOTASENTRENADAS"+\
                "(mascota_entrenada_id, orden, mascota_id, modelo_id) " +\
                "VALUES ("+str(mascota_entrenada_id)+", "+str(orden) + \
                ","+str(mascota_id)+","+str(modelo_id)+")"
            
            print(query)
            
            cur.execute(query)