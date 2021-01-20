from file_input.load_las import get_logs_collection, get_log_names
import pandas as pd
import os
import pickle as pkl


if __name__ == '__main__':

    if os.path.isfile('dataset.csv'):
        dataset = pd.read_csv('dataset.csv')
    else:
        col_names = get_log_names()
        collection = get_logs_collection(col_list=col_names)
        for x in collection:
            print('next')
    print('here')
    dataset = pd.read_csv('dataset.csv')
