from tkinter import *

mainWindow = Tk()

mainWindow.title('Interface Humain Robot')

header = Label(mainWindow,text='Interface Robot',width=100)

connect_to_udp_button = Button(mainWindow,text='Connect to UDP',width=30,padx=5,bg='#034748',fg='white')
get_started_button = Button(mainWindow,text='Getting started',width=30,padx=5,bg='#034748',fg='white')
quit_button = Button(mainWindow, text='Quit', width=30,padx=5, bg='#8A3033', fg='white')

gap = Label(mainWindow,text=' ',height=5)

header.grid(column=0,row=0)
gap.grid(column=0,row=1)
connect_to_udp_button.grid(column=0,row=2)
gap.grid(column=0,row=3)
get_started_button.grid(column=0,row=4)
gap.grid(column=0,row=5)
quit_button.grid(column=0,row=6)
gap.grid(column=0,row=7)
mainWindow.mainloop()