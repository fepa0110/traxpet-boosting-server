import math
import numpy as np
import pandas
from catboost import CatBoostClassifier, Pool, metrics, cv
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split
from dynamic_data import DynamicData
from services.especie_service import EspecieService
from services.model_service import ModelService
from services.mascotas_service import MascotasService
from services.mascotas_entrenadas_service import MascotasEntrenadasService

def get_info_labels():
    print('Labels: {}'.format(set(y)))
    print('Zero count = {}, One count = {}'.format(len(y) - sum(y), sum(y)))

def entrenar_modelo(especie_id):
    especie_service = EspecieService()
    model_service = ModelService()
    mascota_service = MascotasService()
    mascotas_entrenadas_service = MascotasEntrenadasService()

    # especie_id = 1
    especie_nombre = especie_service.get_especie_nombre(especie_id)
    max_id_models = model_service.get_max_id()

    model_filename = "m_{}{}.cbm".format(especie_nombre, max_id_models+1)
    model_directory = "./models/{}".format(model_filename)

    model_antiguo = model_service.get_model_by_especie_id(especie_id)

    mascotas_modelo_nuevo = mascota_service.get_ids_mascotas_by_especie_id(especie_id)

    # Si hay mascotas entrena
    if(mascotas_modelo_nuevo != None):
        dynamicData = DynamicData(str(especie_id))

        print("Especie: {} - id: {}".format(especie_nombre,especie_id))
        print(model_filename)

        train_df = dynamicData.format_mascotas_to_dataFrame()
        print(train_df)

        y = train_df.Mascota
        X = train_df.drop('Mascota', axis=1)

        X.fillna("NaN", inplace=True)

        cat_features = list(range(0, X.shape[1]))
        print(cat_features)

        pool3 = Pool(data=X, cat_features=cat_features, label=y)

        print('Dataset shape')
        print('dataset 3:' + str(pool3.shape))

        print('\n')
        print('Column names')
        print('\ndataset 3:')
        print(pool3.get_feature_names())

        validation_df = train_df
        y_validation = train_df.Mascota
        X_validation = train_df.drop('Mascota', axis=1)
        X_validation.fillna("NaN", inplace=True)

        X_train = X
        y_train = y

        model = CatBoostClassifier(
            # task_type='GPU',
            class_names=y,
            random_seed=63,
            iterations=100,
            eval_metric=metrics.Accuracy(),
            cat_features=cat_features,
            one_hot_max_size=7,
            depth=6,
            loss_function='MultiClass'
        )

        # model.fit(
        #     X_train, y_train,
        #     cat_features=cat_features,
        #     eval_set=(X_validation, y_validation),
        #     # verbose=False
        # )

        print('Model is fitted: ' + str(model.is_fitted()))
        print('Model params:')
        print(model.get_params())

        # model.save_model(model_directory,
        #                 format="cbm",
        #                 export_parameters=None,
        #                 pool=None)
        
        with open(model_directory, "w") as archivo:
            archivo.write("dsajfasljksfljkalkfjasklfjaklsjfklasjfkljflkjadjilalueausesabuileasbueilaseblasu")

        model_nuevo_id = max_id_models+1
        model_service.create_model(model_nuevo_id,model_filename,especie_id)
        max_id_mascotas_entrenadas = mascotas_entrenadas_service.get_max_id()+1
        orden = 1

        print("Mascotas nuevas: {}".format(len(mascotas_modelo_nuevo)))
        for mascota in mascotas_modelo_nuevo:
            mascota_id = mascota[0]
            mascotas_entrenadas_service.create_mascota_entrenada(
                max_id_mascotas_entrenadas,orden,mascota_id, model_nuevo_id)
            max_id_mascotas_entrenadas = max_id_mascotas_entrenadas+1
            orden = orden+1

        if(model_antiguo != None):
            model_service.deshabilitar_modelo_id(model_antiguo[0])
            
def entrenar_todas_especies():
    especie_service = EspecieService()
    all_especies = especie_service.get_especies_activas()
    
    print(all_especies)
    for especie in all_especies:
        entrenar_modelo(especie[0])