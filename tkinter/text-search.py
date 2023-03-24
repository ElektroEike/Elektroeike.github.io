import tkinter as tk
from tkinter import ttk

class A(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self._createWidgets()

    def _createWidgets(self):
        self._text = tk.Text(self, width=40, height=20)
        self._text.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
        self._text.tag_configure('found-tag', background='lightgreen')
        frame = ttk.Frame(self)
        frame.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)
        self._entry = ttk.Entry(frame)
        self._entry.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        button = ttk.Button(frame, text='Finde', command=self._onFind)
        button.pack(side=tk.LEFT, fill=tk.X)

    def _onFind(self):
        searchText = self._entry.get()
        if len(searchText) == 0:
            return
        var = tk.IntVar()
        foundIndex = self._text.search(searchText, '1.0', stopindex=tk.END,
                                       nocase=tk.YES, count=var,
                                       regexp=tk.YES)
        if len(foundIndex) == 0:
            return
        count = var.get()
        lastIndex = self._text.index(f'{foundIndex} + {count}c')
        self._text.tag_remove('found-tag', '1.0', tk.END)
        self._text.tag_add('found-tag', foundIndex, lastIndex)

if __name__ == '__main__':
    window = A()
    window.mainloop()
