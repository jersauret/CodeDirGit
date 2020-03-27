from pathlib import Path
from matplotlib.pyplot import plot as plt
from b_back_pro.c_iso.c_a_iso_mus_act import IsoMusAct
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from b_back_pro.utils.data_crafting_tools.pre_processing_of_data import cutting_beg_and_end_base_on_GRF
from b_back_pro.utils.dynamic_processing.butt_emg_filt_dyn import *


def find_ground_contact(grf):
    ground_contact = np.argmax(grf > 10)
    print("ground", ground_contact)
    return ground_contact


def find_peak_grf_index(grf):
    peak_grf_value = np.amax(grf)
    peak_grf_index = np.argmax(grf == peak_grf_value)
    print("peak grf ", peak_grf_value, " at index ", peak_grf_index)
    return peak_grf_index


class BioRep(object):

    def __init__(self, part_id, bio_task_name, bio_rep_name):
        self.part_id = part_id
        file_url_base = Path("C:\\HealthTrackHome\\DataDir\\bio_json\\")
        new_file_name = Path(part_id + bio_task_name + bio_rep_name + '.json')
        new_file_url = file_url_base.joinpath(new_file_name)
        print("l'adresse du fichier que je vais ouvrir:", new_file_url)
        complete_data = pd.read_json(new_file_url)
        cut_data = cutting_beg_and_end_base_on_GRF(complete_data)
        gc_index = find_ground_contact(cut_data['GrfY'])
        pf_index = find_peak_grf_index(cut_data['GrfY'])
        knee_fle_pos_gc = cut_data["KneeAngleZ"][gc_index]
        knee_fle_pos_pf = cut_data["KneeAngleZ"][pf_index]
        knee_fle_pos_ip = pd.Series(cut_data["KneeAngleZ"][gc_index:pf_index])
        knee_fle_exc_ip = knee_fle_pos_gc - knee_fle_pos_pf
        series_index = knee_fle_pos_ip.index - gc_index - 200
        model_knee_fle_pos_ip = interp1d(series_index, knee_fle_pos_ip)
        new_knee_fle_pos_ip=model_knee_fle_pos_ip(series_index)
        new_range = np.arange(series_index[0], series_index[len(series_index) - 1], len(series_index) / 100)
        filt_m1_mh_emg = pd.Series(filter_implementation_butter_low_pass_dyn_emg(abs(complete_data["vm"])))
        filt_m1_lh_emg = pd.Series(filter_implementation_butter_low_pass_dyn_emg(abs(complete_data["vl"])))
        filt_m2_mh_emg = pd.Series(filter_implementation_butter_low_pass_dyn_emg(abs(complete_data["st"])))
        filt_m2_lh_emg = pd.Series(filter_implementation_butter_low_pass_dyn_emg(abs(complete_data["bf"])))
        m1_lh_emg_ip = pd.Series(filt_m1_lh_emg[gc_index: pf_index])
        m1_mh_emg_ip = pd.Series(filt_m1_mh_emg[gc_index: pf_index])
        m2_lh_emg_ip = pd.Series(filt_m2_lh_emg[gc_index: pf_index])
        m2_mh_emg_ip = pd.Series(filt_m2_mh_emg[gc_index: pf_index])
        model_filt_m1_mh_emg = interp1d(series_index, m1_mh_emg_ip)
        model_filt_m1_lh_emg = interp1d(series_index, m1_lh_emg_ip)
        model_filt_m2_mh_emg = interp1d(series_index, m2_mh_emg_ip)
        model_filt_m2_lh_emg = interp1d(series_index, m2_lh_emg_ip)
        new_filt_m1_mh_emg = model_filt_m1_mh_emg(new_range)
        new_filt_m1_lh_emg = model_filt_m1_lh_emg(new_range)
        new_filt_m2_mh_emg = model_filt_m2_mh_emg(new_range)
        new_filt_m2_lh_emg = model_filt_m2_lh_emg(new_range)


        knee_val_pos_gc = cut_data["KneeAngleY"][gc_index]
        knee_val_pos_pf = cut_data["KneeAngleY"][pf_index]
        knee_val_exc_ip = knee_val_pos_gc - knee_val_pos_pf

        self.b_res_rep_dict = {
            "peak_grf": np.amax(cut_data['GrfY']),
            "ip_dur": pf_index - gc_index,
            "knee_val_pos_gc": knee_fle_pos_gc,
            "knee_val_exc_ip": knee_fle_exc_ip,
            # "knee_fle_pos_ip" : new_knee_fle_pos_ip,
            "knee_fle_pos_gc": knee_val_pos_gc,
            # "knee_fle_exc_ip": knee_val_exc_ip,
            # "m1_tot_emg_ip": new_filt_m1_mh_emg + new_filt_m1_lh_emg,
            # "m2_tot_emg_ip": new_filt_m2_mh_emg + new_filt_m2_lh_emg,
            # "m1_mh_emg_ip": new_filt_m1_mh_emg,
            # "m1_lh_emg_ip": new_filt_m1_lh_emg,
            # "m2_mh_emg_ip": new_filt_m2_mh_emg,
            # "m2_lh_emg_ip": new_filt_m2_lh_emg,

        }
        # plt(new_filt_m2_mh_emg)
        self.b_res_rep_df = pd.DataFrame.from_dict(self.b_res_rep_dict, orient='index')
        print( self.b_res_rep_df)
        print("j'ai fini cette répétition de bio")
    # self.data_angle_hip_z = cut_data['HipAngleZ']
    # self.data_angle_hip_y = cut_data['HipAngleY']
    # self.data_angle_hip_x = cut_data['HipAngleX']
    # self.data_angle_hip_z = cut_data['KneeAngleZ']
    # self.data_angle_hip_y = cut_data['KneeAngleY']
    # self.data_angle_hip_x = cut_data['KneeAngleX']
    # self.data_angle_hip_z = cut_data['AnkleAngleZ']
    # self.data_angle_hip_y = cut_data['AnkleAngleY']
    # self.data_angle_hip_x = cut_data['AnkleAngleX']
    # self.data_pos_com_y = cut_data['CoMY']
    # self.data_moment_hip_z = cut_data['HipMomZ']
    # self.data_moment_hip_y = cut_data['HipMomY']
    # self.data_moment_hip_x = cut_data['HipMomX']
    # self.data_moment_knee_z = cut_data['KneeMomZ']
    # self.data_moment_knee_y = cut_data['KneeMomY']
    # self.data_moment_knee_x = cut_data['KneeMomX']
    # self.data_moment_ankle_z = cut_data['AnkleMomZ']
    # self.data_moment_ankle_y = cut_data['AnkleMomY']
    # self.data_moment_ankle_x = cut_data['AnkleMomX']
    # self.data_antshefor_knee = cut_data['KneeShearForce']
    # self.data_raw_vl = cut_data['vl']
    # self.data_raw_vm = cut_data['vm']
    # self.data_raw_bf = cut_data['bf']
    # self.data_raw_st = cut_data['st']
    # self.data_grf_z = cut_data['GrfZ']
    # self.data_grf_y = cut_data['GrfY']
    # self.data_grf_x = cut_data['GrfX']
    #
