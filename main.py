from tkinter import *

screen = Tk()
screen.title(" Converter ")
screen.minsize(height=50, width=80)
screen.config(padx=20, pady=20)

label1 = Label()
label1.config(text='Miles')
label1.grid(column=2, row=0)

label2 = Label()
label2.config(text='Is Equal to :')
label2.grid(column=0, row=1)

label3 = Label()
label3.config(text='Km')
label3.grid(column=1, row=1)

label4 = Label()
label4.config(text='0')
label4.grid(column=2, row=1)


def click_k():
    value = int(entry.get())
    km = value * 1.609
    label3.config(text=km)


button = Button(text='Calculate', command=click_k)
button.grid(column=1, row=2)

entry = Entry(width=10)
entry.get()
entry.grid(column=1, row=0)

screen.mainloop()
