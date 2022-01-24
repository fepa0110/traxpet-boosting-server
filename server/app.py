# import main Flask class and request object
from flask import Flask, request
from perros_predictions import PerrosPrediction
from dynamic_predictions import DynamicPredictions
from mascota_formatter import MascotaFormatter
from especie_service import EspecieService
from flask_cors import CORS, cross_origin

# create the Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/predict', methods=['POST'])
@cross_origin()
def json_example():
    request_data = request.get_json()
    
    mascotaFormatter = MascotaFormatter()
    especieService = EspecieService()

    mascota_data = request_data["mascota"]
    especie_name = mascota_data['especie']['nombre']

    especie_id = especieService.get_especie_id(especie_name)

    if(especie_id != None):
        dynamicPredictions = DynamicPredictions(especie_id)
        dictionary = dynamicPredictions.get_predict_data_from_json(
            mascota_data["valores"])
        if(type(dictionary) == type(dict())):
            data = mascotaFormatter.parse_to_json(dictionary)
        else:
            data = "No hay modelos para la especie {}".format(especie_name)
    else:
        data = "No existe la especie {}".format(especie_name)
    # return especie
    return data

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(host="192.168.0.100", debug=True, port=5000)
