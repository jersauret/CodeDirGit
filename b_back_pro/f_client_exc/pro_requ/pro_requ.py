from b_back_pro.utils.data_qualifiers import *
from b_back_pro.a_part.participant import Participant

def get_predicted_biomec_value_list(first_participant: Participant, last_participant: Participant):
    predicted_biomec_value_list = []

    # index_predicted_variables_name = predicted_variables_names[]
    # print(index_predicted_variables_name)
    predicted_value = first_participant.task_bio['c1'].biomechanics_repetitions_manager['c1'].mean_peak_grf
    print(predicted_value)
    # predicted_biomec_value_list[index_predicted_variables_name]= predicted_value
    return predicted_biomec_value_list


def get_calibration_results(first_participant: Participant, last_participant:Participant):
    predicted_values = []
    for p in range(first_participant, last_participant):
        predicted_value_of_participant= first_participant.c1.c1.mean_peak_grf
    print(predicted_value_of_participant)


def aggregate_for_exploitation():
    np_array_dataset = []
    return np_array_dataset

# je créé une classe resultat, elle sera instanciée en un objet précis
# celui ci traite une requete client paramétrée ( quels participants ?) dans requetes_clients
# dois je passer directement
class RendusServices:

    def __init__(self, first_participant: int, last_participant: int):
        self.predictor_variables_names = predictor_variables_names
        self.predicted_variables_names = predicted_variables_names
        def entry_point_local (first_participant, last_participant):
            for participant_as_a_int in range(first_participant, last_participant):
                current_participant = Participant(participant_as_a_int)
                get_predicted_biomec_value_list(first_participant)
        # self.predictor_variables_values = get_calibration_results()
        # self.dataset_as_np_array = aggregate_for_exploitation()
        # accuracy = AccuracyCalculation(self.dataset_as_np_array)
        # logistic_regression.fit(self.predictor_variables_values, self.predicted_variables_values)

