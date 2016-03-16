__author__ = 'Daniil'
from tkinter import *


class Card:
    def __init__(self, master, number, location1='', location2='', x=0, y=0):
        self.img_inside = PhotoImage(file=location1)
        self.img_ouside = PhotoImage(file=location2)
        self.img = [self.img_inside, self.img_ouside]
        self.number = number
        self.state = 0
        self.master=master
        self.image = Label(master, image=self.img[0], cursor='hand2')
        self.position = {'x': x, 'y': y}
        self.set_bind()
        self.show()

    def flip(self):
        self.state = (self.state+1) % 2
        self.image['image'] = self.img[self.state]
        self.master.update()

    def set_bind(self):
        self.image.bind('<Button-1>', lambda e: self.flip())

    def unbind(self):
        self.image.unbind('<Button-1>')

    def show(self):
        self.image.grid(row=self.position['x'], column=self.position['y'])

    def hide(self):
        self.image.grid_forget()