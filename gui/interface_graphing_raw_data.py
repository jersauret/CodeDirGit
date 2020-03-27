__author__ = 'Jer'

import matplotlib
from b_back_pro.a_part import participant
from b_back_pro.a_part.participant import Participant

matplotlib.use('TkAgg')
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *



class mclass:

    def __init__(self, window):
        self.canvas = None
        self.window=window
        self.window.geometry('800x1500-1600+150')
        self.v = IntVar()
        self.v.set(2)
        self.box = Entry(window, textvariable=self.v)
        self.box.focus()
        self.box.bind("<Return>", self.get_Min_Vin_R1)
        self.button = Button(window, text="voir les données", command=self.plot_with_participant_v2)
        self.button.pack()
        self.box.pack()
        self.var = StringVar()
        self.choix_muscle = Listbox(window,exportselection=0)
        self.choix_muscle.configure(justify=LEFT)
        self.choix_muscle.pack()
        for item in ["quadriceps", "hamstrings"]:
            self.choix_muscle.insert(END, item)
        self.choix_muscle.bind("<<ListboxSelect>>", self.get_Min_V1_R1)

        self.choix_velocity = Listbox(window,exportselection=0 )
        self.choix_velocity.configure(justify=LEFT)
        self.choix_velocity.pack()
        for item in ["V1", "V2", "V3"]:
            self.choix_velocity.insert(END, item)
        self.choix_velocity.bind("<<ListboxSelect>>", self.get_Min_Vin_R1)

    def get_Min_Vin_R1(self, event):
        part_nb = int(self.box.get())
        participant_of_int = participant.Participant(part_nb)
        muscle_index = self.choix_muscle.curselection()
        data = get_forPart_Min_Vin_R1_VL(participant_of_int,
                                                                 self.choix_muscle.get(muscle_index))
        self.plot_with_participant_v2(data)

    def get_Min_V1_R1(self, event):
        part_nb = int(self.box.get())
        participant_of_int = Participant(part_nb)
        muscle_index = self.choix_muscle.curselection()
        muscle_of_int= str(self.choix_muscle.get(muscle_index))
        data = get_forPart_Min_V1_R1_VL(participant_of_int, muscle_of_int)
        print("choix", type(str(self.choix_muscle.get(muscle_index))))
        self.plot_with_participant_v2(data)

    def get_Min_Vin_R1(self, eventvelocity_of_int):
        part_nb = int(self.box.get())
        participant_of_int = participant.Participant(part_nb)
        muscle_index = self.choix_muscle.curselection()
        muscle_of_int = str(self.choix_muscle.get(muscle_index))
        velocity_index = self.choix_velocity.curselection()
        velocity_of_int = self.choix_velocity.get(velocity_index)
        data = get_forPart_Min_Vin_R1_VL(participant_of_int, muscle_of_int, velocity_of_int)
        print(data)
        self.plot_with_participant_v2(data)

    def appelaplot(self, event):
        self.plot_with_participant_v2()

    def plot_with_participant_v2(self, data):
        p = np.array(data)
        v = np.arange(len(data))
        fig = Figure(figsize=(6, 6))
        a = fig.add_subplot(111)
        #      a.scatter(v,x,color='red')
        a.plot(v, p, color='blue')
        a.set_title( self.create_str__4_graph_title(), fontsize=16)
        a.set_ylabel('mV', fontsize=14)
        a.set_xlabel("ms", fontsize=14)
        if self.canvas is not None:
            self.canvas.get_tk_widget().pack_forget()

        self.canvas = FigureCanvasTkAgg(fig, master=self.window)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def create_str__4_graph_title (self):
        participant = ('Participant ' + self.box.get())
        filename = str(data_acess.DataService.filename)

        return (participant + ' ' + filename)

    def plot_with_participant(self):
        part_nb = int(self.box.get())
        participant_of_int = participant.Participant(part_nb)
        data = participant.Participant.get_forPart_M1_V1_R1_VL(participant_of_int)
        p = np.array(data)
        v = np.arange(len(data))
        print(len(v))
        # p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
        #     19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])

        fig = Figure(figsize=(6, 6))
        a = fig.add_subplot(111)
        #      a.scatter(v,x,color='red')
        a.plot(v, p, color='blue')
        a.invert_yaxis()

        a.set_title(int(self.box.get()), fontsize=16)
        a.set_ylabel(self.v, fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

window = Tk()
start = mclass(window)
window.mainloop()
