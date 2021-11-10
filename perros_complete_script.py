import math
import numpy as np
import pandas
from catboost import CatBoostClassifier, Pool, metrics, cv
from sklearn.metrics import confusion_matrix, accuracy_score

def get_mascotas_ids():
    data_train = pandas.read_csv('data/perrosTrainAllComplete.csv')
    null_value_stats = data_train.isnull().sum(axis=0)
    null_value_stats[null_value_stats != 0]

    data_train.fillna("NaN", inplace=True)
    prepared_data_train = data_train.drop('Mascota', axis=1)

    dataset_labels = prepared_data_train.columns.to_list()

    mascotas_train_ids = data_train.Mascota
    return data_train.Mascota

def load_test_data():
    dataset_test = pandas.read_csv('./data/perrosTestComplete.csv')

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

def import_model():
    model = CatBoostClassifier().load_model(
        "models/modeldeep3ite2000lr015.cbm", format='cbm')
    
    return model

def get_predictions_dict(prediction):
    prediction = prediction[0]
    mascotas_ids = get_mascotas_ids()
    mascotas_similares = dict()

    for prediction_index in range(len(prediction)):
        mascotas_similares[str(mascotas_ids[prediction_index])] = prediction[prediction_index]

    return mascotas_similares

def sort_dictionary(dictionary):
    sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_dictionary

def get_prettify_probs(predictions_probs_dict):
    pretty_output = ""
    for item in sort_dictionary(predictions_probs_dict):
        probabilidad = item[1]*100
        pretty_output = pretty_output+str("{}\t=>\t".format(item[0]))+str("{0:.2f}%\n".format(probabilidad))

    return pretty_output

def get_predictions(pool, model):
    prediction = model.predict_proba(pool)

    predictions_dict = get_predictions_dict(prediction)
    sort_dictionary(predictions_dict)
    
    return predictions_dict

predict_pool = load_test_data()
model = import_model()

pet_pridiction = get_predictions(predict_pool,model)

print(get_prettify_probs(pet_pridiction))
