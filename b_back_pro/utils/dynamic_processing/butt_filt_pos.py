from scipy import signal


def filter_creation_butter_low_pass_position(order=4, freq=3):
    fn = 1000
    [a_low_pass_pos, b_low_pass_pos] = signal.butter(order, freq / fn, 'low')  # make sure the one for bio is the same
    return a_low_pass_pos, b_low_pass_pos


def filter_implementation_butter_low_pass_position(position, order=4, freq=3):
    a_low_pass_pos, b_low_pass_pos = filter_creation_butter_low_pass_position(order, freq)
    position_low_passed = signal.filtfilt(a_low_pass_pos, b_low_pass_pos, position)
    return position_low_passed
