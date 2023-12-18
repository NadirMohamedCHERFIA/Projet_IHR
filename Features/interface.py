from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import bcrypt
import re
import time
from configuration import *




main = Tk()
style = tb.Style(selected_theme)
main.title("Interface Robotique")
main.geometry(dimensions)


def handle_ip_text_change(ip_var):
    global valid_ip 
    print(ip_var.get())
    temp_ip = ip_var.get()
    if re.fullmatch(ip_pattern, temp_ip):
        valid_ip = True
        print('ip valid')
        ip_error_label.configure(text='')
    else:
        valid_ip= False
        print('ip non valid')
        ip_error_label.configure(text='Wrong IP format!',fg='red')
        ip_error_label.pack()

def handle_configuration_save():
    if valid_ip:
        IP = ip_entry.get()
        PORT = port_entry.get()
        submit_button.configure(text='Enregistrement terminé!',bootstyle='success',width=buttons_width,style='success.TButton')
        submit_button.after(500,lambda: submit_button.configure(text='Enregistrer', bootstyle='primary', style='primary.TButton'))
    else:
        print('Ip non valid')
def configuration_window_pack():
    header_label.configure(text='Configuration du protocole UDP!')
    ip_entry.delete(0,'end')
    port_entry.delete(0,'end')
    ip_label.pack(pady=(10,0))
    ip_entry.pack(pady=10)
    ip_error_label.pack()
    port_label.pack(pady=(10,0))
    port_entry.pack(pady=(10,30))
    submit_button.pack(pady=10)
    return_button.pack(pady=10)
    ip_entry.insert(0,IP)
    port_entry.insert(0,PORT)


def configuration_window_unpack():
    ip_label.pack_forget()
    ip_entry.pack_forget()
    ip_error_label.pack_forget()
    port_entry.pack_forget()
    port_label.pack_forget()
    ip_entry.pack_forget()
    submit_button.pack_forget()

def login_window_pack():
    first_window_unpack()
    username_entry.insert(0,'admin')
    header_label.configure(text='Login')
    username_label.pack(pady=(30,0))
    username_entry.pack(pady=10)
    password_label.pack()
    password_entry.pack(pady=(10,30))
    login_button.pack(pady=10)
    return_button.pack(pady=20)

def login_window_unpack():
    username_entry.pack_forget()
    password_entry.pack_forget()
    return_button.pack_forget()
    login_button.pack_forget()
    password_label.pack_forget()
    username_label.pack_forget()

def handle_login(username: str, password: str):
    if bcrypt.checkpw(password.encode('utf-8'), HASHED_PASSWORD) and username == 'admin':
        print("match")
        password_entry.delete(0, 'end')
        login_window_unpack()
        username_entry.delete(0, 'end')
        configuration_window_pack()
    else:
        print("does not match")


def logs_window_pack():
    header_label.configure(text='Logs')
    first_window_unpack()
    return_button.pack(pady=20)
    # pass

def first_window_pack():
    # packing
    header_label.configure(text='Welcome to our robotique control interface!')
    toggle_theme_button.pack(pady=(40, 20))
    header_label.pack(pady=(10, 10))
    getting_started_button.pack(pady=20)
    configuration_udp_button.pack(pady=20)
    logs_button.pack(pady=20)
    exit_button.pack(pady=20)
    return_button.pack_forget()

def first_window_unpack():
    # packing
    getting_started_button.pack_forget()
    configuration_udp_button.pack_forget()
    exit_button.pack_forget()
    logs_button.pack_forget()

def getting_started_window_pack():
    first_window_unpack()
    header_label.configure(text='Getting started!')
    activate_checkbox.pack(pady=(10,20))
    indicators_frame.pack()
    robot_indicator_frame.pack(padx=(30,40),side='left')
    robot_connection_canvas.pack()
    robot_connection_label.pack()
    udp_indicator_frame.pack(padx=(0, 30),side='left')
    udp_server_canvas.pack()
    udp_server_label.pack()
    main_frame.pack(pady=(0,20))
    directions_frame.pack(side='left',padx=(0,50))
    forward_button.pack(side='top',pady=10)
    backward_button.pack(side='bottom',pady=10)
    left_button.pack(side='left',pady=10,padx=10)
    right_button.pack(side='right',pady=10,padx=10)
    grab_frame.pack(side='right')
    grab_button.pack(pady=20)
    unlatch_button.pack(pady=20)
    stop_frame.pack()
    stop_button.pack()
    return_button.pack(pady=20)

