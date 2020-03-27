from statistics import mean

import pandas as pd

from b_back_pro.e_bio.b_b_rep import BioRep
from b_back_pro.utils.data_qualifiers.obj_names_lists import bio_rep_nam_dict
from b_back_pro.utils.dynamic_processing.butt_emg_filt_dyn import *

class BioTaskMan(object):
    def __init__(self, part_id, bio_task_name):
        self.part_id = part_id
        self.bio_task_name = bio_task_name
        self.bio_rep = {}
        self.res_list = {}
        for bio_rep_name in bio_rep_nam_dict:
            self.bio_rep[bio_rep_name] = BioRep(part_id, bio_task_name, bio_rep_name)
        self.update_values()

    def update_values(self):
        bio_rep_value_list = {}
        for bio_rep_name in bio_rep_nam_dict:
            print("dans la boucle de update value")
            bio_rep_value_list[bio_rep_name] = self.bio_rep[bio_rep_name].b_res_rep_dict
            print(bio_rep_value_list)
        # mean_peak_grf = mean(bio_rep_value_list[k] for k in bio_rep_value_list)
        mean_peak_grf = mean(d['peak_grf'] for d in bio_rep_value_list.values() if d)
        df= pd.DataFrame.from_dict(bio_rep_value_list, orient='index')
        # print(df.mean(axis=0))