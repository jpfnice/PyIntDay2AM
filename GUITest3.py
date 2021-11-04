import tkinter as tk

class MyWindow(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self) # <=> super().__init__()
        s = tk.Scrollbar(self)
        L = tk.Listbox(self)
        s.pack(side=tk.RIGHT, fill=tk.Y)
        L.pack(side=tk.LEFT, fill=tk.Y)
        s.config(command=L.yview)
        L.config(yscrollcommand=s.set)

        L.bind('<<ListboxSelect>>', self.onSelect) 
        
        for i in range(30): 
            L.insert(tk.END, str(i)*3)
            
    def onSelect(self, evt):
        theListBox = evt.widget 
        index = int(theListBox.curselection()[0])
        print("Position is", index) 
        val = theListBox.get(index)
        print("Val is", val)  
           
if __name__== "__main__":
    win=MyWindow()
    tk.mainloop()