def getting_started_window_unpack():
    activate_checkbox.pack_forget()
    indicators_frame.pack_forget()
    robot_indicator_frame.pack_forget()
    robot_connection_canvas.pack_forget()
    robot_connection_label.pack_forget()
    udp_indicator_frame.pack_forget()
    udp_server_canvas.pack_forget()
    udp_server_label.pack_forget()
    main_frame.pack_forget()
    directions_frame.pack_forget()
    forward_button.pack_forget()
    backward_button.pack_forget()
    left_button.pack_forget()
    right_button.pack_forget()
    grab_frame.pack_forget()
    grab_button.pack_forget()
    unlatch_button.pack_forget()
    stop_frame.pack_forget()
    stop_button.pack_forget()
    return_button.pack_forget()

def handle_activate_click():
    if activate_var.get()==1:
        activate_checkbox.configure(text='Activé', bootstyle='success.Toolbutton', width=buttons_width)
        forward_button.configure(state="enable")
        backward_button.configure(state='enable')
        left_button.configure(state='enable')
        right_button.configure(state='enable')
        grab_button.configure(state='enable')
        unlatch_button.configure(state='enable')

    else:
        activate_checkbox.configure(text='Activer', bootstyle='primary.Toolbutton', width=buttons_width)
        forward_button.configure(state='disabled')
        backward_button.configure(state='disabled')
        left_button.configure(state='disabled')
        right_button.configure(state='disabled')
        grab_button.configure(state='disabled')
        unlatch_button.configure(state='disabled')

def handle_forward_click():
    backward_var.set(0)
    pass

def handle_backward_click():
    forward_var.set(0)
    pass

def handle_left_click():
    right_var.set(0)
    pass

def handle_right_click():
    left_var.set(0)
    pass

def handle_grab_click():
    unlatch_var.set(0)
    pass

def handle_unlatch_click():
    grab_var.set(0)
    pass

def handle_stop_click():
    grab_var.set(0)
    unlatch_var.set(0)
    left_var.set(0)
    right_var.set(0)
    forward_var.set(0)
    backward_var.set(0)
    activate_var.set(0)
    pass

def handle_exit_button():
    main.destroy()

def handle_toggle_theme():
    if theme_var.get() == 0:
        selected_theme_label='Dark theme'
        tb.Style('darkly')
    else:
        selected_theme_label='Light theme'
        tb.Style('cosmo')
    toggle_theme_button.configure(text=selected_theme_label)


def handle_return():
    login_window_unpack()
    first_window_pack()
    configuration_window_unpack()
    getting_started_window_unpack()

#style
style = tb.Style()
style.configure('primary.TButton',font=(font_var,18,'bold'))
style.configure('success.TButton',font=(font_var,18,'bold'))
style.configure('danger.TButton', font=(font_var, 18, 'bold'))

#theme_toggle-chooser
theme_var = IntVar()
toggle_theme_button = tb.Checkbutton(
    main,
    text='Dark theme',
    bootstyle='primary,round-toggle',
    variable=theme_var,
    onvalue=1,
    offvalue=0,
    command=handle_toggle_theme
    )
#main window
    #header_label
header_label = tb.Label(
    main, 
    text='Bienvenue dans notre interface robotique',
    font=(font_var, 18, 'bold')
    )

    #buttons
getting_started_button = tb.Button(
    main,
    text='Getting started',
    bootstyle='primary',
    style='primary.TButton',
    width=buttons_width,
    command=getting_started_window_pack
    )

configuration_udp_button = tb.Button(
    main, 
    text='Configuration UDP',
    bootstyle='PRIMARY',
    style='primary.TButton',
    width=buttons_width,
    command=login_window_pack
    )

logs_button = tb.Button(
    main, 
    text='Logs',
    bootstyle='PRIMARY',
    style='primary.TButton',
    width=buttons_width,
    command=logs_window_pack
    )

exit_button = tb.Button(
    main,
    text='Exit',
    bootstyle='DANGER',
    style='danger.TButton',
    width=buttons_width,
    command=handle_exit_button
    )
return_button = tb.Button(
    main,
    text='Return',
    bootstyle='DANGER',
    style='danger.TButton',
    width=buttons_width,
    command=handle_return
    )

#login
    #Entries
username_entry = tb.Entry(
    main,
    text='Username :',
    width=entries_width
    )
password_entry = tb.Entry(
    main,
    text='Password',
    show='*',
    width=entries_width
    )

    #labels
username_label = tb.Label(text='Username')
password_label = tb.Label(text='Password')

    #buttons
login_button = tb.Button(
    main,
    text='Login',
    bootstyle='primary',
    style='primary.TButton',
    width=buttons_width,
    command= lambda: handle_login(username_entry.get(),password_entry.get())
    )


#getting started
    #main frame
main_frame = Frame(
    main,
    width=500,
    height=200,
    # highlightbackground='red',
    # highlightthickness=3
    )
    # indicators frames
