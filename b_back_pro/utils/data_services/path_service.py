# cette classe est un service permettant d'aller dans le(s) bon(s) répertoires
# et de récupérer les dataFrames des .txt ou .exp ou anthropometrics.
# En input : N° Participant,
#

import os
from pathlib import Path

source_path_base = Path('C:\\HealthTrackHome\\DataDir\\calibrationsDataDir')

def get_calibration_repetition_path(participant_obj, muscle_mov_of_int, vel_of_int, rep_of_int):
    part_id = participant_obj.part_id

    if muscle_mov_of_int == 1:
        muscle_id = ['M1']
    else:
        muscle_id = ['M2']

    if vel_of_int == 1:
        vel_id = ['V1']
    elif vel_of_int == 2:
        vel_id = ['V2']
    else:
        vel_id = ['V3']

    if rep_of_int == 1:
        rep_id = ['R1']
    elif rep_of_int == 2:
        rep_id = ['R2']
    else:
        rep_id = ['R3']

    return source_path_base.joinpath(*part_id, *muscle_id, *vel_id, *rep_id)


def get_source_path_pre_rep_calibration(participant_obj, muscle_mov_of_int, vel_of_int):
    part_id = participant_obj.part_id

    if muscle_mov_of_int == "quadriceps":
        code_muscle_mov_of_int = ['M1']
    else:
        code_muscle_mov_of_int = ['M2']

    if vel_of_int == "V1":
        code_vel_of_int = ['V1']
    elif vel_of_int == "V2":
        code_vel_of_int = ['V2']
    else:
        code_vel_of_int = ['V3']
    filename = (code_muscle_mov_of_int[0] + " " + code_vel_of_int[0])
    return source_path_base.joinpath(*part_id, *code_muscle_mov_of_int, *code_vel_of_int)


def get_each_repetition_folder(participant_obj, muscle_mov_of_int, vel_of_int):
    # To do : a voir parce que un dataFrame est renvoyé par boucle,
    source_path_pre_rep = get_source_path_pre_rep_calibration(participant_obj.part_nb,
                                                              muscle_mov_of_int, vel_of_int)
    list_rep_dir = os.listdir(Path(source_path_pre_rep))
    for dir_rep in list_rep_dir:
        return source_path_pre_rep.joinpath(*[dir_rep])
