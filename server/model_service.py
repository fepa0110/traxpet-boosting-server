import drda
import pandas

class ModelService:
    def __init__(self):
        self.conn = drda.connect(
            host='localhost', database='traxpet-db', port=28001)

    def set_connection(self, conn):
        self.conn = conn

    def get_model_by_especie_id(self, especie_id):
        cur = self.conn.cursor()

        cur.execute("SELECT model.modelo_id, model.FILENAME " +
                    "FROM MODELO AS model " +
                    "WHERE model.ESPECIE_ID = "+str(especie_id))

        result = cur.fetchall()
        if(len(result) > 0):
            return result[0]
        else:
            return None
