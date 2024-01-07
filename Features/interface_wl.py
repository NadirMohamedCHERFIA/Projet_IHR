from tkinter import *
from tkinter import ttk
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
import bcrypt
import re
from PIL import ImageTk, Image
from configuration import *

' Last update by cherfia mohamed nadir please dont push to the main branch create a seperate one and submit a pull request have a nice day!"'

# colors
bgColor = '#0A1045'
whiteColor = "#F2F2F2"
dangerColor = '#F25757'
successColor = '#10FFCB'
secondaryColor = '#E0E2DB'
alertColor = '#E6AF2E'
primaryColor = '#2176FF'


#font
font_configuration_lg = (font_var,18,'bold')
font_configuration_md = (font_var,14,'bold')

main = Tk()
# style = tb.Style(selected_theme)
main.configure(bg=bgColor)
main.title("Interface Robotique")
main.iconbitmap('../src/images/Robot.png')
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
        submit_button.configure(
            text='Enregistrement terminé!',
            # bootstyle='success',
            width=buttons_width,
            font=font_configuration_lg
            # style='success.TButton'

            )
        submit_button.after(
            500,
            lambda: submit_button.configure(text='Enregistrer',
                                            font=font_configuration_lg,
                                            # bootstyle='primary',
                                            # style='primary.TButton'
                                            ))
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
    header_label.configure(text='Welcome to our robotique control interface!',bg=bgColor,fg=whiteColor)
    # toggle_theme_button.pack(pady=(40, 20))
    header_label.pack(pady=(10, 10))
    getting_started_button.pack(pady=(100,20))
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
    header_label.configure(text='Getting started!',bg=bgColor,fg=whiteColor)
    activate_checkbox.pack(pady=(10,20))
    stop_button.pack(pady=(0,20))
    indicators_frame.pack()
    robot_indicator_frame.pack(padx=(30,40),side='left')
    robot_connection_canvas.pack()
    robot_connection_label.pack()
    udp_indicator_frame.pack(padx=(0, 30),side='left')
    udp_server_canvas.pack()
    udp_server_label.pack()
    main_frame.pack(pady=(0,10))
    getting_started_images_frame.pack()
    body_img_frame.pack(side='left',padx=(150,150))
    label_body_image.pack(padx=50)
    # stop_frame.pack(side='left',pady=(20,10))
    label_head_image.pack(padx=50)
    head_img_frame.pack(side='left',padx=(250,0))
    directions_frame.pack(side='left',padx=(0,150))
    forward_button.pack(side='top',pady=(10,20))
    backward_button.pack(side='bottom',pady=(20,10))
    left_button.pack(side='left',pady=10,padx=10)
    right_button.pack(side='right',pady=10,padx=10)
    grab_frame.pack(side='right',padx=(20,20))
    head_frame.pack(side='right')
    head_up_button.pack(pady=20)
    head_down_button.pack(pady=20)
    grab_button.pack(pady=20)
    unlatch_button.pack(pady=20)
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
    getting_started_images_frame.pack_forget()
    body_img_frame.pack_forget()
    label_body_image.pack_forget()
    stop_frame.pack_forget()
    label_head_image.pack_forget()
    stop_button.pack_forget()
    head_img_frame.pack_forget()
    directions_frame.pack_forget()
    forward_button.pack_forget()
    backward_button.pack_forget()
    left_button.pack_forget()
    right_button.pack_forget()
    grab_frame.pack_forget()
    head_frame.pack_forget()
    head_closed_img_frame.forget()
    head_up_button.pack_forget()
    head_down_button.pack_forget()
    grab_button.pack_forget()
    unlatch_button.pack_forget()
    return_button.pack_forget()

def handle_activate_click():
    if activate_var.get()==1:
        activate_checkbox.configure(text='Activé', 
                                    # bootstyle='success.Toolbutton',
                                    width=buttons_width,
                                    bg=successColor,
                                    # fg=whiteColor
                                    )
        robot_connection_indicator = robot_connection_canvas.create_oval((0,0,20,20),fill='green')
        forward_button.configure(state="active")
        backward_button.configure(state='active')
        left_button.configure(state='active')
        right_button.configure(state='active')
        grab_button.configure(state='active')
        unlatch_button.configure(state='active')
        head_up_button.configure(state='active')
        head_down_button.configure(state='active')

    else:
        activate_checkbox.configure(text='Activer', 
                                    # bootstyle='primary.Toolbutton',
                                    bg=alertColor,
                                    width=buttons_width)
        robot_connection_indicator = robot_connection_canvas.create_oval((0,0,20,20),fill='orange')
        forward_button.configure(state='disabled')
        backward_button.configure(state='disabled')
        left_button.configure(state='disabled')
        right_button.configure(state='disabled')
        grab_button.configure(state='disabled')
        unlatch_button.configure(state='disabled')
        head_up_button.configure(state='disabled')
        head_down_button.configure(state='disabled')


