__author__ = 'Daniil'
from MainFrame import*

class Level:
    def __init__(self, master):
        self.frame = Frame(master, height=100, width=100, bg='orange')
        self.labels = []
        self.commands = {'Easy': self.Easy, 'Middle': self.Middle, 'Hard': self.Hard}
        self.master = master
        self.labels.append(Label(self.frame, font='ComicSans 20', text='Easy', background='orange', fg='green', cursor='hand2'))
        self.labels.append(Label(self.frame, font='ComicSans 20', text='Middle', background='orange', fg='green', cursor='hand2'))
        self.labels.append(Label(self.frame, font='ComicSans 20', text='Hard', background='orange', fg='green', cursor='hand2'))
        for i in self.labels:
            i.grid(row=self.labels.index(i))
        self.labels[0].bind('<Button-1>', lambda e: self.Easy())
        self.labels[1].bind('<Button-1>', lambda e: self.Middle())
        self.labels[2].bind('<Button-1>', lambda e: self.Hard())
        self.frame.pack(side='top')

    def show(self):
        self.frame.pack(side='top')

    def Easy(self):
        self.frame.pack_forget()
        game = Game(self.master, 16, self.frame)

    def Middle(self):
        self.frame.pack_forget()
        game = Game(self.master, 28, self.frame)

    def Hard(self):
        self.frame.pack_forget()
        game = Game(self.master, 36, self.frame)