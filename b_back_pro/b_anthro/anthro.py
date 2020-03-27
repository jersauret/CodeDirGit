from b_back_pro.utils.data_services.antrho_data_service import *


class Anthropometric:
    def __init__(self, participant_obj):
        self.height = int(get_height_from_exp_file(participant_obj))
        self.weight = int(get_weight_from_exp_file(participant_obj))
        self.legweight = int (get_leg_weight_from_exp_file(participant_obj))
        print("la taille de la participante" , self.height)
        print("le poids de la participante" , self.weight)
        print("le poids de sa jambe" , self.legweight)