from statistics import mean

import pandas as pd

from b_back_pro.c_iso.c_c_iso_rep import IsoCalRep
from b_back_pro.utils.data_qualifiers.obj_names_lists import cal_rep_nam_dict


class IsoCalRepMan:
    def __init__(self, part_id, mus_iso_name):
        self.mus_iso_name = mus_iso_name
        self.part_id = part_id
        # initialise iso_cal_reps_list
        self.iso_cal_reps_list = {}
        # create self.iso_cal_reps_list
        self.cre_iso_cal_reps_list(part_id, mus_iso_name)
        # initialise rep_man_iso_values
        self.rep_man_iso_values = {}
        # create
        # self.get_rep_man_iso_val(part_id, mus_iso_name)
        self.get_rep_man_iso_val_df(part_id, mus_iso_name)

    def cre_iso_cal_reps_list(self, part_id, mus_iso_name):
        temp = {}
        for cal_rep_nam in cal_rep_nam_dict:
            print("je vais traiter la repetition isometrique n°", cal_rep_nam_dict[cal_rep_nam]["code"])
            print("je crée l'objet IsoCalRep")
            temp[cal_rep_nam] = IsoCalRep(part_id, mus_iso_name, cal_rep_nam_dict[cal_rep_nam]["as_text"])
        self.iso_cal_reps_list = temp

    def get_rep_man_iso_val(self, part_id, mus_iso_name):  # velocity of form "V4"
        temp = {}
        for cal_rep_nam in cal_rep_nam_dict:
            objet_repetition_name = self.iso_cal_reps_list[cal_rep_nam]
            temp[cal_rep_nam] = objet_repetition_name.c_iso_res_rep_df
        print(temp)

        iso_mean_max_emg_ago_mh = mean(d['max_emg_ago_mh_rep'] for d in temp.values() if d)
        iso_mean_max_emg_ago_lh = mean(d['max_emg_ago_lh_rep'] for d in temp.values() if d)
        iso_mean_max_emg_ago = (iso_mean_max_emg_ago_lh + iso_mean_max_emg_ago_mh)
        iso_mean_max_tor = mean(d['max_tor'] for d in temp.values() if d)
        iso_values = {"ago_iso_mean_emg_mh": iso_mean_max_emg_ago_mh,
                      "ago_iso_mean_emg_lh": iso_mean_max_emg_ago_lh,
                      "ago_iso_mean_emg": iso_mean_max_emg_ago,
                      "ago_iso_mean_tor": iso_mean_max_tor
                      }
        self.rep_man_iso_values = iso_values

    def get_rep_man_iso_val_df(self, part_id, mus_iso_name):  # velocity of form "V4"
        col_names=self.iso_cal_reps_list['r1'].c_iso_res_rep_df.columns

        print(col_names)
        new_df = pd.DataFrame(columns=col_names)
        print(new_df)
        for cal_rep_nam in cal_rep_nam_dict:
            print(type(new_df))
            objet_repetition_name = self.iso_cal_reps_list[cal_rep_nam]
            new_df.append(objet_repetition_name.c_iso_res_rep_df)

        print("new_df",new_df)