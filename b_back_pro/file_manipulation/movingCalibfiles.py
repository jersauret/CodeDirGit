from pathlib import Path
import os
import shutil

source_path = Path('C:/Users/a766560/OneDrive - Atos/Desktop/perso/these/calib')
destination_path_base = Path('C:/Users/a766560/OneDrive - Atos/Desktop/perso/these')
file_list = list(source_path.glob('*.txt'))
for file in source_path.glob('*.txt'):
    type_of_test = ['calibdeplace']
    part_nb = [file.name[0:3]]
    muscle_nb = [file.name[3:5]]
    velocity_nb = [file.name[5:7]]
    repetition_nb = [file.name[7:9]]
    destination_path_final = destination_path_base.joinpath(*type_of_test,*part_nb, *muscle_nb, *velocity_nb, *repetition_nb)

    while not destination_path_final.exists():
        source_path_file = source_path.joinpath(*[file.name])
        destination_path_final_file = destination_path_final.joinpath(*[file.name])
        os.makedirs(destination_path_final)
        shutil.copyfile(source_path_file, destination_path_final_file)