def handle_forward_click():
    if(forward_var.get()==1):
        forward_button.configure(bg=primaryColor)
        backward_button.configure(bg=secondaryColor)
    else:
        forward_button.configure(bg=secondaryColor)
    backward_var.set(0)
    pass

def handle_backward_click():
    if(backward_var.get()==1):
        forward_var.set(0)
        backward_button.configure(bg=primaryColor)
        forward_button.configure(bg=secondaryColor)
    else:
        backward_button.configure(bg=secondaryColor)
    pass

def handle_left_click():
    if(left_var.get()==1):
        right_var.set(0)
        left_button.configure(bg=primaryColor)
        right_button.configure(bg=secondaryColor)
    else:
        left_button.configure(bg=secondaryColor)
    pass

def handle_right_click():
    if(right_var.get()==1):
        left_var.set(0)
        right_button.configure(bg=primaryColor)
        left_button.configure(bg=secondaryColor)
    else:
        right_button.configure(bg=secondaryColor)
    pass

def handle_grab_click():
    if(grab_var.get()==1):
        grab_button.configure(bg=primaryColor)
        unlatch_button.configure(bg=secondaryColor)
        unlatch_var.set(0)
        head_closed_img_frame.pack(side='left')
        head_closed_img_frame.configure(bg=bgColor)
        head_img_frame.forget()
        label_head_image_closed.pack(padx=50)
    else:
        grab_button.configure(bg=secondaryColor)
        label_head_image_closed.forget()
        head_closed_img_frame.forget()
        head_closed_img_frame.configure(bg=bgColor)
        head_img_frame.pack()
        grab_var.set(0)


def handle_unlatch_click():
    if(unlatch_var.get()==1):
        unlatch_button.configure(bg=primaryColor)
        grab_button.configure(bg=secondaryColor)
    else:
        unlatch_button.configure(bg=secondaryColor)

    label_head_image_closed.forget()
    head_closed_img_frame.forget()
    head_closed_img_frame.configure(bg=bgColor)
    head_img_frame.pack()
    grab_var.set(0)
    pass

def handle_head_up_click():
    head_down_var.set(0)
    pass

def handle_head_down_click():
    head_up_var.set(0)
    pass

def handle_stop_click():
    grab_var.set(0)
    unlatch_var.set(0)
    left_var.set(0)
    right_var.set(0)
    forward_var.set(0)
    backward_var.set(0)
    activate_var.set(0)
    head_up_var.set(0)
    head_down_var.set(0)
    handle_activate_click()
    pass

def handle_exit_button():
    main.destroy()

def handle_return():
    login_window_unpack()
    first_window_pack()
    configuration_window_unpack()
    getting_started_window_unpack()

#style
# style = tb.Style()
# style.configure('primary.TButton',font=(font_var,18,'bold'))
# style.configure('success.TButton',font=(font_var,18,'bold'))
# style.configure('danger.TButton', font=(font_var, 18, 'bold'))

#theme_toggle-chooser
# theme_var = IntVar()
# toggle_theme_button = Checkbutton(
#     main,
#     text='Dark theme',
#     # bootstyle='primary,round-toggle',
#     variable=theme_var,
#     onvalue=1,
#     offvalue=0,
#     command=handle_toggle_theme
#     )
#main window
    #header_label
header_label = Label(
    main, 
    text='Bienvenue dans notre interface robotique',
    font=(font_var, 18, 'bold')
    )

    #buttons
getting_started_button = Button(
    main,
    text='Getting started',
    # bootstyle='primary',
    # style='primary.TButton',
    width=buttons_width,
    font=font_configuration_lg,
    command=getting_started_window_pack
    )

configuration_udp_button = Button(
    main, 
    text='Configuration UDP',
    # bootstyle='PRIMARY',
    # style='primary.TButton',
    width=buttons_width,
    font=font_configuration_lg,
    command=login_window_pack
    )

logs_button = Button(
    main, 
    text='Logs',
    # bootstyle='PRIMARY',
    # style='primary.TButton',
    width=buttons_width,
    font=font_configuration_lg,
    command=logs_window_pack
    )

exit_button = Button(
    main,
    text='Exit',
    # bootstyle='DANGER',
    # style='danger.TButton',
    width=buttons_width,
    font=font_configuration_lg,
    command=handle_exit_button
    )
exit_button.configure(bg=dangerColor,fg=whiteColor)
return_button = Button(
    main,
    text='Return',
    width=buttons_width,
    font=font_configuration_lg,
    command=handle_return,
    bg=dangerColor,
    fg=whiteColor
    )

