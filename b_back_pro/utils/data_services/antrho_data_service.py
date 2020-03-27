from pathlib import Path
import pandas as pd


def get_height_from_exp_file(participant_obj):
    data = get_anthropometric_data_sheet()
    return data['height'].iloc[int(participant_obj.part_nb)]


def get_weight_from_exp_file(participant_obj):
    data = get_anthropometric_data_sheet()
    return data['weight'].iloc[int(participant_obj.part_nb)]


def get_leg_weight_from_exp_file(participant_obj):
    data = get_anthropometric_data_sheet()
    return data['Tcorrection'].iloc[int(participant_obj.part_nb)]


def get_anthropometric_data_sheet():
    file_of_interest = Path('C:\\HealthTrackHome\\DataDir\\anthropometricsDataDir\\codingTableForAnthropometric.xls')
    data = pd.read_excel(file_of_interest, sheet_name='participants',
                         encoding='utf8',
                         header=0,
                         nrows=43,
                         usecols=['weight', 'height', 'Tcorrection']
                         )
    return data
