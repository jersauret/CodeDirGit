from b_back_pro.utils.data_qualifiers.cal_enums import get_movement_characteristics


def get_str_for_m_v_type_repnb_dir(muscle_and_velocity_asm1v1):
    if get_movement_characteristics('M1_Co_act', muscle_and_velocity_asm1v1) == 'agonist':
        muscle_as_text = 'Quadriceps'
        type_as_text = get_movement_characteristics('M1_action', muscle_and_velocity_asm1v1)
    else:
        muscle_as_text = 'Hamstrings'
        type_as_text = get_movement_characteristics('M2_action', muscle_and_velocity_asm1v1)
    velocity_as_text = str(get_movement_characteristics('Speed', muscle_and_velocity_asm1v1))
    direction_as_text = get_movement_characteristics('Direction', muscle_and_velocity_asm1v1)
    return muscle_as_text, velocity_as_text, type_as_text, direction_as_text


def classify_raw_emg_from_vl_etc_to_ago_medial(muscle_and_velocity_asm1v1, raw_vl_emg, raw_vm_emg, raw_bf_emg,
                                               raw_st_emg):
    if get_movement_characteristics('M1_Co_act', muscle_and_velocity_asm1v1) == 'agonist':

        agonist_raw_emg_medial_head = raw_vm_emg
        agonist_raw_emg_lateral_head = raw_vl_emg
        antagonist_raw_emg_medial_head = raw_st_emg
        antagonist_raw_emg_lateral_head = raw_bf_emg
    else:
        agonist_raw_emg_medial_head = raw_st_emg
        agonist_raw_emg_lateral_head = raw_bf_emg
        antagonist_raw_emg_medial_head = raw_vm_emg
        antagonist_raw_emg_lateral_head = raw_vl_emg

    return agonist_raw_emg_medial_head, agonist_raw_emg_lateral_head, antagonist_raw_emg_medial_head, antagonist_raw_emg_lateral_head
