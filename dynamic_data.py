import drda
import pandas
from services.valor_service import ValorService
from services.caracteristicas_service import CaracteristicasService
from constants import getConnection

class DynamicData:
    def __init__(self,especie_id):
        self.especie_id = especie_id
        self.conn = getConnection()

    def set_connection(self, conn):
        self.conn = conn
        
    def get_especie_id(self,especie_name):
        cur = self.conn.cursor()
        features_dict = dict()
        features_dict["Mascota"] = []

        cur.execute("SELECT esp.ESPECIE_ID " +
                    "FROM ESPECIE AS esp" +
                    "WHERE UPEER(esp.NOMBRE) = "+especie_name.upper())

        return cur.fetchall()[0][0]

    def create_features_dict(self):
        cur = self.conn.cursor()
        features_dict = dict()
        features_dict["Mascota"] = []

        cur.execute("SELECT DISTINCT car.NOMBRE " +
                    "FROM MASCOTA AS mas JOIN MASCOTA_VALOR AS masval ON (mas.MASCOTA_ID=masval.MASCOTAS_MASCOTA_ID)" +
                    "JOIN VALOR AS val ON (masval.VALORES_VALOR_ID=val.VALOR_ID)" +
                    "JOIN CARACTERISTICA AS car ON (val.CARACTERISTICA_ID=car.CARACTERISTICA_ID)" +
                    "WHERE mas.ESPECIE_ID = "+self.especie_id)

        for row in cur.fetchall():
            features_dict[row[0]] = []
        
        return features_dict

    def query_mascotas_especie(self):
        cur = self.conn.cursor()

        # Mascotas
        cur.execute("SELECT mas.MASCOTA_ID " +
                    "FROM MASCOTA AS mas JOIN MASCOTA_VALOR AS masval ON (mas.MASCOTA_ID=masval.MASCOTAS_MASCOTA_ID) "+
                    "JOIN VALOR AS val ON (masval.VALORES_VALOR_ID=val.VALOR_ID) "+
                    "JOIN CARACTERISTICA AS car ON (val.CARACTERISTICA_ID=car.CARACTERISTICA_ID) "+
                    "WHERE mas.ESPECIE_ID = "+self.especie_id+
                    "ORDER BY mas.MASCOTA_ID")
        
        list_mascotas_ids = cur.fetchall()

        cur.execute("SELECT val.VALOR_ID " +
                    "FROM MASCOTA AS mas JOIN MASCOTA_VALOR AS masval ON (mas.MASCOTA_ID=masval.MASCOTAS_MASCOTA_ID) "+
                    "JOIN VALOR AS val ON (masval.VALORES_VALOR_ID=val.VALOR_ID) "+
                    "JOIN CARACTERISTICA AS car ON (val.CARACTERISTICA_ID=car.CARACTERISTICA_ID) "+
                    "WHERE mas.ESPECIE_ID = "+self.especie_id+
                    "ORDER BY mas.MASCOTA_ID")

        list_valores_ids = cur.fetchall()
        # print(len(list_mascotas_ids))

        cur.execute("SELECT car.CARACTERISTICA_ID " +
                    "FROM MASCOTA AS mas JOIN MASCOTA_VALOR AS masval ON (mas.MASCOTA_ID=masval.MASCOTAS_MASCOTA_ID) "+
                    "JOIN VALOR AS val ON (masval.VALORES_VALOR_ID=val.VALOR_ID) "+
                    "JOIN CARACTERISTICA AS car ON (val.CARACTERISTICA_ID=car.CARACTERISTICA_ID) "+
                    "WHERE mas.ESPECIE_ID = "+self.especie_id+
                    "ORDER BY mas.MASCOTA_ID")

        list_caracteristicas_ids = cur.fetchall()

        valorService = ValorService()
        caracteristicasService = CaracteristicasService()

        list_mascotas = list()

        for mascota_index in range(len(list_mascotas_ids)):
            mascota_tuple = (list_mascotas_ids[mascota_index][0],
                            list_valores_ids[mascota_index][0],
                            valorService.get_nombre_by_id(
                                list_valores_ids[mascota_index][0]),
                            caracteristicasService.get_nombre_by_id(
                                list_caracteristicas_ids[mascota_index][0])
                            )
            
            print("Valores leidos: ", mascota_index, "de ",len(list_mascotas_ids))
            list_mascotas.append(mascota_tuple)
        
        # print(list_mascotas)
        return list_mascotas

    def format_mascotas_to_dataFrame(self):
        data_train = self.create_features_dict()
        # print(data_train)

        mascotas_list = self.query_mascotas_especie()
        print(mascotas_list)
        
        mascota_anterior = mascotas_list[0][0]
        lista_mascotas_id = data_train["Mascota"]
        lista_mascotas_id.append(mascota_anterior)
        data_train["Mascota"] = lista_mascotas_id

        for row in mascotas_list:
            mascotaActual = row[0]
            if(mascota_anterior != mascotaActual):
                lenArrays = len(data_train["Mascota"])
                for columna in data_train.keys():
                    if(len(data_train[columna]) != lenArrays):
                        lista_columna = data_train[columna]
                        lista_columna.append("")
                        data_train[columna] = lista_columna
                lista_mascotas_id = data_train["Mascota"]
                lista_mascotas_id.append(mascotaActual)
                data_train["Mascota"] = lista_mascotas_id

            lista = data_train[row[3]]
            lista.append(row[2])

            data_train[row[3]] = lista
            mascota_anterior = mascotaActual


        lenArrays = len(data_train["Mascota"])
        for columna in data_train.keys():
            if(len(data_train[columna]) != lenArrays):
                lista_columna = data_train[columna]
                lista_columna.append("")
                data_train[columna] = lista_columna

        return pandas.DataFrame.from_dict(data_train)
