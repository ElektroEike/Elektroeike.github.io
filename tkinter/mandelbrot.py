""" Mandelbrot """

import tkinter  as tk
from tkinter import ttk
from PIL  import Image, ImageDraw, ImageTk

class Mandelbrot(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.geometry('400x400')
        self.title('Mandelbrot')
        # config for rows, columns
        self.rowconfigure(0, weight=10)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=0)
        # canvas
        self.canvas = tk.Canvas(
            self, bd=1, relief=tk.SUNKEN, width=200, height=200,
            scrollregion=(0, 0, self.width, self.height),
            background='white')
        self.canvas.grid(column=0, row=0, sticky=tk.E+tk.W+tk.N+tk.S)
        # scrollbars for canvas
        scrollH = ttk.Scrollbar(self, orient=tk.HORIZONTAL,
                                command=self.canvas.xview)
        scrollH.grid(column=0, row=1, sticky=tk.E+tk.W)
        scrollV = ttk.Scrollbar(self, orient=tk.VERTICAL,
                                command=self.canvas.yview)
        scrollV.grid(column=1, row=0, sticky=tk.N+tk.S)
        self.canvas['xscrollcommand'] = scrollH.set
        self.canvas['yscrollcommand'] = scrollV.set
        #
        # run
        self.image = Image.new('RGB', (self.width, self.height))
        self.photoImage = ImageTk.PhotoImage(self.image)
        self.drawImage = ImageDraw.Draw(self.image)
        self.canvas.create_image(0, 0,
                                 anchor=tk.NW,
                                 image=self.photoImage)
        # calculate region of image
        self.scaleXMin = int(self.width * 3 // 4)
        self.scaleXMax = self.width - self.scaleXMin
        self.scaleXDivider = self.scaleXMax
        self.scaleYMin = int(self.height // 2)
        self.scaleYMax = self.scaleYMin
        self.scaleYDivider = self.scaleYMax // 2
        
        self.makeIteration()

    def mandelbrotIteration(self, x, y, count):
        z0 = complex(0, 0)
        c = complex(x, y)
        for n in range(0, count):
            z = z0 * z0 + c
            z0 = z
            if abs(z) > 10:
                return n
        return count

    def plotPixel(self, x, y, value):
        v = 255 - value * 20    # rgb color value
        color = (v, v, v)       # set color to grey mode
        self.drawImage.point((x+self.scaleXMin, y+self.scaleYMin),
                             fill=color)

    def makeIteration(self):
        for x in range(-self.scaleXMin, self.scaleXMax+1):
            for y in range(-self.scaleYMin, self.scaleYMax+1):
                xi = x / self.scaleXDivider
                yi = y / self.scaleYDivider
                count = self.mandelbrotIteration(xi, yi, 10)
                self.plotPixel(x, y, count)
        self.photoImage.paste(self.image)

if __name__ == '__main__':
    app = Mandelbrot(500, 500)
    app.mainloop()
