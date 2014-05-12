from tkinter import *

class Panel(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.canvas = Canvas(self, width=512, height=512)
        self.canvas.pack()
        for x in range(16):
            x0 = x * 16
            for y in range(16):
                y0 = y * 16
                self.canvas.create_rectangle((x0,y0,x0+16,y0+16), outline='', fill='#%2x%2x00' % (x0, y0))


Panel().mainloop()
