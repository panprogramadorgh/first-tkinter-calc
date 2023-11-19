from tkinter import *
from functions import calculate as calc, handle_click, delete_entry

root = Tk()

# entries
firstEntry = Entry(root, width=50)
seccondEntry = Entry(root, width=50)

# buttons
sumButton = Button(root, text='Sum numbers', command=lambda: handle_click((firstEntry, seccondEntry), 'sum'))
subButton = Button(root, text='Sub numbers', command=lambda: handle_click((firstEntry, seccondEntry), 'sub'))
multiButton = Button(root, text='Multi numbers', command=lambda: handle_click((firstEntry, seccondEntry), 'multi'))
divButton = Button(root, text='Div numbers', command=lambda: handle_click((firstEntry, seccondEntry), 'div'))

# griding entries
Label(root, text='First number').grid(row=0, column=0)
Label(root, text='Seccond number').grid(row=1, column=0)
firstEntry.grid(row=0, column=1)
seccondEntry.grid(row=1, column=1)
# griding buttons
sumButton.grid(row=2, column=0)
subButton.grid(row=2, column=1)
multiButton.grid(row=2, column=2)
divButton.grid(row=2, column=3)

root.mainloop()