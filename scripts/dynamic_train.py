import math
import numpy as np
import pandas
from catboost import CatBoostClassifier, Pool, metrics, cv
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split
from dynamic_data import DynamicData

def get_info_labels():
    print('Labels: {}'.format(set(y)))
    print('Zero count = {}, One count = {}'.format(len(y) - sum(y), sum(y)))

dynamicData = DynamicData("2")

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

model.fit(
    X_train, y_train,
    cat_features=cat_features,
    eval_set=(X_validation, y_validation),
    # verbose=False
)

print('Model is fitted: ' + str(model.is_fitted()))
print('Model params:')
print(model.get_params())

model.save_model("../server/models/nuevo_modelo.cbm",
                format="cbm",
                export_parameters=None,
                pool=None)
