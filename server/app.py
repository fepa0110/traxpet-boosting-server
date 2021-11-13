# import main Flask class and request object
from flask import Flask, request
from perros_predictions import PerrosPrediction
from mascota_formatter import MascotaFormatter
from flask_cors import CORS, cross_origin

# create the Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/predict', methods=['POST'])
@cross_origin()
def json_example():
    request_data = request.get_json()
    
    perrosPrediction = PerrosPrediction()
    mascotaFormatter = MascotaFormatter()

    mascota_data = request_data["mascota"]

    dictionary = perrosPrediction.get_predict_data_from_json(
        mascota_data["valores"])

    data = mascotaFormatter.parse_to_json(dictionary)

    return data

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(host="192.168.0.100", debug=True, port=5000)
