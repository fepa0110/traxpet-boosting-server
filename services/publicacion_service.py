from constants import getConnection
from datetime import date

from dateutil.relativedelta import relativedelta

class PublicacionService:
    def __init__(self):
        self.conn = getConnection()

    def set_connection(self, conn):
        self.conn = conn

    def clean_up_posts(self):
        current_date = date.today()
        cur = self.conn.cursor()
        previus_date = current_date - relativedelta(months=6)
        
        #query ="SELECT * FROM PUBLICACION AS publicacion where publicacion.FECHAPUBLICACION <= DATE('{}')".format(str(previus_date))
        query = "UPDATE PUBLICACION SET ESTADO='INACTIVA' where FECHAMODIFICACION <= DATE('{}')".format(str(previus_date))
        #query = "SELECT * FROM PUBLICACION AS publicacion where publicacion.ESTADO = 'ACTIVA'"
        print(query)
        cur.execute(query)
        
        result = cur.fetchall()
        #print(result)
        print(len(result))

        if(len(result) > 0):
            return result[0][0]
        else:
            return None