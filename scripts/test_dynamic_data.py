from dynamic_data import DynamicData

dynamicData = DynamicData("1")

train_df = dynamicData.format_mascotas_to_dataFrame()

print(train_df)