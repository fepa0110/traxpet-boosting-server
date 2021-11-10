from perros_predictions import PerrosPrediction
from mascota_formatter import MascotaFormatter

perrosPredictions = PerrosPrediction()
mascotaFormatter = MascotaFormatter()

data = dict({
    "mascota": {
        "nombre": "",
        "especie": {
            "nombre": "Perro"
        },
        "valores": [
            {
                "nombre": "Adulto",
                "caracteristica": {
                    "nombre": "Edad"
                }
            },
            {
                "nombre": "Chico",
                "caracteristica": {
                    "nombre": "Tamaño"
                }
            },
            {
                "nombre": "Macho",
                "caracteristica": {
                    "nombre": "Sexo"
                }
            },
            {
                "nombre": "Liso",
                "caracteristica": {
                    "nombre": "Patron de pelaje"
                }
            },
            {
                "nombre": "Blanco",
                "caracteristica": {
                    "nombre": "Color de pelaje 1"
                }
            },
            {
                "nombre": "Marron oscuro",
                "caracteristica": {
                    "nombre": "Color de ojos"
                }
            },
            {
                "nombre": "Corto",
                "caracteristica": {
                    "nombre": "Largo de hocico"
                }
            },
            {
                "nombre": "Largo",
                "caracteristica": {
                    "nombre": "Largo de cola"
                }
            },
            {
                "nombre": "Cortadas",
                "caracteristica": {
                    "nombre": "Largo de orejas"
                }
            },
            {
                "nombre": "Caidas",
                "caracteristica": {
                    "nombre": "Tipo de orejas"
                }
            }
        ]
    }
})

dictionary = perrosPredictions.get_predict_data(data['mascota']["valores"])
list_pred = mascotaFormatter.parse_to_json(dictionary)

print(list_pred)
