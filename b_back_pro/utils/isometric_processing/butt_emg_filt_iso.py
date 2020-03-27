from matplotlib import pyplot
from scipy import signal


def filter_creation_butter_low_pass_iso_emg(order=4, freq=3):
    fn = 1000
    [a_low_pass_pos, b_low_pass_pos] = signal.butter(order, freq / fn, 'low')
    return a_low_pass_pos, b_low_pass_pos


def filter_implementation_butter_low_pass_iso_emg(signal_to_filter, order=4, freq=3):
    a_low_pass_pos, b_low_pass_pos = filter_creation_butter_low_pass_iso_emg(order, freq)
    signal_to_filter_low_passed = signal.filtfilt(a_low_pass_pos, b_low_pass_pos, signal_to_filter)

    return signal_to_filter_low_passed
