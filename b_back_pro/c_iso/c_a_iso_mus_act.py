from b_back_pro.utils.data_qualifiers.obj_names_lists import mus_iso_dict, mus_name_dict
from .c_b_iso_rep_man import IsoCalRepMan


class IsoMusAct(object):

    def __init__(self, part_id, mus_iso_name):
        self.part_id = part_id
        self.mus_iso_name = mus_iso_name
        self.iso_cal_repman_list = {}
        self.get_iso_cal_repman_list()
        self.mus_res_iso = self.get_iso_mus_res()

    def get_iso_cal_repman_list(self):
        print("je crée l'objet IsoCalRepMan")
        print("de type", self.mus_iso_name)
        self.iso_cal_repman_list[self.mus_iso_name] = IsoCalRepMan(self.part_id, self.mus_iso_name)

    def get_iso_mus_res(self):
        temp = {}
        print("je fais les moyennes sur les répétitions de:", self.mus_iso_name)
        print(self.iso_cal_repman_list.values())
        objet_rep_man = self.iso_cal_repman_list[self.mus_iso_name]
        print("objet_rep_man", objet_rep_man.rep_man_iso_values)
        temp[self.mus_iso_name] = objet_rep_man.rep_man_iso_values
        print("temp", temp)
        return temp
# iso_mean_peak_emg_ago_mh = mean(d['peak_emg_ago_mh'] for d in list_lists_reps.values() if d)
