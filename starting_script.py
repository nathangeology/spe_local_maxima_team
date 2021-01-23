from file_input.load_las import get_logs_collection, get_log_names
import pandas as pd
import os
import numpy as np
import pickle as pkl


if __name__ == '__main__':
    alias_dict = {
        'DTSM': ['DTSM', 'DTSM_FAST', 'DTST', 'DTSM_SLOW', 'DTM'],
        'DT': ['DTCO', 'DTCO', 'DTL', 'YDT', 'DTSH', 'DT4SR', 'DTMD', 'DT2R', 'DTLF', 'DT1R',
               'DT4S', 'XDT2', 'DTC', 'DTX', 'DT4P', 'DTLN', 'DT4PT', 'DT4PR', 'DTTS', 'DTY', 'DT1T',
               'DTRS', 'DT', 'DT1'],
        'NPHIS': ['NPHI', 'CNC', 'NPOR', 'NPHS', 'TNPH', 'TNPH_SS'],
        'GR': ['GRD', 'SGRDD', 'GR_EDTC', 'GR', 'HCGR',
               'GRD_1', 'GRN', 'HSGR', 'HSGRS', 'SGR',
               'GRC', 'GRR_R2', 'HCGRS', 'GRS'],
        'DRES': ['RT_HRLT', 'AT90', 'LLS_R2', 'AST90', 'LLD',
                 'CILD', 'RILD', 'ILD_1', 'AHT90', 'AF90', 'ILD1', 'LLD_R1', 'ILD'],
        'MRES': ['ILM', 'RLA4', 'ILM1', 'MSFL', 'RHOM', 'AF60'],
        'SRES': ['RLA1', 'AST10', 'AT10', 'AF20', 'AE10', 'SFLA'],
        'RXO': ['RXOZ_R', 'RXOZ', 'RXO8'],
        'RHO': ['QRHO_SLDT', 'DRHO', 'RHOZ'],
        'CAL': ['CALS', 'CALI_1', 'LCALR', 'HCALR', 'LCAL', 'DCAL', 'CALI_SPCS',
                'CALI', 'HCAL2R', 'HCAL', 'HCALS', 'CALX', 'CALSR', 'CAL1R'],
        'SAND_PHI': ['SPHI_SS', 'PHIX', 'DPHZ'],
        'DPHIS': ['DPHI', 'DPHI_SLDT', 'DPOR'],
        # 'LS_PHI': ['PORZ_LS', 'DPHI_LS', 'SPHI_LS', 'TPHI_LS'],
        # 'DPHIL': ['DPOR_LS', 'DPHZLS', 'TNPH_LS', 'DPHILS'],
        # 'NPHIL': ['CNC_LS', 'NPORLS', 'NPHILS', 'NPHI_LS'],
        'GR_TH': ['THOR', 'GRT'],
        'GR_K': ['POTA'],
        'RHOB': ['RHOB_SLDT', 'ZDEN', 'RHOB'],
        'PEF': ['PEFL', 'PEFZ', 'PEF', 'PE'],
        'md': ['md'],
        'idx': ['idx']
    }
    if os.path.isfile('dataset.csv'):
        dataset_iterator = pd.read_csv('dataset.csv', chunksize=10000, iterator=True)
    else:
        col_names = get_log_names()
        collection = get_logs_collection(col_list=col_names)
        for x in collection:
            print('next')
        dataset_iterator = pd.read_csv('dataset.csv', chunksize=10000, iterator=True)
    processed_chunks = []
    first = True
    for chunk in dataset_iterator:
        cols_with_data = []
        rename_dict = {}
        for col in chunk:
            num_test = pd.to_numeric(chunk[col], errors='coerce').sum()
            if num_test > 0:
                continue
            else:
                cols_with_data.append(col)
        temp_chunk = chunk[cols_with_data]
        for col in cols_with_data:
            for alias in alias_dict.keys():
                if col in alias_dict[alias]:
                    rename_dict[col] = alias
        temp_chunk.rename(columns=rename_dict, inplace=True)
        if sum(temp_chunk.columns.duplicated()) > 1:
            cols = list(set(temp_chunk.columns[temp_chunk.columns.duplicated()]))
            for col in cols:
                df = temp_chunk[col]
                temp_col = df.mean(axis=1)
                temp_chunk.drop(columns=[col], inplace=True)
                temp_chunk[col] = temp_col
            # print('here')
        for alias in alias_dict.keys():
            if alias not in temp_chunk:
                temp_chunk[alias] = np.nan
        if first:
            append = 'w'
            columns = True
            first = False
        else:
            append = 'a'
            columns = False
        drop_cols = []
        for col in temp_chunk:
            if col not in alias_dict.keys():
                drop_cols.append(col)
        output = temp_chunk.loc[~temp_chunk['DTSM'].isna()]
        output.drop(columns=drop_cols, inplace=True)
        for col in output:
            output[col] = pd.to_numeric(output[col], errors='coerce')
        if not output.empty:
            output.to_csv('processed_data.csv', mode=append, header=columns, index=False)
    print('here')

