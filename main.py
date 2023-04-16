from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('408x355')

root.minsize(405, 355)
root.maxsize(408, 355)

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#ffffff',
          bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)


root.mainloop()