#login
    #Entries
username_entry = Entry(
    main,
    text='Username :',
    width=entries_width
    )
password_entry = Entry(
    main,
    text='Password',
    show='*',
    width=entries_width
    )

    #labels
username_label = Label(text='Username'
                    ,bg=bgColor,
                    fg=whiteColor,
                    font=font_configuration_lg
                    )
password_label = Label(text='Password'                       ,bg=bgColor,
                    fg=whiteColor,
                    font=font_configuration_lg
                    )

    #buttons
login_button = Button(
    main,
    text='Login',
    # bootstyle='primary',
    # style='primary.TButton',
    width=buttons_width,
    font=font_configuration_lg,
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
main_frame.configure(bg=bgColor)
    # indicators frames
indicators_frame = Frame(
    main,
    width=400,
    height=50,
    highlightbackground='grey',
    highlightthickness=1
)
indicators_frame.configure(bg=bgColor)
    #indicator frame
robot_indicator_frame = Frame(
    indicators_frame,
    width=400,
    height=50,
    # highlightbackground='gold',
    # highlightthickness=3,
)
robot_indicator_frame.configure(bg=bgColor)
udp_indicator_frame = Frame(
    indicators_frame,
    width=200,
    height=50,
    # highlightbackground='green',
    # highlightthickness=3
)
udp_indicator_frame.configure(bg=bgColor)
    #getting started images
getting_started_images_frame = Frame(
    main_frame,
    width=400,
    height=50,
    # highlightbackground='red',
    # highlightthickness=3
    )
getting_started_images_frame.configure(bg=bgColor)
    #body img frame
body_img_frame = Frame(
    getting_started_images_frame,
    width=200,
    height=50,
    # highlightbackground='red',
    # highlightthickness=3
    )
body_img_frame.configure(bg=bgColor)
    #head img frame
head_img_frame = Frame(
    getting_started_images_frame,
    width=50,
    height=50,
    # highlightbackground='green',
    # highlightthickness=3
    )
head_img_frame.configure(bg=bgColor)
head_closed_img_frame = Frame(
    getting_started_images_frame,
    width=50,
    height=50,
    # highlightbackground='gold',
    # highlightthickness=3
    )

    #head frame
head_frame = Frame(
    main_frame,
    width=50,
    height=50,
    # highlightbackground='red',
    # highlightthickness=3
    )
head_frame.configure(bg=bgColor)
    # Control frames
directions_frame = Frame(
    main_frame,
    width=200,
    height=50,
    # highlightbackground='red',
    # highlightthickness=3
)
directions_frame.configure(bg=bgColor)
    #grab frame
grab_frame = Frame(
    main_frame,
    width=200,
    height=50,
    # highlightbackground='green',
    # highlightthickness=3
    )
grab_frame.configure(bg=bgColor)
    #stop frame
stop_frame = Frame(
    getting_started_images_frame,
    # main,
    width=500,
    height=50,
    # highlightbackground='red',
    # highlightthickness=3
    )
stop_frame.configure(bg=bgColor)
    #images object
img_body = ImageTk.PhotoImage(Image.open("../src/images/body.png"))
img_head = ImageTk.PhotoImage(Image.open("../src/images/head.png"))
img_head_closed = ImageTk.PhotoImage(Image.open('../src/images/head-closed.png'))

    #canvas
robot_connection_canvas = Canvas(
    robot_indicator_frame,
    bg='ivory',
    width=30,
    height=30,
    highlightthickness=0
    )
robot_connection_canvas.configure(bg=bgColor)
robot_connection_indicator = robot_connection_canvas.create_oval((0,0,20,20),fill='orange')
udp_server_canvas = Canvas(
    udp_indicator_frame,
    bg='ivory',
    width=30,
    height=30,
    highlightthickness=0
    )
udp_server_canvas.configure(bg=bgColor)
udp_server_indicator = udp_server_canvas.create_oval((0,0,20,20),fill='green')
    #labels
label_body_image = Label(body_img_frame, image = img_body)
label_body_image.configure(bg=bgColor)
label_head_image = Label(head_img_frame, image = img_head)
label_head_image.configure(bg=bgColor)
label_head_image_closed = Label(head_closed_img_frame,image=img_head_closed)
label_head_image_closed.configure(bg=bgColor)
robot_connection_label = Label(
    robot_indicator_frame,
    text='Robot connection',
    font=font_configuration_lg
    )
robot_connection_label.configure(bg=bgColor,fg=whiteColor)
udp_server_label = Label(
    udp_indicator_frame,
    text='UDP server',
    font=font_configuration_lg
    )
udp_server_label.configure(bg=bgColor,fg=whiteColor)
    #Buttons
activate_var = IntVar()
# Create a custom style to hide the checkmark
# style = ttk.Style()
# style.layout('NoCheckmark.TCheckbutton', style.layout('TCheckbutton', []))
# style.configure('NoCheckmark.TCheckbutton',background='SystemButtonFace', foreground='SystemButtonFace')
activate_checkbox = Checkbutton(
    main,
    text='Activer',
    # bootstyle='primary.Toolbutton',
    width=buttons_width,
    font=font_configuration_lg,
    variable=activate_var,
    bg=alertColor,
    # style='NoCheckmark.TCheckbutton',
    onvalue=1,
    offvalue=0,
    command=handle_activate_click
    )   
forward_var = IntVar()
forward_button = Checkbutton(
    directions_frame,
    text='Forward',
    width=20,
    font=font_configuration_md,
    bg=secondaryColor,
    # bootstyle='primary.Toolbutton',
    state='disabled',
    variable=forward_var,
    onvalue=1,
    offvalue=0,
    command=handle_forward_click
    )
backward_var = IntVar()
backward_button = Checkbutton(
    directions_frame,
    text='Backward',
    width=20,
    font=font_configuration_md,
    bg=secondaryColor,
    # bootstyle='primary.Toolbutton',
    state='disabled',
    variable=backward_var,
    onvalue=1,
    offvalue=0,
    command=handle_backward_click
    )
left_var = IntVar()
left_button = Checkbutton(
    directions_frame,
    text='Left',
    width=20,
    font=font_configuration_md,
    bg=secondaryColor,
    # bootstyle='primary.Toolbutton',
    state='disabled',
    variable=left_var,
    onvalue=1,
    offvalue=0,
    command=handle_left_click
    )
right_var = IntVar()
right_button = Checkbutton(
    directions_frame,
    text='Right',
    width=20,
    font=font_configuration_md,
    bg=secondaryColor,
    # bootstyle='primary.Toolbutton',
    state='disabled',
    variable=right_var,
    onvalue=1,
    offvalue=0,
    command=handle_right_click
    )
grab_var = IntVar()
grab_button = Checkbutton(
    grab_frame,
    text='Grab',
    width=20,
    font=font_configuration_md,
    bg=secondaryColor,
    # bootstyle='primary.Toolbutton',
    state='disabled',
    variable=grab_var,
    onvalue=1,
    offvalue=0,
    command=handle_grab_click
    )
unlatch_var = IntVar()
unlatch_button =Checkbutton(
    grab_frame,
    text='Ungrab',
    width=20,
    font=font_configuration_md,
    bg=secondaryColor,
    # bootstyle='primary primary.Toolbutton',
    state='disabled',
    variable=unlatch_var,
    onvalue=1,
    offvalue=0,
    command=handle_unlatch_click
    )

head_up_var = IntVar()
head_up_button = Checkbutton(
    head_frame,
    text='Head up',
    width=20,
    font=font_configuration_md,
    bg=secondaryColor,
    # bootstyle='primary primary.Toolbutton',
    state='disabled',
    variable=head_up_var,
    onvalue=1,
    offvalue=0,
    command=handle_head_up_click
)
head_down_var = IntVar()
head_down_button = Checkbutton(
    head_frame,
    text='Head down',
    width=20,
    font=font_configuration_md,
    bg=secondaryColor,
    # bootstyle='primary primary.Toolbutton',
    state='disabled',
    variable=head_down_var,
    onvalue=1,
    offvalue=0,
    command=handle_head_down_click
)


stop_button = Button(
    # stop_frame,
    main,
    text='Stop',
    width=20,
    font=font_configuration_lg,
    # bootstyle='danger',
    command=handle_stop_click
    )
stop_button.configure(bg='#FF0000',fg=whiteColor)
#configuration udp
    #Entries
ip_var = StringVar()
ip_var.trace_add("write",lambda name,index,mode ,ip_var=ip_var : handle_ip_text_change(ip_var))

ip_entry = Entry(
    main,
    text='IP',
    width=entries_width,
    textvariable=ip_var
    )
port_entry = Entry(
    main,
    text='PORT',
    width=entries_width
    )

    #Labels
ip_label = Label(
    main,
    text='IP Address',
    bg=bgColor,
    fg=whiteColor,
    font=font_configuration_lg
    )
ip_error_label = Label(
    main,
    text='',
    fg='red',
    bg=bgColor
    )
port_label = Label(
    main,
    text='PORT',
    bg=bgColor,
    fg=whiteColor,
    font=font_configuration_lg
    )
    #Buttons
submit_button = Button(
    main,
    text='Enregistrer',
    # bootstyle='primary',
    # style='primary.TButton',
    width=buttons_width,
    font=font_configuration_lg,
    command=handle_configuration_save
    )




first_window_pack()
main.mainloop()
