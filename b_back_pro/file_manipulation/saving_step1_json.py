from pathlib import Path


def save_step1_json(data_2_save,bio_dyn_cal_ou_iso,part_id):
    base_new_path = Path("C:\\HealthTrackHome\\DataDir\\step2\\")
    if bio_dyn_cal_ou_iso =="bio":
        lev_one_path = "bio"
    elif bio_dyn_cal_ou_iso =="dyn_cal":
        lev_one_path = "dyn_cal"
    else:
        lev_one_path = "iso_cal"
    part_nb_path=Path(part_id + lev_one_path + '.json'  )
    new_file_path= base_new_path.joinpath(lev_one_path, part_nb_path)
    print(type(data_2_save))
    data_2_save.to_json(new_file_path, orient="index", indent=4)
