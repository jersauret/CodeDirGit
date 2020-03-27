from pathlib import Path

from b_back_pro.utils.data_crafting_tools.pre_processing_of_data import cutting_beg_and_end_from_position, \
    cutting_beg_and_end_base_on_GRF
from b_back_pro.utils.data_services.antrho_data_service import import_biomechanics_as_df, \
    import_calibration_as_df


# a run toute seule pour faire transfert exp et csv to json.

def csv_to_json():
    path_to_folder_of_file = Path('C:/Users/a766560/OneDrive - Atos/Desktop/perso/these/calib')
    file_list = list(path_to_folder_of_file.glob('*.txt'))
    for file_name_as_path in file_list:
        muscle_and_velocity_asm1v1 = str(file_name_as_path.stem[3:7])
        table_mv_desirable = ["M1V1", "M2V1", "M1V4", "M2V4"]
        for MV in table_mv_desirable:
            if MV == muscle_and_velocity_asm1v1:
                velocity_as_1 = int(file_name_as_path.stem[6:7])
                raw_data = import_calibration_as_df(file_name_as_path)
                if velocity_as_1 < 4:
                    cut_data = cutting_beg_and_end_from_position(raw_data, muscle_and_velocity_asm1v1)
                else:
                    cut_data = raw_data

                base_new_path = Path("C:\\HealthTrackHome\\DataDir\\calib_json")
                new_file_name = Path(file_name_as_path.stem + ".json")
                new_file_path = base_new_path.joinpath(new_file_name)
                calib_data_as_json = cut_data.to_json(new_file_path, orient="columns", indent=2)


def exp_to_json():
    path_to_folder_of_file = Path('C:/Users/a766560/OneDrive - Atos/Desktop/perso/these/biomecanicsflat')
    file_list = list(path_to_folder_of_file.glob('*.exp'))
    for file_name_as_path in file_list:
        complete_data = import_biomechanics_as_df(file_name_as_path)
        cut_data = cutting_beg_and_end_base_on_GRF(complete_data)
        base_new_path = Path("C:\\HealthTrackHome\\DataDir\\bio_json")
        new_file_name = Path(file_name_as_path.stem + ".json")
        new_file_path = base_new_path.joinpath(new_file_name)
        bio_data_as_json = cut_data.to_json(new_file_path, orient='columns', indent=2)


csv_to_json()
exp_to_json()
#
