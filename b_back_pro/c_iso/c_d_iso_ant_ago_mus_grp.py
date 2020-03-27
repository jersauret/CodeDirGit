from b_back_pro.muscle.mus_heads import IsoMedialMuscleHead, IsoLateralMuscleHead


class IsoAntMusGrp:
    def __init__(self, ago_raw_emg_mh, ago_raw_emg_lh, vel_txt):
        self.mmh = IsoMedialMuscleHead(ago_raw_emg_mh, vel_txt)
        self.lmh = IsoLateralMuscleHead(ago_raw_emg_lh, vel_txt)


class IsoAgoMusGrp:
    def __init__(self, ago_raw_emg_mh, ago_raw_emg_lh, vel_txt):
        self.mmh = IsoMedialMuscleHead(ago_raw_emg_mh, vel_txt)
        self.lmh = IsoLateralMuscleHead(ago_raw_emg_lh, vel_txt)
