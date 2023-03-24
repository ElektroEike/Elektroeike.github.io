import tkinter as tk
import tkinter.font as font
from tkinter import ttk

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('250x150')
        self.create_widgets()
        self.styleInfo()

    def create_widgets(self):
        self.label = ttk.Label(self.root, anchor=tk.CENTER, text="Hallo, Welt", style='BlackLabel.TLabel');
        self.label.pack(fill=tk.BOTH, expand=tk.YES)

        self.button = ttk.Button(self.root, text="Hallo, Button", style='BlackLabel.TButton');
        self.button.pack(fill=tk.BOTH, expand=tk.YES)

        self.quit = ttk.Button(self.root, text='Quit', command=self.root.destroy)
        self.quit.pack(fill=tk.X, expand=tk.NO)

    def styleInfo(self):
        print(self.label.winfo_class())
        print(self.button.winfo_class())
        
        self.style = ttk.Style(self.root);
        print( self.style.theme_use() )
        self.style.configure('BlackLabel.TLabel', background='black',
            foreground='white', anchor=tk.CENTER, font=('Courier', 20, font.BOLD, font.ITALIC) );

        self.style.configure('BlackLabel.TButton', font=('Courier', 20, font.BOLD), borderwidth=5 );


        self.style.map('BlackLabel.TButton', foreground = [('active', '!disabled', 'blue')],
                     background = [('active', '!focus', 'red')], text="foo")

        
        print( self.style.layout('BlackLabel.TButton') )
        print( self.style.element_options('BlackLabel.TButton.padding'))

        print(self.button.winfo_children())

        

        
app = Application()
app.root.mainloop()

