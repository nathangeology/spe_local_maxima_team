

def get_logs_collection(folder_path='./data/', col_list=[]):
    import os
    files = os.listdir(folder_path)
    return (load_las(folder_path +x, idx, col_list) for idx, x in enumerate(files))


def get_log_names(folder_path='./data/'):
    import os
    files = os.listdir(folder_path)
    col_set = set()
    for file in files:
        cols = set(get_las_cols(folder_path + file))
        col_set = cols.union(col_set)

    return list(col_set)


def load_las(filename, counter, col_list):
    import lasio
    import numpy as np
    # Read the las file from the filename
    las = lasio.read(filename)
    df = las.df()
    df['idx'] = counter
    df['md'] = df.index
    print(counter)
    if counter == 0:
        mode = 'w'
        columns = True
    else:
        mode = 'a'
        columns = False
    for col in col_list:
        if col not in df:
            df[col] = np.nan
    df.to_csv('dataset.csv', mode=mode, index=False, header=columns)
    return df


def get_las_cols(filename):
    import lasio
    las = lasio.read(filename)
    df = las.df()
    return list(df.columns)
