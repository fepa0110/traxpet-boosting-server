import drda
import pandas

class EspecieService:
    def __init__(self):
        self.conn = drda.connect(
            host='localhost', database='traxpet-db', port=28001)

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
