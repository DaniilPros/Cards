__author__ = 'Daniil'
from Card import *
import time

from End import *

class Game:
    def __init__(self, master, count, start):
        self.start = start
        self.master = master
        self.count = count
        self.count_of_flip = 0
        self.choise_number = {}
        self.step = 0
        if count == 28:
            self.c = 7
        elif count == 16:
            self.c = 4
        elif count == 36:
            self.c = 6
        self.cards = []
        self.frame = Frame(master, bg='orange')
        self.numbers = self.generate()
        ss = "inside.png"
        for i in range(count):
            s = '%s' % (self.numbers[i]+1)
            s += ".png"
            self.cards.append(Card(self.frame, [self.numbers[i], i], ss, s, i//self.c, i % self.c))
        for i in self.cards:
            i.image.bind('<Button-1>', lambda e, obj=i: self.flip(obj))
            i.show()
        self.frame.update()
        self.frame.pack(side='top')
        self.time = time.time()

    def set_bind(self):
        for i in self.cards:
            i.image.bind('<Button-1>', lambda e, obj=i: self.flip(obj))

    def unbind(self):
        for i in self.cards:
            i.unbind()

    def flip(self, obj):
        if self.count_of_flip == 0:
            obj.flip()
            self.choise_number = obj.number
            self.count_of_flip = (self.count_of_flip+1) % 2
        elif self.choise_number[0] == obj.number[0]and self.choise_number[1] != obj.number[1]:
            obj.flip()
            time.sleep(0.1)
            self.step += 2
            obj.hide()
            self.cards[self.choise_number[1]].hide()
            self.count_of_flip = (self.count_of_flip+1) % 2
            if self.step == self.count:
                self.frame.destroy()
                self.time = time.time()-self.time
                f = End(self.master, self.start, self.time)
        elif self.choise_number[0] == obj.number[0]and self.choise_number[1] == obj.number[1]:
            pass
        else:
            obj.flip()
            self.unbind()
            time.sleep(0.5)
            obj.flip()
            self.cards[self.choise_number[1]].flip()
            self.set_bind()
            self.count_of_flip = (self.count_of_flip+1) % 2

    def generate(self):
        l = []
        d = {}
        def isset(n, d):
            if d[n] == 1 or d[n] == 0:
                d[n] += 1
                return TRUE
            else:
                return FALSE

        import random
        ll = []
        i=0
        #r = NONE
        while i !=self.count//2:
            r = random.randint(1, 22)
            if r in ll:
                pass
            else:
                ll.append(int(r))
                d.update({r: 0})
                i+=1
        leng = 0
        while leng != len(ll)*2:
            r = random.randint(0, len(ll)-1)
            if isset(ll[r], d):
                l.append(int(r))
                leng += 1
        return l
