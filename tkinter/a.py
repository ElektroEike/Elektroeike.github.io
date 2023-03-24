import tkinter as tk
from tkinter import ttk

class A(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('200x200')
        self._createWidgets()

    def _createWidgets(self):
        button = ttk.Button(self, text='Hallo',
                            command=lambda a='xxx': self._onClick(a))
        button.pack(fill=tk.BOTH, expand=tk.YES)

        self.bind('<KeyPress-x>',
                  lambda event, a='Hallo, Welt': self._onPress(event, a))

    def _onClick(self, text):
        print('Hello, extra Parameter:', text)

    def _onPress(self, event, text):
        print('x gedrück mit Parameter:', event, text)



if __name__ == '__main__':
    window = A()
    window.mainloop()
