import pandas as pd


def import_calibration_as_df(source_path_rep_with_file_name):
    importation_data_as_df = pd.read_csv(source_path_rep_with_file_name,
                                         sep='\s+',
                                         skiprows=16,
                                         index_col=0,
                                         usecols=[1, 2, 3, 4, 5, 6, 7, 8],
                                         header=0,
                                         error_bad_lines=False,
                                         skip_blank_lines=True,
                                         keep_default_na=False,
                                         na_values='.',
                                         names=['Msec', 'VL', 'VM', 'BF', 'ST', 'Torque', 'Velocity', 'Position']) \
        .dropna()
    return importation_data_as_df


def import_biomechanics_as_df(source_path_rep_with_file_name):
    cols_to_get_from_initial_exp = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    data = pd.read_table(source_path_rep_with_file_name,
                         skiprows=6,
                         header=1,
                         usecols=cols_to_get_from_initial_exp
                         )
    data.columns = [
        'HipAngleZ', 'HipAngleY', 'HipAngleX', 'KneeAngleZ', 'KneeAngleY', 'KneeAngleX', 'AnkleAngleZ', 'AnkleAngleY',
        'AnkleAngleX', 'CoMY', 'HipMomZ', 'HipMomY', 'HipMomX', 'KneeMomZ', 'KneeMomY', 'KneeMomX', 'AnkleMomZ',
        'AnkleMomY',
        'AnkleMomX', 'KneeShearForce', 'vl', 'vm', 'bf', 'st', 'GrfZ', 'GrfY', 'GrfX']

    return data
