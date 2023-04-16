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
px = 40


def click_button(num):
    return


def division_button():
   return


def multply_button():
   return


def sum_button():
    return


def minus_button():
    return


def ac_button():
    return


def total_button():
    return


divide = Button(root,
                text='/',
                padx=40,
                pady=20,
                command=division_button,
                fg='#ffffff',
                activebackground='#ffffff',
                bg='#E38A1E',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
divide.grid(row=0, column=4)

n_one = Button(root,
               text='1',
               padx=40,
               pady=20,
               command=lambda: click_button(1),
               fg='#ffffff',
               activebackground='#ffffff',
               bg='#E38A1E',
               relief=FLAT,
               font=('futura', 12, 'bold')
               )
n_one.grid(row=1, column=1)

n_two = Button(root,
               text='2',
               padx=40,
               pady=20,
               command=lambda: click_button(2),
               fg='#ffffff',
               activebackground='#ffffff',
               bg='#E38A1E',
               relief=FLAT,
               font=('futura', 12, 'bold')
               )
n_two.grid(row=1, column=2)

n_three = Button(root,
                 text='3',
                 padx=40,
                 pady=20,
                 command=lambda: click_button(3),
                 fg='#ffffff',
                 activebackground='#ffffff',
                 bg='#E38A1E',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
n_three.grid(row=1, column=3)

multply = Button(root,
                 text='*',
                 padx=44,
                 pady=20,
                 command=multply_button,
                 fg='#ffffff',
                 activebackground='#ffffff',
                 bg='#E38A1E',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
multply.grid(row=1, column=4)

n_four = Button(root,
                text='4',
                padx=px,
                pady=20,
                command=lambda: click_button(4),
                fg='#ffffff',
                activebackground='#ffffff',
                bg='#E38A1E',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
n_four.grid(row=2, column=1)

n_five = Button(root,
                text='5',
                padx=px,
                pady=20,
                command=lambda: click_button(5),
                fg='#ffffff',
                activebackground='#ffffff',
                bg='#E38A1E',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
n_five.grid(row=2, column=2)

n_six = Button(root,
               text='6',
               padx=px,
               pady=20,
               command=lambda: click_button(6),
               fg='#ffffff',
               activebackground='#ffffff',
               bg='#E38A1E',
               relief=FLAT,
               font=('futura', 12, 'bold')
               )
n_six.grid(row=2, column=3)

sum = Button(root,
             text='+',
             padx=43,
             pady=20,
             command=sum_button,
             fg='#ffffff',
             activebackground='#ffffff',
             bg='#E38A1E',
             relief=FLAT,
             font=('futura', 12, 'bold')
             )
sum.grid(row=2, column=4)

n_seven = Button(root,
                 text='7',
                 padx=px,
                 pady=20,
                 command=lambda: click_button(7),
                 fg='#ffffff',
                 activebackground='#ffffff',
                 bg='#E38A1E',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
n_seven.grid(row=3, column=1)

n_eight = Button(root,
                 text='8',
                 padx=px,
                 pady=20,
                 command=lambda: click_button(8),
                 fg='#ffffff',
                 activebackground='#ffffff',
                 bg='#E38A1E',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
n_eight.grid(row=3, column=2)

n_nine = Button(root,
                text='9',
                padx=px,
                pady=20,
                command=lambda: click_button(9),
                fg='#ffffff',
                activebackground='#ffffff',
                bg='#E38A1E',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
n_nine.grid(row=3, column=3)

minus = Button(root,
               text='-',
               padx=45,
               pady=20,
               command=minus_button,
               fg='#ffffff',
               activebackground='#ffffff',
               bg='#E38A1E',
               relief=FLAT,
               font=('futura', 12, 'bold')
               )
minus.grid(row=3, column=4)


n_zero = Button(root,
                text='0',
                padx=91,
                pady=20,
                command=lambda: click_button(0),
                fg='#ffffff',
                activebackground='#ffffff',
                bg='#E38A1E',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
n_zero.grid(row=4, column=1, columnspan=2)

ac = Button(root,
            text='AC',
            padx=33,
            pady=20,
            command=ac_button,
            fg='#ffffff',
            activebackground='#ffffff',
            bg='#E38A1E',
            relief=FLAT,
            font=('futura', 12, 'bold')
            )
ac.grid(row=4, column=3)

total = Button(root,
               text='=',
               padx=43,
               pady=20,
               command=total_button,
               fg='#ffffff',
               activebackground='#ffffff',
               bg='#E38A1E',
               relief=FLAT,
               font=('futura', 12, 'bold')
               )
total.grid(row=4, column=4)


root.mainloop()


root.mainloop()
