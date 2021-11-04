import tkinter

def onSelect(evt):
    theListBox = evt.widget 
    index = int(theListBox.curselection()[0])
    print("Position is", index) 
    val = theListBox.get(index)
    print("Val is", val)  
        
s = tkinter.Scrollbar()
L = tkinter.Listbox()
s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
L.pack(side=tkinter.LEFT, fill=tkinter.Y)
s.config(command=L.yview)
L.config(yscrollcommand=s.set)

L.bind('<<ListboxSelect>>', onSelect) 

for i in range(30): 
    L.insert(tkinter.END, str(i)*3)
    
tkinter.mainloop()