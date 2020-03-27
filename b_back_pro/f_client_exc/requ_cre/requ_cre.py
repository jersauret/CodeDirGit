from b_back_pro.a_part.participant import Participant
from b_back_pro.utils.data_qualifiers.requ_lists import participant_as_nb_list, \
    predicted_variable_from_lists,predictor_variable_list_from_lists


class RequestObject:

    def __init__(self):
        dict_var_names_and_val= {}
        for cur_part_nb in participant_as_nb_list:
            cur_part_obj = Participant(cur_part_nb)
            preded_var_name = predicted_variable_from_lists
            dict_var_names_and_val[cur_part_nb]['predicted']=preded_var_name
            for current_variable_requested in predictor_variable_list_from_lists:
                pass
