import pandas
import numpy as np

class MascotaFormatter:
    def __init__(self):
        pass

    def format_caracteristicas(self, valores):
        caracteristicas = dict({
            "Mascota":[0],
            "Edad":[""], 
            "Tamaño":[""], 
            "Sexo":[""], 
            "Patron de pelaje":[""],
            "Color de pelaje 1":[""],
            "Color de pelaje 2":[""], 
            "Color de pelaje 3":[""], 
            "Largo de pelaje":[""], 
            "Color de ojos":[""], 
            "Largo de hocico":[""],
            "Largo de cola":[""], 
            "Largo de orejas":[""],
            "Tipo de orejas":[""]
        })

        for valor in valores:
            caracteristicas[valor['caracteristica']['nombre']] = [valor['nombre']]
        
        return caracteristicas
    
    def format_caracteristicas_to_csv(self,caracteristicas):
        dFCaracteristicaspandas = pandas.DataFrame.from_dict(caracteristicas)
        return dFCaracteristicaspandas

    def sort_dictionary(self, dictionary):
        sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[0], reverse=True)
        return sorted_dictionary

    def get_prettify_probs(self, predictions_probs_dict):
        pretty_output = "{["
        sorted_dict = self.sort_dictionary(predictions_probs_dict)

        for index in range(len(predictions_probs_dict)):
            probabilidad = sorted_dict[index][1]*100
            pretty_output = pretty_output + \
                str('"{}":'.format(sorted_dict[index][0])
                    )+str('{0:.5f}'.format(probabilidad))
            if(index != len(sorted_dict)-1):
                pretty_output = pretty_output + ","
        pretty_output = pretty_output + "]}"

        return pretty_output


    def parse_to_json(self, predictions_probs_dict):
        def order_by_prob(n):
            return n[1]
        pretty_output = "["

        data = list(predictions_probs_dict.items())
        data.sort(key=order_by_prob, reverse=True)

        an_array = np.array(data)
        '''[{
            "id": 23,
            "probabilidad": 0.83643
        }, 
        {
            "id": 23,
            "probabilidad": 0.83643
        }]'''

        for index in range(len(an_array)):
            mascota_id = an_array[index][0]
            probabilidad_mascota = float(an_array[index][1])

            pretty_output = pretty_output + \
                '{'+ \
                    str('"id":{},'.format(mascota_id))+ \
                    str('"probabilidad": {}'.format(probabilidad_mascota))+'}'
            if(index != len(an_array)-1):
                pretty_output = pretty_output + ","

        pretty_output = pretty_output + "]"

        return pretty_output
