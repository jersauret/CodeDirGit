from pathlib import Path
import pandas as pd
from b_back_pro.utils.isometric_processing.iso_tor_pro import filter_iso_tor, tor_to_nm, get_max_tor_nm
from matplotlib.pyplot import plot as plt
from b_back_pro.c_iso.c_d_iso_ant_ago_mus_grp import IsoAgoMusGrp, IsoAntMusGrp
from b_back_pro.utils.data_qualifiers.class_emg import classify_raw_emg_from_vl_etc_to_ago_medial, \
    get_str_for_m_v_type_repnb_dir


class IsoCalRep:
    def __init__(self, part_id, mus_iso_name, cal_rep_nam):
        self.fil_name_no_ext = str(part_id + mus_iso_name + "V4" + cal_rep_nam)
        self.part_id = part_id
        self.mus_iso_name = mus_iso_name
        self.cal_rep_nam = cal_rep_nam
        self.c_iso_res_rep_dict = {}
        self.mus_vel_m1v1 = str(mus_iso_name + "V4")
        full_data_from_json = self.read_json()
        self.iso_max_tor = self.get_max_tor(full_data_from_json['Torque'])
        [self.ago_mus_txt, self.vel_txt, self.aty_txt, self.fex_txt] = get_str_for_m_v_type_repnb_dir(
            self.mus_vel_m1v1)
        print("le muscle agoniste est", self.ago_mus_txt)
        print("la velocité est", self.vel_txt)

        [ago_raw_emg_mh, ago_raw_emg_lh, ant_raw_emg_mh, ant_raw_emg_lh] = classify_raw_emg_from_vl_etc_to_ago_medial(
            self.mus_vel_m1v1,
            full_data_from_json['VL'],
            full_data_from_json['VM'],
            full_data_from_json['BF'],
            full_data_from_json['ST'])

        self.ago_mus_grp = IsoAgoMusGrp(ago_raw_emg_mh, ago_raw_emg_lh, self.vel_txt)
        self.ant_mus_grp = IsoAntMusGrp(ant_raw_emg_mh, ant_raw_emg_lh, self.vel_txt)
        # initialize list res
        self.c_iso_res_rep_df = pd.DataFrame
        # start rec of res
        self.cre_iso_res_rep_df()

    def cre_iso_res_rep_df(self):
        self.c_iso_res_rep_df = pd.DataFrame({
            "max_emg_ago_mh_rep": self.ago_mus_grp.mmh.results_df["max_emg"],
            "max_emg_ago_lh_rep": self.ago_mus_grp.lmh.results_df["max_emg"],
            "max_tor": self.iso_max_tor
        })

    def read_json(self):
        base_new_path = Path("C:\\HealthTrackHome\\DataDir\\calib_json")
        new_file_name = Path(self.fil_name_no_ext + '.json')
        print("pour cette répétition je charge le fichier:", new_file_name)
        path_folder_cal_file = base_new_path.joinpath(new_file_name)
        return pd.read_json(path_folder_cal_file)

    def get_max_tor(self, iso_tor):
        filt_iso_tor = filter_iso_tor(iso_tor)
        nm_iso_tor = tor_to_nm(filt_iso_tor)
        max_iso_tot = get_max_tor_nm(nm_iso_tor)
        return max_iso_tot
