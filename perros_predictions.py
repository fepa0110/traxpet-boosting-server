import math
import numpy as np
import pandas
from catboost import CatBoostClassifier, Pool, metrics, cv
from mascota_formatter import MascotaFormatter

class PerrosPrediction:
    def __init__(self):
        self.model = self.import_model()
        self.mascotaFormatter = MascotaFormatter()
        self.predictPool = None

    def get_mascotas_ids(self):
        data_train = pandas.read_csv('../data/perrosTrainAllInComplete.csv')
        null_value_stats = data_train.isnull().sum(axis=0)
        null_value_stats[null_value_stats != 0]

        data_train.fillna("NaN", inplace=True)
        prepared_data_train = data_train.drop('Mascota', axis=1)

        dataset_labels = prepared_data_train.columns.to_list()

        mascotas_train_ids = data_train.Mascota
        return data_train.Mascota

    # Metodo que genera un Pool de prediccion de una mascota
    def load_test_data(self,caracteristicas):
        caracteristicas = self.mascotaFormatter.format_caracteristicas(caracteristicas)
        dataset_test = self.mascotaFormatter.format_caracteristicas_to_csv(caracteristicas)

        null_value_stats = dataset_test.isnull().sum(axis=0)
        null_value_stats[null_value_stats != 0]

        dataset_test.fillna("NaN", inplace=True)

        prepared_dataset_test = dataset_test.drop('Mascota', axis=1)

        mascotas_test_ids = dataset_test.Mascota

        categorical_features_indices = np.where(
            prepared_dataset_test.dtypes != np.float)[0]

        return Pool(data=prepared_dataset_test,
                        label=mascotas_test_ids,
                        cat_features=categorical_features_indices)

    def load_test_data_from_df(self, mascotas_dict):
        # dataset_mascota = pandas.read_csv('../data/perrosTestComplete.csv')
        dataset_mascota = self.mascotaFormatter.format_caracteristicas_to_csv(
            mascotas_dict)
        null_value_stats = dataset_mascota.isnull().sum(axis=0)
        null_value_stats[null_value_stats != 0]

        dataset_mascota.fillna("NaN", inplace=True)

        prepared_dataset_mascota = dataset_mascota.drop('Mascota', axis=1)

        mascotas_test_ids = dataset_mascota.Mascota

        categorical_features_indices = np.where(
            prepared_dataset_mascota.dtypes != np.float)[0]

        return Pool(data=prepared_dataset_mascota,
                    label=mascotas_test_ids,
                    cat_features=categorical_features_indices)

    def import_model(self):
        model_file_name = "./models/m_perros.cbm"
        model = CatBoostClassifier().load_model(
            model_file_name, format='cbm')
        
        return model

    def get_predictions_dict(self, prediction):
        prediction = prediction[0]
        mascotas_ids = self.get_mascotas_ids()
        mascotas_similares = dict()

        for prediction_index in range(len(prediction)):
            mascotas_similares[str(mascotas_ids[prediction_index])] = prediction[prediction_index]

        return mascotas_similares

    def sort_dictionary(self, dictionary):
        sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[0], reverse=True)
        return sorted_dictionary

    def get_prettify_probs(self, predictions_probs_dict):
        pretty_output = ""
        for item in self.sort_dictionary(predictions_probs_dict):
            probabilidad = item[1]*100
            pretty_output = pretty_output+str("{}\t=>\t".format(item[0]))+str("{0:.2f}%\n".format(probabilidad))

        return pretty_output

    # Predecir y parsear las predicciones obtenidas
    def get_predictions(self, pool):
        prediction = self.model.predict_proba(pool)

        predictions_dict = self.get_predictions_dict(prediction)
        self.sort_dictionary(predictions_dict)
        return predictions_dict

    def get_predict_data_from_json(self, caracteristicas):
        # Generar el pool para predecir la mascota
        predict_pool = self.load_test_data(caracteristicas)
        # self.load_test_data(caracteristicas)

        return self.get_predictions(predict_pool)

    def get_predict_data_from_df(self, mascota_df):
        predict_pool = self.load_test_data_from_df(mascota_df)
        # self.load_test_data(caracteristicas)

        return self.get_predictions(predict_pool)
