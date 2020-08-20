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
    _data = np.array(data)
    scaler = joblib.load(PATH + '\scaler')
    _data = scaler.fit_transform(_data)
    return np.reshape(_data, (1, 4, 1))


#
#
#
def check_range(x, a, b):
    return a <= x < b


#
#
#
def fix_output(output):
    res = {
        # (-1, 0.165): 'Unsuitable',
        # (0.165, 0.495): 'Moderately suitable',
        # (0.495, 0.825): 'Suitable',
        # (0.825, 1.5): 'Best suitability',
        (-1, 0.165): 0,
        (0.165, 0.495): 1,
        (0.495, 0.825): 2,
        (0.825, 1.5): 3,
    }
    fixed_output = []
    # fix output
    for i in output:
        for a, b in res:
            if check_range(i, a, b):
                fixed_output.append(res[(a, b)])
    return fixed_output


#
#   Make a prediction about Land Suitability
#   Using the given data
#
def make_prediction(model, data):
    # Precipitation  Relative  Humidity  Pressure  Temp_avg
    _input = prepare_data([data])
    results = model.predict(_input)
    results = fix_output(results)
    return results
