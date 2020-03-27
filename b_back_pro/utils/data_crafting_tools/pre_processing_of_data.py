import numpy as np
from b_back_pro.utils.data_qualifiers.cal_enums import get_movement_characteristics
from b_back_pro.utils.dynamic_processing.butt_filt_pos import \
    filter_implementation_butter_low_pass_position


def cutting_beg_and_end_from_position(uncut_data_as_df, muscle_and_velocity_asm1v1):
    index_beg_rep, index_end_rep = defining_beg_and_end_from_position(uncut_data_as_df, muscle_and_velocity_asm1v1)
    print(len(uncut_data_as_df))
    print("index_beg_rep",index_beg_rep,"index_end_rep",index_end_rep)
    cut_data_as_df = uncut_data_as_df[index_beg_rep:index_end_rep]
    return cut_data_as_df


def defining_beg_and_end_from_position(uncut_data_as_df, muscle_and_velocity_asm1v1):
    uncut_position = uncut_data_as_df['Position']
    uncut_filtered_position = filter_implementation_butter_low_pass_position(uncut_position)
    index_end_of_rep_from_data = get_end_of_position(uncut_filtered_position, muscle_and_velocity_asm1v1)
    index_beg_of_rep_from_data = np.argmin(np.gradient(uncut_filtered_position[0:index_end_of_rep_from_data]))
    return index_beg_of_rep_from_data - 150, index_end_of_rep_from_data + 150


def get_end_of_position(uncut_filtered_position, muscle_and_velocity_asm1v1):
    direction_of_movement = get_movement_characteristics('Direction', muscle_and_velocity_asm1v1)
    if direction_of_movement == 'flexion':
        index_end_of_rep_from_data = np.argmax(uncut_filtered_position)
    else:
        index_end_of_rep_from_data = np.argmin(uncut_filtered_position)
    return index_end_of_rep_from_data


def defining_ground_contact_from_GRF(uncut_GRFY_as_df):
    index_of_ground_contact = 600
    return index_of_ground_contact


def cutting_beg_and_end_base_on_GRF(complete_data):
    uncut_GRFY_as_df = complete_data['GrfY']
    index_of_ground_contact = defining_ground_contact_from_GRF(uncut_GRFY_as_df)
    cut_data_as_df = complete_data[index_of_ground_contact - 500:index_of_ground_contact + 500]
    return cut_data_as_df
