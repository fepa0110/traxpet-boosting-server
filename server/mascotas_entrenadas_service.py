import drda
import pandas

class MascotasEntrenadasService:
    def __init__(self):
        self.conn = drda.connect(
            host='localhost', database='traxpet-db', port=28001)

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
            return result
        else:
            return None
