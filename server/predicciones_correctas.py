import pandas
import numpy as np
from perros_predictions_puras import PerrosPrediction
from mascota_formatter import MascotaFormatter

dataset_testeo = pandas.read_csv('../data/perros_train_v3.csv')

perrosPrediction = PerrosPrediction()
mascotaFormatter = MascotaFormatter()

dictionary_all_predictions = perrosPrediction.get_predict_data_all()

def order_by_prob(n):
    return n[1]

contador_predicciones = 0
mascotas_incorrectas = []
for mascota_id in perrosPrediction.get_mascotas_ids():

    list_predictions = list(dictionary_all_predictions[mascota_id].items())
    list_predictions.sort(key=order_by_prob, reverse=True)

    array_predictions = np.array(list_predictions)

    if(str(array_predictions[0][0]) == str(mascota_id)):
        contador_predicciones = contador_predicciones + 1
    else:
        mascotas_incorrectas.append(mascota_id)

print("Contador mascotas correctas: ", contador_predicciones)
print("Contador mascotas incorrectas: ",len(mascotas_incorrectas))
print("Mascotas incorrectas: ",mascotas_incorrectas)
