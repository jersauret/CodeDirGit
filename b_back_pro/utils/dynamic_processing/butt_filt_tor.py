from matplotlib import pyplot
from scipy import signal


def filter_creation_butter_low_pass_torque(order=4, freq=3):
    fn = 1000
    [a_low_pass_tor, b_low_pass_tor] = signal.butter(order, freq / fn, 'low')  # make sure the one for bio is the same
    return a_low_pass_tor, b_low_pass_tor


def filter_implementation_butter_low_pass_torque(torque, order=4, freq=3):
    a_low_pass_tor, b_low_pass_tor = filter_creation_butter_low_pass_torque(order, freq)
    torque_low_passed = signal.filtfilt(a_low_pass_tor, b_low_pass_tor, torque)
    return torque_low_passed

