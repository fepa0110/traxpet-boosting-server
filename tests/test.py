# from .. import CaracteristicasService
from services import *

caracteristicaService = CaracteristicasService()

caracteristicas = caracteristicaService.get_caracteristicas(2)
caracteristicasDict = dict({"Mascota":[0]})
for caracteristica in caracteristicas:
    caracteristicasDict.update({caracteristica[0]:[""]})

print(caracteristicasDict)

