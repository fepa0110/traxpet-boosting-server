import drda
import pandas

def create_features_dict(especie_id):
    cur = conn.cursor()
    features_dict = dict()
    features_dict["Mascota"] = []

    cur.execute("SELECT DISTINCT car.NOMBRE " +
                "FROM MASCOTA AS mas JOIN MASCOTA_VALOR AS masval ON (mas.MASCOTA_ID=masval.MASCOTAS_MASCOTA_ID)" +
                "JOIN VALOR AS val ON (masval.VALORES_VALOR_ID=val.VALOR_ID)" +
                "JOIN CARACTERISTICA AS car ON (val.CARACTERISTICA_ID=car.CARACTERISTICA_ID)" +
                "WHERE mas.ESPECIE_ID = "+especie_id)

    for row in cur.fetchall():
        features_dict[row[0]] = []
    
    return features_dict

def query_mascotas_especie(especie_id):
    cur = conn.cursor()

    # Mascotas
    cur.execute("SELECT mas.MASCOTA_ID, val.VALOR_ID, val.NOMBRE, car.NOMBRE " +
                "FROM MASCOTA AS mas JOIN MASCOTA_VALOR AS masval ON (mas.MASCOTA_ID=masval.MASCOTAS_MASCOTA_ID) " +
                "JOIN VALOR AS val ON (masval.VALORES_VALOR_ID=val.VALOR_ID) " +
                "JOIN CARACTERISTICA AS car ON (val.CARACTERISTICA_ID=car.CARACTERISTICA_ID) " +
                "WHERE mas.ESPECIE_ID = "+especie_id)
    return cur.fetchall()

def format_mascotas_to_dataFrame(especie_id):

    data_train = create_features_dict(especie_id)

    mascotas_list = query_mascotas_especie(especie_id)
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
                    # print(lenArrays, " -- ", len(data_train[columna]))
                    # print("Completando ",columna,"...")
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

    for col in data_train.keys():
        print(col,": ",len(data_train[col]))

    return pandas.DataFrame.from_dict(data_train)

# Conexion con derby
conn = drda.connect(host='localhost', database='traxpet-db', port=28001)

especie_id = "1"

data_frame = format_mascotas_to_dataFrame(especie_id)

print(data_frame)