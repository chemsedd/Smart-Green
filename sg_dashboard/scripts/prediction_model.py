from tensorflow import keras
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

PATH = 'D:\works\master-2\smart_green\sg_dashboard\scripts\lstm_model'


def prepare_data(data):
    """Prepare data before feeding it to model
    - convert to numpy array
    - Reshape data to a 3D arrray

    Args:
        data (list): List that contains the input data

    Returns:
        numpy.array: A numpy array to feed to model
    """
    _data = np.array(data)
    return np.reshape(_data, (1, 4, 1))


def make_prediction(model, data):
    """Makes a prediction about Land Suitability
    Using the given data

    Args:
        model ([type]): The Deep learning model loaded from the file
        data ([type]): numpy array that contains the input data for making a prediction.

    Returns:
        int: land suitability (class affiliation)
    """
    # Precipitation  Relative  Humidity  Pressure  Temp_avg
    _input = prepare_data([data])
    results = model.predict(_input)
    results = np.argmax(results, axis=1)
    return results
