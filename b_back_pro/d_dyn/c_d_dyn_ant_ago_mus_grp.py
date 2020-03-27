from b_back_pro.muscle.mus_heads import DynMedialMuscleHead, DynLateralMuscleHead


class DynAntMusGrp:
    def __init__(self, ago_raw_emg_mh, ago_raw_emg_lh, vel_txt):
        self.mmh = DynMedialMuscleHead(ago_raw_emg_mh, vel_txt)
        self.lmh = DynLateralMuscleHead(ago_raw_emg_lh, vel_txt)


class DynAgoMusGrp:
    def __init__(self, ago_raw_emg_mh, ago_raw_emg_lh, vel_txt):
        self.mmh = DynMedialMuscleHead(ago_raw_emg_mh, vel_txt)
        self.lmh = DynLateralMuscleHead(ago_raw_emg_lh, vel_txt)
