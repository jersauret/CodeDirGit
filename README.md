# CodeDirGit
 
# HealthTrack

HealthTrack is a Python3 app with purpose to help pratictioners diagnostic an increased risk of ACL injury in 
females aged around 20.

## Installation

This super app has been created using a virtualenv (python37) with all requirements listed in requirements.txt
Simply download the files, access the project folder and run entrypoint.py
a_data_from ... : script to transform the original data and transform it to json format.
this format is what the rest of the project will use.
b_back_pro: calculations and object structure
	a_part: participant class(top of the structure)
	b_anthro: getting all the anthropometric data from a file that is attached to the project
	c_iso: processing of isometric (V4) data, storing of individual emg amplitude maxes for normalization
	d_dyn: processing of dynamic (V1) data, creation of the equation describing the amount of emg amplitude 
		(% of isometric max) necessary to create one unit of torque at a specific knee angle
		- @65° 10%IsoMaxEmg / 1 Nm
	e_bio: processing of biomechanics data (drop jump see here https://www.youtube.com/watch?v=SrCfgnllAmk)
		-get data during the impact phase (time between ground contact and peak ground reaction force)
		-average over 5 repetitions
in 

## Usage
you can change the number of participants that you wish to include in the analysis by modifying the participant file

## Folder Structure
This app is organized in an a, b, c format for packages.
Typically the processes are organized in the order in which the packages are used during the creation of participants