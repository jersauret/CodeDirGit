import json
import os

#
# from google.cloud import firestore

from b_back_pro.a_part.participant import Participant


def push_participant_object(participant_obj: Participant, calibration=True, biomechanics=True, anthropometric=True,
                            hamstrings=True, quadriceps=True):
    print(participant_obj.part_id)
    list_muscles = []
    if hamstrings:
        list_muscles.append('Hamstrings')
    if quadriceps:
        list_muscles.append('Quadriceps')

    # push_calibration_object(participant_obj,  list_muscles)
    # push_biomechanics_object(participant_obj)
    # push_anthropometry(participant_obj)

#
# def push_calibration_object(participant_obj: Participant, list_muscles):
#     datacat_part_ref_collection = get_db(participant_obj, 'Calibration')
#     for muscle in list_muscles:
#         muscle_ref_document = datacat_part_ref_collection.document(muscle)
#         for velocity in ['V1']:
#             velocity_ref_collection = muscle_ref_document.collection(velocity)
#             for repetition in calibration_repetition_names_list:
#                 repetition_ref_document = velocity_ref_collection.document(repetition)
#                 print(muscle, velocity, repetition)
#                 # fin de boucle
#
#                 data_part_velocity_muscle_rep = \
#                     participant_obj.muscle_actions[muscle].repetitions_managers[velocity].calibration_repetition[
#                         repetition]
#                 json_file_part_velocity_muscle_rep = json.loads((
#                     data_part_velocity_muscle_rep.complete_data_from_import.to_json(
#                         orient='index')))  # oreint = index regroupe par index, columns regroupe par columne
#                 repetition_ref_document.set(json_file_part_velocity_muscle_rep)
#
#
# def push_anthropometry(participant_obj: Participant):
#     datacat_part_ref_collection = get_db(participant_obj, 'Anthropometrics')
#     anthropometric_json_file = json.loads(
#         json.dumps(participant_obj.anthropometric, default=lambda o: o.__dict__, indent=4))
#     heightweight_part_ref_collection_document = datacat_part_ref_collection.document(u'heightandweight')
#     heightweight_part_ref_collection_document.set(anthropometric_json_file)
#     pass
#
#
# def push_biomechanics_object(participant_obj: Participant):
#     datacat_part_ref_collection = get_db(participant_obj, 'Biomechanics')
#     for task in biomechanics_tasks_and_rep_manager_list:
#         task_part_ref_document = datacat_part_ref_collection.document(task)
#         for repetition_manager in biomechanics_tasks_and_rep_manager_list:
#             repm_task_part_ref_collection = task_part_ref_document.collection(repetition_manager)
#             for repetition in biomechanics_repetition_names_list:
#                 print(task, repetition_manager, repetition)
#                 rep_repm_task_part_ref_document = repm_task_part_ref_collection.document(repetition)
#                 # fin de boucle
#                 print("repmaner2", type( repetition_manager))
#                 data_part_task_manager_rep = participant_obj.biomechanics_tasks[task].biomechanics_repetitions_manager[
#                     repetition_manager].biomechanics_repetitions[repetition]
#                 json_part_task_manager_rep_data_grf_y = json.loads((data_part_task_manager_rep.data_grf_y.to_json(
#                     orient='index')))  # oreint = index regroupe par index, columns regroupe par columne
#                 rep_repm_task_part_ref_document.set(json_part_task_manager_rep_data_grf_y)
#
#
# def get_db(participant_obj: Participant, typededonnees):
#     part_id = participant_obj.part_id
#     credential_path = 'C:\\HealthTrackHome\\EnvironmentDir\\credentials_google\\healthtrack.json'
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
#     db = firestore.Client()
#     part_ref_collection = db.collection(u'Participants')
#     part_ref_document = part_ref_collection.document(part_id)
#     datacat_part_ref_collection = part_ref_document.collection(typededonnees)
#     return datacat_part_ref_collection
