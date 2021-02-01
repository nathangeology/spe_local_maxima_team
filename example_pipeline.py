import pandas as pd


if __name__ == '__main__':
    ## 1 -- Load semi-cleaned up dataset
    dataset = pd.read_csv('processed_datav1.csv')
    basic_stats = dataset.describe()
    info = dataset.info()
    # 2 -- Explore data, what do have and how much do we have?
    print('here')