indicators_frame = Frame(
    main,
    width=200,
    height=50,
    highlightbackground='grey',
    highlightthickness=1
)
    #indicator frame
robot_indicator_frame = Frame(
    indicators_frame,
    width=200,
    height=50,
    # highlightbackground='green'
    # highlightthickness=3,
)
udp_indicator_frame = Frame(
    indicators_frame,
    width=200,
    height=50,
    # highlightbackground='green',
    # highlightthickness=3
)

    # Control frames
directions_frame = Frame(
    main_frame,
    width=200,
    height=50,
    # highlightbackground='red',
    # highlightthickness=3
)
    #grab frame
grab_frame = Frame(
    main_frame,
    width=200,
    height=50,
    # highlightbackground='red',
    # highlightthickness=3
    )
    #stop frame
stop_frame = Frame(
    main,
    width=500,
    height=50,
    # highlightbackground='red',
    # highlightthickness=3
    )
    #canvas
robot_connection_canvas = Canvas(
    robot_indicator_frame,
    bg='ivory',
    width=30,
    height=30
    )
robot_connection_indicator = robot_connection_canvas.create_oval((0,0,20,20),fill='orange')
udp_server_canvas = Canvas(
    udp_indicator_frame,
    bg='ivory',
    width=30,
    height=30
    )
udp_server_indicator = udp_server_canvas.create_oval((0,0,20,20),fill='green')
    #labels
robot_connection_label = tb.Label(
    robot_indicator_frame,
    text='Robot connection'
    )
udp_server_label = tb.Label(
    udp_indicator_frame,
    text='UDP server'
    )
    #Buttons
activate_var = IntVar()
activate_checkbox = tb.Checkbutton(
    main,
    text='Activer',
    bootstyle='primary.Toolbutton',
    width=buttons_width,
    variable=activate_var,
    onvalue=1,
    offvalue=0,
    command=handle_activate_click
    )   
forward_var = IntVar()
forward_button = tb.Checkbutton(
    directions_frame,
    text='Forward',
    width=20,
    bootstyle='primary.Toolbutton',
    state='disabled',
    variable=forward_var,
    onvalue=1,
    offvalue=0,
    command=handle_forward_click
    )
backward_var = IntVar()
backward_button = tb.Checkbutton(
    directions_frame,
    text='Backward',
    width=20,
    bootstyle='primary.Toolbutton',
    state='disabled',
    variable=backward_var,
    onvalue=1,
    offvalue=0,
    command=handle_backward_click
    )
left_var = IntVar()
left_button = tb.Checkbutton(
    directions_frame,
    text='Left',
    width=20,
    bootstyle='primary.Toolbutton',
    state='disabled',
    variable=left_var,
    onvalue=1,
    offvalue=0,
    command=handle_left_click
    )
right_var = IntVar()
right_button = tb.Checkbutton(
    directions_frame,
    text='Right',
    width=20,
    bootstyle='primary.Toolbutton',
    state='disabled',
    variable=right_var,
    onvalue=1,
    offvalue=0,
    command=handle_right_click
    )
grab_var = IntVar()
grab_button = tb.Checkbutton(
    grab_frame,
    text='Grab',
    width=20,
    bootstyle='primary.Toolbutton',
    state='disabled',
    variable=grab_var,
    onvalue=1,
    offvalue=0,
    command=handle_grab_click
    )
unlatch_var = IntVar()
unlatch_button = tb.Checkbutton(
    grab_frame,
    text='Unlatch',
    width=20,
    bootstyle='primary primary.Toolbutton',
    state='disabled',
    variable=unlatch_var,
    onvalue=1,
    offvalue=0,
    command=handle_unlatch_click
    )

stop_button = tb.Button(
    stop_frame,
    text='Stop',
    width=buttons_width,
    bootstyle='danger',
    command=handle_stop_click
    )

#configuration udp
    #Entries
ip_var = StringVar()
ip_var.trace_add("write",lambda name,index,mode ,ip_var=ip_var : handle_ip_text_change(ip_var))

ip_entry = tb.Entry(
    main,
    text='IP',
    width=entries_width,
    textvariable=ip_var
    )
port_entry = tb.Entry(
    main,
    text='PORT',
    width=entries_width
    )

    #Labels
ip_label = tb.Label(
    main,
    text='IP Address'
    )
ip_error_label = Label(
    main,
    text='',
    fg='red'
    )
port_label = tb.Label(
    main,
    text='PORT'
    )
    #Buttons
submit_button = tb.Button(
    main,
    text='Enregistrer',
    bootstyle='primary',
    style='primary.TButton',
    width=buttons_width,
    command=handle_configuration_save
    )




first_window_pack()
main.mainloop()
