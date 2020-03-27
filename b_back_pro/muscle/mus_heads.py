import pandas as pd

from b_back_pro.utils.isometric_processing.iso_pro import get_iso_peak_emg_one_mus


def get_iso_res(raw_emg, vel_txt):

    results_dict = {
        "max_emg": get_iso_peak_emg_one_mus(raw_emg)
    }

    return results_dict
def get_iso_res_df(raw_emg, vel_txt):

    results_dict = {
        "max_emg": get_iso_peak_emg_one_mus(raw_emg),
        "max_emg2": get_iso_peak_emg_one_mus(raw_emg)
    }
    results_df = pd.DataFrame([results_dict])

    return results_df

class IsoMedialMuscleHead(object):
    def __init__(self, raw_emg_mh, vel_txt):
        self.results = get_iso_res(raw_emg_mh, vel_txt)
        self.results_df = get_iso_res_df(raw_emg_mh, vel_txt)


class IsoLateralMuscleHead(object):
    def __init__(self, raw_emg_lh, vel_txt):
        self.results = get_iso_res(raw_emg_lh, vel_txt)
        self.results_df = get_iso_res_df(raw_emg_lh, vel_txt)


class DynMedialMuscleHead(object):
    def __init__(self, raw_emg_mh, vel_txt):
        pass


class DynLateralMuscleHead(object):
    def __init__(self, raw_emg_lh, vel_txt):
        pass

