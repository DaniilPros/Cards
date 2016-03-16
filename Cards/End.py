__author__ = 'Daniil'
from tkinter import *
class End:
    def __init__(self, master, start, time):
        self.start = start
        self.frame = Frame(master, height=100, width=100, bg='orange')
        import math
        time =self.set_time( math.floor(time))
        Label(self.frame, font='ComicSans 20', text='Your time: %s minute(s) %s seconds' % (time[0], time[1]), background='orange', fg='red').pack(side='top')
        l1 = Label(self.frame, font='ComicSans 20', text='Play', background='orange', fg='green', cursor='hand2')
        l1.bind('<Button-1>', lambda e: self.Play())
        l1.pack(side='top')
        l2 = Label(self.frame, font='ComicSans 20', text='End', background='orange', fg='green', cursor='hand2')
        l2.bind('<Button-1>', lambda e: self.End())
        l2.pack(side='top')
        self.frame.update()
        self.frame.pack(side='top')
        self.master = master

    def set_time(self, time):
        if time >= 60:
            return [time//60, time % 60]
        else:
            return [0, time]


    def Play(self):
        self.frame.pack_forget()
        self.start.pack(side='top')

    def End(self):
        self.master.destroy()
#mvc
# in python