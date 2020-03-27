from statistics import mean

from .c_b_dyn_rep_man import DynCalRepMan
from b_back_pro.utils.data_qualifiers.obj_names_lists import mus_vel_dict, mus_name_dict


class MusAct(object):

    def __init__(self, Fileurl_part_mus):
        self.cal_repman_list = {}
        get_cal_repman_list(self, Fileurl_part_mus)
        self.mus_act_res_iso = get_mus_act_res(self)


def get_cal_repman_list(self, Fileurl_part_mus):
    for mus_act_vel in mus_vel_dict:
        print("je m'occupe de muscle et velocity ", mus_vel_dict[mus_act_vel]["as_text"])
        mus_act_vel_ind = mus_vel_dict[mus_act_vel]['index']
        print("mus_act_vel_dict[mus_act_vel][vel]", mus_vel_dict[mus_act_vel]["velocity_as_text"])
        Fileurl_part_mus_vel = Fileurl_part_mus + mus_vel_dict[mus_act_vel]["velocity_as_text"]
        self.cal_repman_list[mus_act_vel_ind] = DynCalRepMan(Fileurl_part_mus_vel)


def get_mus_act_res(self):
    mus_act_res_temp = {}
    for mus_vel_name in mus_vel_dict:
        mus_vel = mus_vel_name[0:4]
        print("je recupere les données de muscle action:", mus_vel)
        mus_act_for_ind = mus_vel_dict[mus_vel_name]['index']
        objet_rep_man = self.cal_repman_list[mus_act_for_ind]
        print("objet_rep_man", objet_rep_man)
        mus_act_res_temp[mus_vel] = objet_rep_man.iso_values

    print("mus_act_res_temp", mus_act_res_temp)
    return mus_act_res_temp
    # iso_mean_peak_emg_ago_mh = mean(d['peak_emg_ago_mh'] for d in list_lists_reps.values() if d)
