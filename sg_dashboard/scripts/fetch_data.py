import pandas as pd


# Get Temperature data from excel file
def get_temp_data(path):
    return pd.read_excel(path)
