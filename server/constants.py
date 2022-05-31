import drda 

HOST = 'if012pf.fi.mdn.unp.edu.ar'
DATABASE = 'traxpet-db'
PORT = 28001

def getConnection():
    return drda.connect(
            host=HOST, database=DATABASE,port=PORT)