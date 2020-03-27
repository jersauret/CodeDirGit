import math

from scipy import stats


def torque_from_raw_to_positive(raw_torque, group):
    volt_baseline = 2.4967
    if group == 1:
        processed_signal = (raw_torque / -2) - volt_baseline
    elif group == 2:
        processed_signal = raw_torque * 2
    else:
        processed_signal = raw_torque

    plot_data(processed_signal)

    return processed_signal


def torque_from_positive_to_nm(positive_torque, group):
    # TO DO find the reason why the reading is not on baseline at the beginning
    torque_converter_mv_nm = 0.003269444444444
    if group == 1:
        tor_volts = positive_torque
    elif group == 2:
        tor_volts = positive_torque
    elif group == 3:
        tor_volts = positive_torque

        torque_nm = (tor_volts / torque_converter_mv_nm)
    return torque_nm


def correct_for_gravity(torque, Tcorrection, position):
    cpos = int
    gravcorr = math.sin(stats.mean(position) * Tcorrection)  # a revoir
    # gravcorr = (sind(mean(CPOS)). * Tcorrection);
    # torque_corrigee = torque - gravcorr
    # CITORGC = CTOR - gravcorr;
    # torqueconverter=0.003269444444444;
    # torqueconverter=0.001634722222222;
    # torinvolts=torinvolts;%-2.4967
