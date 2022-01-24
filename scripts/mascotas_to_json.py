import pandas
import numpy
import json

data = pandas.read_csv('../data/perrosTrainAllInComplete.csv')

mascotas = data.Mascota.to_list()
data = data.drop('Mascota', axis=1)
data_dict = data.to_dict()
cant_pets = len(mascotas)
colums = data_dict.keys()

my_json = list()
json_pet = dict()
json_especie = dict()

json_valores = list()
valor = dict()

# for index in range(cant_pets):
index = 0
while(index < cant_pets):
    json_pet["nombre"] = mascotas[index]
    json_especie["nombre"] = "Perro"
    json_pet["especie"] = json_especie

    # Por cada valor
    for key in data_dict.keys():
        if(not pandas.isna(data_dict[key][index])):
            valor["nombre"] = data_dict[key][index]
            caracteristica = dict()
            caracteristica["nombre"] = key
            valor["caracteristica"] = caracteristica
            json_valores.append(valor.copy())
            valor.clear()
    json_pet["valores"] = json_valores.copy()
    json_valores.clear()
    my_json.append(json_pet.copy())
    index = index + 1

print(json.dumps(my_json, indent=3))





""" for key in data_dict:
    print(type(data_dict[key].values()))
    for value in data_dict[key].values():
        print(value) """

""" 
{
    "nombre": Mascota,
    "especie": {
        "nombre": "Perro"
    },
    "valores": [
        {
            "nombre": dict[column][index],
            "caracteristica": {
                "nombre": column
            }  
        }
    ]
}
"""
