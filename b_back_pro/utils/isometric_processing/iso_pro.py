import numpy
from b_back_pro.utils.isometric_processing.butt_emg_filt_iso import *


def get_iso_peak_emg_one_mus(raw_emg):
    rect_emg = (abs(raw_emg))
    low_pass_rect_emg = filter_implementation_butter_low_pass_iso_emg(rect_emg)
    max_emg_rep = numpy.amax(low_pass_rect_emg)
    return max_emg_rep

