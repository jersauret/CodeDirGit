from b_back_pro.utils.isometric_processing.butt_emg_filt_iso import filter_implementation_butter_low_pass_iso_emg
import numpy as np


def filter_iso_tor(iso_tor):
    correction_voltage = 5
    correction_gravite = 0
    return filter_implementation_butter_low_pass_iso_emg(abs((iso_tor + correction_gravite + correction_voltage)))


def tor_to_nm(torque_in_v):
    facteur_mult_from_v_to_nm = 0.003269444444444

    return torque_in_v / facteur_mult_from_v_to_nm


def get_max_tor_nm(tor_nm):
    return np.amax(tor_nm)
