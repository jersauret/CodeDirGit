from pathlib import Path

import pandas as pd

from b_back_pro.d_dyn.c_d_dyn_ant_ago_mus_grp import DynAgoMusGrp, DynAntMusGrp
from b_back_pro.utils.data_qualifiers.class_emg import classify_raw_emg_from_vl_etc_to_ago_medial, \
    get_str_for_m_v_type_repnb_dir


def access_json(Fileurl_part_mus_vel_rep):
    base_new_path = Path("C:\\HealthTrackHome\\DataDir\\calib_json")
    new_file_name = Path(Fileurl_part_mus_vel_rep + '.json')
    print("pour cette répétition je charge le fichier:", new_file_name)
    path_folder_cal_file = base_new_path.joinpath(new_file_name)
    return pd.read_json(path_folder_cal_file)


class DynCalRep:

    def __init__(self, Fileurl_part_mus_vel_rep):
        self.ago_mus_grp = None
        self.ant_mus_grp = None
        self.c_res_rep_dict = {}
        self.ago_mus_txt = None
        self.mus_vel_m1v1 = None
        self.aty_txt = None
        self.fex_txt = None
        self.vel_txt = None
        complete_data_from_json = access_json(Fileurl_part_mus_vel_rep)
        self.mus_vel_m1v1 = str(Fileurl_part_mus_vel_rep)[3:7]
        [self.ago_mus_txt, self.vel_txt, self.aty_txt, self.fex_txt] = get_str_for_m_v_type_repnb_dir(
            self.mus_vel_m1v1)
        print("le muscle agoniste est", self.ago_mus_txt)
        print("la velocité est", self.vel_txt)

        [ago_raw_emg_mh, ago_raw_emg_lh, ant_raw_emg_mh, ant_raw_emg_lh] = classify_raw_emg_from_vl_etc_to_ago_medial(
            self.mus_vel_m1v1,
            complete_data_from_json['VL'],
            complete_data_from_json['VM'],
            complete_data_from_json['BF'],
            complete_data_from_json['ST'])

        self.ago_mus_grp = DynAgoMusGrp(ago_raw_emg_mh, ago_raw_emg_lh, self.vel_txt)
        self.ant_mus_grp = DynAntMusGrp(ant_raw_emg_mh, ant_raw_emg_lh, self.vel_txt)

        self.c_dyn_res_rep_dict = {
            "peak_emg_ago_mh": self.ago_mus_grp.mmh.results["raw_emg"],
            "peak_emg_ago_lh": self.ago_mus_grp.lmh.results["raw_emg"]
        }

