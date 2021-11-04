
"""
tkinter (tk -> tcl)
PyQT (QT -> C++)

PyGTK (GTK -> C++)


Container : Window (tk frame)

Final component: Button, Entry, Scrollbars

Layout Managers (Geometry Managers): placer, gridder, packer

Event: event source + event listener

"""

import tkinter as tk 
import tkinter.filedialog as fd
import tkinter.messagebox as mb

class MyWindow(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self) # <=> super().__init__()
        
        self.minsize(500,200)
        self.title("Just a test")
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
#        self.rowconfigure(0, weight=1)
#         self.rowconfigure(1, weight=1)

        # Binding variables:
        self.nameStr=tk.StringVar()
        self.telStr=tk.StringVar()
        
        nameL=tk.Label(self, text="Name:")
        # Geometry Manager: placer, packer, gridder
        
        nameL.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E+tk.W)
        
        nameE=tk.Entry(self, textvariable=self.nameStr)
        nameE.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E+tk.W)
        
        clickB=tk.Button(self, text="click", command=self.hello)
        clickB.grid(row=0, column=2, padx=10, pady=10)
        
        clearB=tk.Button(self, text="clear", command=self.clear)
        clearB.grid(row=0, column=3, padx=10, pady=10)
        
        telL=tk.Label(self, text="Phone number:")
        telL.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        
        telE=tk.Entry(self, textvariable=self.telStr)
        telE.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E+tk.W)
        
        self.setMenu()
        
    def setMenu(self):
        import sys
        mainmenu = tk.Menu(self)  # MenuBar
         
        menuFile = tk.Menu(mainmenu)  # Menu File
        menuFile.add_command(label="Open", command=self.openFile)
        menuFile.add_command(label="Quit", command=sys.exit) 
  
        menuHelp = tk.Menu(mainmenu) # Menu Help
        menuHelp.add_command(label="About", command=self.about) 
        
        mainmenu.add_cascade(label = "File", menu=menuFile) 
        mainmenu.add_cascade(label = "Help", menu=menuHelp)
        
        # display the menu
        self.config(menu = mainmenu) 

    def about(self): 
        mb.showinfo("A tkinter example", "Version 1.0")
        
    def hello(self):
        print("Hello", self.nameStr.get())
        
    def clear(self):
        self.nameStr.set("")
        self.telStr.set("")
        
    def openFile(self): 
        FILEOPENOPTIONS = dict(defaultextension='*.xml',
                               filetypes=[('Gif file', '*.gif'),('XML file','*.xml'),('All files','*.*')])
        file_path = fd.askopenfilename(parent=self, **FILEOPENOPTIONS)
        if file_path:
            print(file_path)
              
if __name__== "__main__":
    win=MyWindow()
    tk.mainloop()
