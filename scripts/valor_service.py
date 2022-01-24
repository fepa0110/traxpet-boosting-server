import drda
import pandas

class ValorService:
    def __init__(self):
        self.conn = drda.connect(
            host='localhost', database='traxpet-db', port=28001)

    def set_connection(self, conn):
        self.conn = conn

    def get_nombre_by_id(self, valor_id):
        cur = self.conn.cursor()

        cur.execute("SELECT valor.NOMBRE " +
                    "FROM Valor AS valor " +
                    "WHERE valor.VALOR_ID = "+str(valor_id))

        result = cur.fetchall()
        if(len(result) > 0):
            return result[0][0]
        else:
            return None
