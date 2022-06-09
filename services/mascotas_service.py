from constants import getConnection
import pandas
import drda
import string

class MascotasService:
    def __init__(self):
        self.conn = getConnection()

    def set_connection(self, conn):
        self.conn = conn

    def get_ids_mascotas_by_especie_id(self, especie_id):
        cur = self.conn.cursor()

        cur.execute("SELECT MASCOTA.MASCOTA_ID " +
                    "FROM PUBLICACION AS publicacion JOIN MASCOTA AS mascota "+
                    "ON(PUBLICACION.MASCOTA_ID=MASCOTA.MASCOTA_ID) "+
                    "WHERE publicacion.ESTADO='ACTIVA' AND MASCOTA.ESPECIE_ID="+str(especie_id))

        result = cur.fetchall()
        if(len(result) > 0):
            return result
        else:
            return None
