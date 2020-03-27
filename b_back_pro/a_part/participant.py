import matplotlib.pyplot as plt
import pandas as pd

from b_back_pro.b_anthro.anthro import Anthropometric
from b_back_pro.c_iso.c_a_iso_mus_act import IsoMusAct
from b_back_pro.d_dyn.c_a_dyn_mus_act import MusAct
from b_back_pro.e_bio.b_a_task_man import BioTaskMan
from b_back_pro.utils.data_qualifiers.obj_names_lists import *
from b_back_pro.file_manipulation.saving_step1_json import save_step1_json


class Participant(object):

    def __init__(self, part_nb):
        self.part_nb = part_nb
        self.part_id = self.get_part_id_from_obj()
        print("Début du traitement du participant", part_nb, "id: ", self.part_id)
        print("Je commence l'anthro")
        # self.initialize_anthro()
        print("Je finis l'anthro, je commence l'iso")
        self.iso_cal = {}
        self.init_iso_cal()
        print("Je finis l'iso, je commence le dyn")
        self.dyn_cal = {}
        # self.init_dyn_cal()
        print("Je finis le dyn, je commence le bio")
        self.bio = {}  # c1
        # self.init_task_bio()
        print("Je finis le bio, je commence l'enregistrement en j_son")
        self.res_2_json(self.iso_cal, 'iso_cal')
        self.res_2_json(self.dyn_cal, 'dyn_cal')
        self.res_2_json(self.bio, 'bio')

    def res_2_json(self, data_as_dict, data_type):
        if data_as_dict:
            print(type(data_as_dict))
            save_step1_json(pd.DataFrame.from_dict(data_as_dict, orient="index"), data_type, self.part_id)

    def init_iso_cal(self):
        for mus_iso_name in mus_iso_dict:
            print('je fais le traitement isométrique pour:', mus_vel_dict[mus_iso_name]['muscle_as_text'])
            print("je cree l'objet IsoMusAct et itère pour remplor iso_cal[]")
            self.iso_cal[mus_iso_name] = IsoMusAct(self.part_id, mus_vel_dict[mus_iso_name]['muscle_as_text']).mus_res_iso

    def init_dyn_cal(self):
        for mus_vel_name in mus_vel_dict:
            if mus_vel_dict[mus_vel_name]["velocity_as_text"] == "V1":
                print('je fais la calib de', mus_vel_dict[mus_vel_name]['as_text'])
                fil_url_part_mus = str(self.part_id) + mus_vel_dict[mus_vel_name]['muscle_as_text']
                mus_for_ind = mus_vel_dict[mus_vel_name]["index"]
                self.dyn_cal[mus_for_ind] = MusAct(fil_url_part_mus)

    def init_task_bio(self):
        for bio_task_name in bio_task_dict:
            print("je fais la bio de:", bio_task_name)
        self.task_bio[bio_task_name] = BioTaskMan(self.part_id, bio_task_name)

    def get_part_id_from_obj(self):
        if self.part_nb < 10:
            part_id = "S0" + str(self.part_nb)
        else:
            part_id = "S" + str(self.part_nb)
        return part_id

    def initialize_anthro(self):
        self.anthropometric = Anthropometric(self)
