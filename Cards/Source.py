__author__ = 'Daniil'
from Level import *

root = Tk('Cards', 'Cards', 'Cards')
root.config(bg='orange')
root.wm_attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.iconify())
root.update_idletasks()
start = Level(root)
root.mainloop()
