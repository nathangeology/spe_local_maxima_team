from file_input.load_las import get_logs_collection, get_log_names
import pandas as pd
import os
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
        'LS_PHI': ['PORZ_LS', 'DPHI_LS', 'SPHI_LS', 'TPHI_LS'],
        'DPHIL': ['DPOR_LS', 'DPHZLS', 'TNPH_LS', 'DPHILS'],
        'NPHIL': ['CNC_LS', 'NPORLS', 'NPHILS', 'NPHI_LS'],
        'GR_TH': ['THOR', 'GRT'],
        'GR_K': ['POTA'],
        'RHOB': ['RHOB_SLDT', 'ZDEN', 'RHOB'],
        'PEF': ['PEFL', 'PEFZ', 'PEF', 'PE'],
    }
    if os.path.isfile('dataset.csv'):
        dataset_iterator = pd.read_csv('dataset.csv', chunksize=10000, iterator=True)
    else:
        col_names = get_log_names()
        collection = get_logs_collection(col_list=col_names)
        for x in collection:
            print('next')
        dataset_iterator = pd.read_csv('dataset.csv', chunksize=10000, iterator=True)
    for chunk in dataset_iterator:
        print('here')
    print('here')

