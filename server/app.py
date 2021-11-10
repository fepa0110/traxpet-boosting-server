# import main Flask class and request object
from flask import Flask, request
from perros_predictions import PerrosPrediction
from mascota_formatter import MascotaFormatter

# create the Flask app
app = Flask(__name__)

@app.route('/post-example', methods=['POST'])
def json_example():
    request_data = request.get_json()
    
    perrosPrediction = PerrosPrediction()
    mascotaFormatter = MascotaFormatter()

    mascota_data = request_data["mascota"]

    dictionary = perrosPrediction.get_predict_data(mascota_data["valores"])

    data = mascotaFormatter.parse_to_json(dictionary)

    return data

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)