from pathlib import Path
import os
import shutil

source_path = Path('C:/Users/a766560/OneDrive - Atos/Desktop/perso/these/biomecanicsflat')
destination_path_base = Path('C:/Users/a766560/OneDrive - Atos/Desktop/perso/these')

for file in source_path.glob('*.exp'):
    type_of_test = ['biomecanicsstructure']
    part_nb = [file.name[0:3]]
    task_nb = [file.name[3:5]]
    repetition_nb = [file.name[5:7]]
    destination_path_final = destination_path_base.joinpath(*type_of_test, *part_nb, *task_nb, *repetition_nb)

    while not destination_path_final.exists():
        source_path_file = source_path.joinpath(*[file.name])
        destination_path_final_file = destination_path_final.joinpath(*[file.name])
        os.makedirs(destination_path_final)
        shutil.copyfile(source_path_file, destination_path_final_file)
