from tensorflow import keras
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

PATH = 'D:\works\master-2\smart_green\sg_dashboard\scripts\lstm_model'


'''
    Prepare data before feeding it to model
    - convert to numpy array
    - Reshape data to a 3D arrray
'''


def prepare_data(data):
    _data = np.array(data)
    return np.reshape(_data, (1, 4, 1))


'''
   Make a prediction about Land Suitability
   Using the given data
'''


def make_prediction(model, data):
    # Precipitation  Relative  Humidity  Pressure  Temp_avg
    _input = prepare_data([data])
    results = model.predict(_input)
    results = np.argmax(results, axis=1)
    return results
