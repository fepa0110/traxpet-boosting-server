from pandas.core.algorithms import mode
from perros_predictions import PerrosPrediction
from mascota_formatter import MascotaFormatter
from model_service import ModelService
from mascotas_entrenadas_service import MascotasEntrenadasService
import pandas

mascotasEntrenadasService = MascotasEntrenadasService()

mascotasEntrenadas = mascotasEntrenadasService.get_by_model_id(1)

orden_list = list()
mascotas_ids = list()
for index in range(len(mascotasEntrenadas)):
    orden_list.append(mascotasEntrenadas[index][0])
    mascotas_ids.append(mascotasEntrenadas[index][1])

mascotas_ids_series = pandas.Series(mascotas_ids, orden_list)
print(type(mascotas_ids_series))

prediction = [[0.00052,52565,23546], [0.0058772,25635,245]]
prediction = prediction[0]
# mascotas_ids = mascotas_ids_series
# print(mascotas_ids[1])
mascotas_similares = dict()

for prediction_index in range(len(prediction)):
    mascotas_similares[str(mascotas_ids[prediction_index])
                        ] = prediction[prediction_index]

print(mascotas_similares)
