from tensorflow import keras
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

PATH = 'D:\works\master-2\smart_green\sg_dashboard\scripts\lstm_model'


#
#   Prepare data before feeding it to model
#   - Scale data to the range of 0...1
#   - Reshape data to a 3D arrray
#
def prepare_data(data):
    print('---------------------\n')
    print(f'{data=}')
    print('---------------------\n')
    _data = np.array(data)
    # scaler = joblib.load(PATH + '\scaler')
    # _data = scaler.fit_transform(_data)
    return np.reshape(_data, (1, 4, 1))


#
#
#
def fix_output(output):
    res = ['Unsuitable', 'Moderately suitable', 'Suitable', 'Best suitability']
    return np.argmax(output, axis=1)


#
#   Make a prediction about Land Suitability
#   Using the given data
#
def make_prediction(model, data):
    # Precipitation  Relative  Humidity  Pressure  Temp_avg
    _input = prepare_data([data])
    results = model.predict(_input)
    print('---------------------\n')
    print(results)
    print('---------------------\n')
    results = fix_output(results)
    print(results)
    print('---------------------\n')
    return results
