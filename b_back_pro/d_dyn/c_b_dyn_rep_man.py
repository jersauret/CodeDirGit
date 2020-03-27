from statistics import mean
from b_back_pro.d_dyn.c_c_dyn_rep import DynCalRep
from b_back_pro.utils.data_qualifiers.obj_names_lists import cal_rep_nam_dict


class DynCalRepMan:
    def __init__(self, Fileurl_part_mus_vel):
        self.dyn_cal_reps_list = {}
        self.iso_cal_reps_list = {}
        self.iso_mean = {}
        self.velocity = Fileurl_part_mus_vel[5:7]
        self.iso_values = {}
        for cal_rep_nam in cal_rep_nam_dict:
            can_rep_for_ind = cal_rep_nam_dict[cal_rep_nam]['index']
            Fileurl_part_mus_vel_rep = Fileurl_part_mus_vel + cal_rep_nam_dict[cal_rep_nam]["as_text"]
            self.dyn_cal_reps_list[can_rep_for_ind] = DynCalRep(Fileurl_part_mus_vel_rep)
            print("je vais traiter la repetition dynamique n°", cal_rep_nam_dict[cal_rep_nam]["code"])
        self.get_dyn_mean()

    def get_dyn_mean(self):
        list_dyn_lists_reps = {}
        for rep_nam in cal_rep_nam_dict:
            repetition_nb = cal_rep_nam_dict[rep_nam]['index']
            objet_repetition_name = self.dyn_cal_reps_list[repetition_nb]
            list_dyn_lists_reps[repetition_nb] = objet_repetition_name.c_res_rep_dict

