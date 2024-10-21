import tensorflow as tf
import pandas as pd


data = pd.read_csv('../obtencion_de_datos/coordenadas.csv')

train_data = data.sample(frac=0.8, random_state=0)
test_data = data.drop(train_data.index)

print(train_data)