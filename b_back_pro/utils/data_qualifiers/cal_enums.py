import numpy as np
import pandas as pd
from enum import Enum

# movementtype should describe the direction of the movement
# independent of the contraction
# for example a concentric quadriceps extensiuon and an hamstrings eccentric
# action would be considered extension
from os import write


class MovementType(Enum):
    Extension = 1
    Flexion = 2


# This field should be informed for all four muscles
class MuscleContraction(Enum):
    Concentric = 1
    Eccentric = 2
    Isometric = 3


#  this field should be informed for all four muscles
class CoActivationROle(Enum):
    Agonist = 1
    Antagonist = 2


def get_movement_characteristics(variable_sought, muscle_and_velocity_as_capped_m1v1):
    movement_dict = {
        "M1V1": {"Speed": 180, "Direction": 'flexion', "M1_Co_act": "agonist", "M1_action": "eccentric", "M2_Co_act": "antagonist", "M2_action": "concentric"},
        "M1V2": {"Speed": 270, "Direction": 'flexion', "M1_Co_act": "agonist", "M1_action": "eccentric", "M2_Co_act": "antagonist", "M2_action": "concentric"},
        "M1V3": {"Speed": 180, "Direction": 'extension', "M1_Co_act": "agonist", "M1_action": "concentric", "M2_Co_act": "antagonist", "M2_action": "eccentric"},
        "M1V4": {"Speed": 0, "Direction": 'extension', "M1_Co_act": "agonist", "M1_action": "isometric", "M2_Co_act": "antagonist", "M2_action": "eccentric"},
        "M2V1": {"Speed": 90, "Direction": 'flexion', "M1_Co_act": "antagonist", "M1_action": "eccentric", "M2_Co_act": "agonist", "M2_action": "concentric"},
        "M2V2": {"Speed": 180, "Direction": 'flexion', "M1_Co_act": "antagonist", "M1_action": "eccentric", "M2_Co_act": "agonist", "M2_action": "concentric"},
        "M2V3": {"Speed": 180, "Direction": 'extension', "M1_Co_act": "antagonist", "M1_action": "concentric", "M2_Co_act": "agonist", "M2_action": "eccentric"},
        "M2V4": {"Speed": 0, "Direction": 'flexion', "M1_Co_act": "antagonist", "M1_action": "isometric", "M2_Co_act": "agonist", "M2_action": "isometric"}}
    return movement_dict[muscle_and_velocity_as_capped_m1v1][variable_sought]
