# import main Flask class and request object
from flask import Flask, request
from perros_predictions import PerrosPrediction
from dynamic_predictions import DynamicPredictions
from mascota_formatter import MascotaFormatter
from services.especie_service import EspecieService
from flask_cors import CORS, cross_origin

from dynamic_train import entrenar_todas_especies
from apscheduler.schedulers.background import BackgroundScheduler

from datetime import datetime
import time
import os

HOST="localhost"
PORT=28003

# create the Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def tick():
    print('Tick! The time is: %s' % datetime.now())

def schedule_automatic_trains():
    scheduler = BackgroundScheduler()
    scheduler.add_job(entrenar_todas_especies, 'interval', minutes=10, replace_existing=True)
    scheduler.start()

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

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
        # Inicializo modulo de predicciones
        dynamicPredictions = DynamicPredictions(especie_id)

        # Solicito una prediccion pasandole los valores recibidos
        prediction = dynamicPredictions.get_predict_data_from_json(
            mascota_data["valores"])
        
        if(type(prediction) == type(dict())):
            data = mascotaFormatter.parse_to_json(prediction)
        else:
            data = "No hay modelos para la especie {}".format(especie_name)
    else:
        data = "No existe la especie {}".format(especie_name)
    # return especie
    return data

@app.route('/train', methods=['POST'])
@cross_origin()
def train_models():
    entrenar_todas_especies()
    return "Mascotas entrenadas"

# schedule_automatic_trains()

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(host=HOST, debug=True, port=PORT)
