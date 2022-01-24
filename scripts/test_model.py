from especie_service import EspecieService
from model_service import ModelService

especie_service = EspecieService()

especie_id = especie_service.get_especie_id("Perro")

print("especie_id: ",especie_id)

model_service = ModelService()

model_filename = model_service.get_model_filename_by_especie_id(especie_id)

print(model_filename)


