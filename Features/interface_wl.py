from tkinter import *
import re
from PIL import ImageTk, Image
from configuration import *

import socket

' Last update by cherfia mohamed nadir please dont push to the main branch create a seperate one and submit a pull request have a nice day!"'
msgFromClient = ""
msgToClient = ""
# server info
serverAddressPort = (UDP_IP, UDP_PORT)

bufferSize = 1024
# colors
bgColor = '#0A1045'
whiteColor = "#F2F2F2"
dangerColor = '#F25757'
successColor = '#10FFCB'
secondaryColor = '#E0E2DB'
alertColor = '#E6AF2E'
primaryColor = '#2176FF'


# font
font_configuration_lg = (font_var, 18, 'bold')
font_configuration_md = (font_var, 14, 'bold')

main = Tk()
# style = tb.Style(selected_theme)
main.configure(bg=bgColor)
main.title("Interface Robotique")
# main.iconbitmap('../src/images/Robot.png')
main.geometry(dimensions)
checkCalled = False


def checkConnection():
    if (sendToUdp('c') == '200'):
        # here canvas draw green on robot status
        udp_connection_indicator = robot_connection_canvas.create_oval(
            (0, 0, 20, 20), fill='green')
        return True
    else:
        udp_connection_indicator = robot_connection_canvas.create_oval(
            (0, 0, 20, 20), fill='orange')
        return False

    # if (sendToUdp('d') == '404'):
    #     # here canvas draw orange on robot canvas
    #     udp_connection_indicator = robot_connection_canvas.create_oval(
    #         (0, 0, 20, 20), fill='orange')
    #     return False


def checkButtonsStatus():
    if(checkConnection==True):
        speed = (speed_var.get())
        if (speed >= 100 and speed < 200):
            sendToUdp('v') #level one speed
        if (speed >= 200 and speed < 280):
            sendToUdp('p') #level two speed

        if (speed >= 280 and speed <= 300):
            sendToUdp('k') #level three speed

        # stop linear
        if (forward_var.get() == False and backward_var.get() == False and left_var.get() == False and right_var.get() == False):
            sendToUdp('S')
            sendToUdp('A')
            sendToUdp('H')
        # Head stop
        if (head_up_var.get() == False and head_down_var.get() == False):
            sendToUdp('H')
        # stop gripper
        if (grab_var.get() == False and unlatch_var.get() == False):
            sendToUdp('S')
        # head up
        if (head_up_var.get() == True):
            sendToUdp('u')
        # head down
        if (head_down_var.get() == True):
            sendToUdp('D')
        # grab
        if (grab_var.get() == True):
            print("ss")
            sendToUdp('G')
        # ungrab
        if (unlatch_var.get() == True):
            sendToUdp('U')
        # Forward
        if (forward_var.get() == True):
            sendToUdp('F')
        # backward
        if (backward_var.get() == True):
            sendToUdp('B')
        # left
        if (left_var.get() == True and right_var.get() == False):
            sendToUdp('L')
        # right
        if (right_var.get() == True and left_var.get() == False):
            sendToUdp('R')
    else:
        print("Connection to udp not possible")
        activate_var.set(False)
        handle_activate_click

def sendToUdp(msg):
    # format the message to send
    bytesToSend = str.encode(str(msg))
    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)


def handle_ip_text_change(ip_var):
    global valid_ip
    print(ip_var.get())
    temp_ip = ip_var.get()
    if re.fullmatch(ip_pattern, temp_ip):
        valid_ip = True
        print('ip valid')
        ip_error_label.configure(text='')
    else:
        valid_ip = False
        print('ip non valid')
        ip_error_label.configure(text='Wrong IP format!', fg='red')
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
    ip_entry.delete(0, 'end')
    port_entry.delete(0, 'end')
    ip_label.pack(pady=(10, 0))
    ip_entry.pack(pady=10)
    ip_error_label.pack()
    port_label.pack(pady=(10, 0))
    port_entry.pack(pady=(10, 30))
    submit_button.pack(pady=10)
    return_button.pack(pady=10)
    ip_entry.insert(0, IP)
    port_entry.insert(0, PORT)


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
    username_entry.insert(0, 'admin')
    header_label.configure(text='Login')
    username_label.pack(pady=(30, 0))
    username_entry.pack(pady=10)
    password_label.pack()
    password_entry.pack(pady=(10, 30))
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
    if password == 'admin' and username == 'admin':
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
    header_label.configure(
        text='welcome to our robotic interface', bg=bgColor, fg=whiteColor)
    # toggle_theme_button.pack(pady=(40, 20))
    header_label.pack(pady=(10, 10))
    welcome_window_img_frame.pack()
    label_body_welcome_image.pack()
    getting_started_button.pack(pady=(20, 20))
    configuration_udp_button.pack(pady=20)
    logs_button.pack(pady=20)
    exit_button.pack(pady=20)
    return_button.pack_forget()


def first_window_unpack():
    # packing
    welcome_window_img_frame.forget()
    getting_started_button.pack_forget()
    configuration_udp_button.pack_forget()
    exit_button.pack_forget()
    logs_button.pack_forget()


def getting_started_window_pack():
    first_window_unpack()
    header_label.configure(text='Control Panel', bg=bgColor, fg=whiteColor)
    activate_checkbox.pack(pady=(10, 20))
    stop_button.pack(pady=(0, 20))
    indicators_frame.pack()
    robot_indicator_frame.pack(padx=(30, 40), side='left')
    robot_connection_canvas.pack()
    robot_connection_label.pack()
    udp_indicator_frame.pack(padx=(0, 30), side='left')
    udp_server_canvas.pack()
    udp_server_label.pack()
    scale_frame.pack()
    scale_label.pack(side='left')
    speed_scale.pack()
    main_frame.pack(pady=(0, 10))
    getting_started_images_frame.pack()
    body_img_frame.pack(side='left', padx=(150, 150))
    label_body_image.pack(padx=50)
    # stop_frame.pack(side='left',pady=(20,10))
    label_head_image.pack(padx=50)
    head_img_frame.pack(side='left', padx=(250, 0))
    directions_frame.pack(side='left', padx=(0, 150))
    forward_button.pack(side='top', pady=(10, 20))
    backward_button.pack(side='bottom', pady=(20, 10))
    left_button.pack(side='left', pady=10, padx=10)
    right_button.pack(side='right', pady=10, padx=10)
    grab_frame.pack(side='right', padx=(20, 20))
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
    scale_frame.forget()
    scale_label.forget()
    speed_scale.forget()
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


def activate_clicked():
    activate_var.set(not (activate_var.get()))
    handle_activate_click()


def handle_activate_click():
    print(activate_var.get())
    if activate_var.get() == True:
        activate_checkbox.configure(text='Activé',
                                    width=buttons_width,
                                    bg=successColor,
                                    )
        # robot_connection_indicator = robot_connection_canvas.create_oval(
        #     (0, 0, 20, 20), fill='green')
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
                                    bg=alertColor,
                                    width=buttons_width)
        # robot_connection_indicator = robot_connection_canvas.create_oval(
        #     (0, 0, 20, 20), fill='orange')
        forward_button.configure(state='disabled')
        backward_button.configure(state='disabled')
        left_button.configure(state='disabled')
        right_button.configure(state='disabled')
        grab_button.configure(state='disabled')
        unlatch_button.configure(state='disabled')
        head_up_button.configure(state='disabled')
        head_down_button.configure(state='disabled')
        forward_var.set(False)
        backward_var.set(False)
        left_var.set(False)
        right_var.set(False)
        grab_var.set(False)
        unlatch_var.set(False)
        head_up_var.set(False)
        head_down_var.set(False)
        handle_forward_click
        handle_backward_click
        handle_left_click
        handle_right_click
        handle_grab_click
        handle_unlatch_click
        handle_head_up_click
        handle_head_down_click


def handle_forward_click(e):
    if(activate_var.get()==True):
        forward_var.set(True)
        forward_button.configure(bg=primaryColor)
        print(forward_var.get())
        backward_button.configure(bg=secondaryColor)
        backward_var.set(False)
        backward_button.configure(bg=secondaryColor)
        left_var.set(False)
        left_button.configure(bg=secondaryColor)
        right_var.set(False)
        right_button.configure(bg=secondaryColor)
        checkButtonsStatus()
    # pass


def handle_forward_on_release(event):
    forward_var.set(False)
    forward_button.configure(bg=secondaryColor)
    checkButtonsStatus()

def handle_backward_click(event):
    if(activate_var.get()==True):
        backward_var.set(True)
        forward_var.set(False)
        backward_button.configure(bg=primaryColor)
        forward_button.configure(bg=secondaryColor)
        forward_var.set(False)
        forward_button.configure(bg=secondaryColor)
        left_var.set(False)
        left_button.configure(bg=secondaryColor)
        right_var.set(False)
        right_button.configure(bg=secondaryColor)
        checkButtonsStatus()
        pass


def handle_backward_on_release(event):
    backward_var.set(False)
    backward_button.configure(bg=secondaryColor)
    checkButtonsStatus()

def handle_left_click(event):
    if(activate_var.get()==True):
        left_var.set(True)
        right_var.set(False)
        left_button.configure(bg=primaryColor)
        right_button.configure(bg=secondaryColor)
        forward_var.set(False)
        forward_button.configure(bg=secondaryColor)
        backward_var.set(False)
        backward_button.configure(bg=secondaryColor)
        right_var.set(False)
        right_button.configure(bg=secondaryColor)
        checkButtonsStatus()
        pass


def handle_left_on_release(event):
    left_var.set(False)
    left_button.configure(bg=secondaryColor)
    checkButtonsStatus()

def handle_right_click(event):
    if(activate_var.get()==True):
        right_var.set(True)
        left_var.set(False)
        right_button.configure(bg=primaryColor)
        left_button.configure(bg=secondaryColor)
        forward_var.set(False)
        forward_button.configure(bg=secondaryColor)
        backward_var.set(False)
        backward_button.configure(bg=secondaryColor)
        left_var.set(False)
        left_button.configure(bg=secondaryColor)
        checkButtonsStatus()
        pass


def handle_right_on_release(event):
    right_var.set(False)
    right_button.configure(bg=secondaryColor)
    checkButtonsStatus()


def handle_grab_click(event):
    if(activate_var.get()==True):
        grab_var.set(True)
        grab_button.configure(bg=primaryColor)
        unlatch_button.configure(bg=secondaryColor)
        unlatch_var.set(False)
        head_closed_img_frame.pack(side='left', padx=(250, 0))
        head_closed_img_frame.configure(bg=bgColor)
        head_img_frame.forget()
        label_head_image_closed.pack(padx=50)
        checkButtonsStatus()


def handle_grab_on_release(event):
    grab_button.configure(bg=secondaryColor)
    label_head_image_closed.forget()
    head_closed_img_frame.forget()
    head_closed_img_frame.configure(bg=bgColor)
    head_img_frame.pack(side='left', padx=(250, 0))
    grab_var.set(False)
    checkButtonsStatus()

def handle_unlatch_click(event):
    if(activate_var.get()==True):
        unlatch_var.set(True)
        unlatch_button.configure(bg=primaryColor)
        grab_button.configure(bg=secondaryColor)
        label_head_image_closed.forget()
        head_closed_img_frame.forget()
        head_closed_img_frame.configure(bg=bgColor)
        head_img_frame.pack()
        grab_var.set(False)
        checkButtonsStatus()
        pass


def handle_unlatch_on_release(event):
    unlatch_button.configure(bg=secondaryColor)
    unlatch_var.set(False)
    checkButtonsStatus()

def handle_head_up_click(event):
    if(activate_var.get()==True):
        head_up_var.set(True)
        head_down_var.set(False)
        head_up_button.configure(bg=primaryColor)
        head_down_button.configure(bg=secondaryColor)
        checkButtonsStatus()
        pass


def handle_head_up_on_release(event):
    head_up_button.configure(bg=secondaryColor)
    head_up_var.set(False)
    checkButtonsStatus()

def handle_head_down_click(event):
    if(activate_var.get()==True):
        head_down_var.set(True)
        head_up_var.set(False)
        head_down_button.configure(bg=primaryColor)
        head_up_button.configure(bg=secondaryColor)
        checkButtonsStatus()
        pass


def handle_head_down_on_release(event):
    head_down_button.configure(bg=secondaryColor)
    head_down_var.set(False)
    checkButtonsStatus()


def handle_stop_click():
    grab_var.set(False)
    unlatch_var.set(False)
    left_var.set(False)
    right_var.set(False)
    forward_var.set(False)
    backward_var.set(False)
    activate_var.set(False)
    head_up_var.set(False)
    head_down_var.set(False)
    handle_activate_click()
    checkButtonsStatus()
    pass


def handle_exit_button():
    main.destroy()


def handle_return():
    activate_var.set(False)
    handle_activate_click()
    login_window_unpack()
    first_window_pack()
    configuration_window_unpack()
    getting_started_window_unpack()


# main window
    # header_label
header_label = Label(
    main,
    text='Bienvenue dans notre interface robotique',
    font=(font_var, 18, 'bold')
)

welcome_window_img_frame = Frame(
    # main,
    width=300,
    height=200,
)
welcome_window_img_frame.configure(bg=bgColor)
img_welcome = ImageTk.PhotoImage(Image.open("../src/images/logo_red.png"))
label_body_welcome_image = Label(welcome_window_img_frame, image=img_welcome)
label_body_welcome_image.configure(bg=bgColor)
# buttons
getting_started_button = Button(
    main,
    text='Getting started',
    width=buttons_width,
    font=font_configuration_lg,
    command=getting_started_window_pack
)

configuration_udp_button = Button(
    main,
    text='UDP configuration',
    width=buttons_width,
    font=font_configuration_lg,
    command=login_window_pack
)

logs_button = Button(
    main,
    text='Logs',
    width=buttons_width,
    font=font_configuration_lg,
    command=logs_window_pack
)

exit_button = Button(
    main,
    text='Exit',
    width=buttons_width,
    font=font_configuration_lg,
    command=handle_exit_button
)
exit_button.configure(bg=dangerColor, fg=whiteColor)
return_button = Button(
    main,
    text='Return',
    width=buttons_width,
    font=font_configuration_lg,
    command=handle_return,
    bg=dangerColor,
    fg=whiteColor
)

# login
# Entries
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

# labels
username_label = Label(text='Username', bg=bgColor,
                       fg=whiteColor,
                       font=font_configuration_lg
                       )
password_label = Label(text='Password', bg=bgColor,
                       fg=whiteColor,
                       font=font_configuration_lg
                       )

# buttons
login_button = Button(
    main,
    text='Login',
    width=buttons_width,
    font=font_configuration_lg,
    command=lambda: handle_login(username_entry.get(), password_entry.get())
)


# getting started
# main frame
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
# indicator frame
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
# getting started images
getting_started_images_frame = Frame(
    main_frame,
    width=400,
    height=50,
    # highlightbackground='red',
    # highlightthickness=3
)
getting_started_images_frame.configure(bg=bgColor)
# body img frame
body_img_frame = Frame(
    getting_started_images_frame,
    width=200,
    height=50,
    # highlightbackground='red',
    # highlightthickness=3
)
body_img_frame.configure(bg=bgColor)
# head img frame
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

# head frame
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
# grab frame
grab_frame = Frame(
    main_frame,
    width=200,
    height=50,
    # highlightbackground='green',
    # highlightthickness=3
)
grab_frame.configure(bg=bgColor)
# stop frame
stop_frame = Frame(
    getting_started_images_frame,
    # main,
    width=500,
    height=50,
    # highlightbackground='red',
    # highlightthickness=3
)
stop_frame.configure(bg=bgColor)
# images object
img_body = ImageTk.PhotoImage(Image.open("../src/images/body.png"))
img_head = ImageTk.PhotoImage(Image.open("../src/images/head.png"))
img_head_closed = ImageTk.PhotoImage(
    Image.open('../src/images/head-closed.png'))

# canvas
robot_connection_canvas = Canvas(
    robot_indicator_frame,
    bg='ivory',
    width=30,
    height=30,
    highlightthickness=0
)
robot_connection_canvas.configure(bg=bgColor)
robot_connection_indicator = robot_connection_canvas.create_oval(
    (0, 0, 20, 20), fill='orange')
udp_server_canvas = Canvas(
    udp_indicator_frame,
    bg='ivory',
    width=30,
    height=30,
    highlightthickness=0
)
udp_server_canvas.configure(bg=bgColor)
udp_server_indicator = udp_server_canvas.create_oval(
    (0, 0, 20, 20), fill='green')
# labels
label_body_image = Label(body_img_frame, image=img_body)
label_body_image.configure(bg=bgColor)
label_head_image = Label(head_img_frame, image=img_head)
label_head_image.configure(bg=bgColor)
label_head_image_closed = Label(head_closed_img_frame, image=img_head_closed)
label_head_image_closed.configure(bg=bgColor)
robot_connection_label = Label(
    robot_indicator_frame,
    text='Robot connection',
    font=font_configuration_lg
)
robot_connection_label.configure(bg=bgColor, fg=whiteColor)
udp_server_label = Label(
    udp_indicator_frame,
    text='UDP server',
    font=font_configuration_lg
)
udp_server_label.configure(bg=bgColor, fg=whiteColor)
# Buttons
activate_var = BooleanVar()
activate_checkbox = Button(
    main,
    text='Activer',
    width=buttons_width,
    font=font_configuration_lg,
    bg=alertColor,
    command=activate_clicked
)
forward_var = BooleanVar()
forward_var.set(False)
forward_button = Button(
    directions_frame,
    text='Forward',
    width=20,
    height=2,
    font=font_configuration_md,
    bg=secondaryColor,
    state='disabled',
    # command=handle_forward_click
)
# forward_button.configure(height=20)
forward_button.bind("<ButtonPress>", lambda event: handle_forward_click(event))
forward_button.bind("<ButtonRelease>", handle_forward_on_release)
backward_var = BooleanVar()
backward_var.set(False)
backward_button = Button(
    directions_frame,
    text='Backward',
    width=20,
    height=2,
    font=font_configuration_md,
    bg=secondaryColor,
    state='disabled',
    # command=backward_clicked
)
backward_button.bind("<ButtonPress>", handle_backward_click)
backward_button.bind("<ButtonRelease>", handle_backward_on_release)
left_var = BooleanVar()
left_var.set(False)
left_button = Button(
    directions_frame,
    text='Left',
    width=20,
    height=2,
    font=font_configuration_md,
    bg=secondaryColor,
    state='disabled',
    # command=left_clicked
)
left_button.bind("<ButtonPress>", handle_left_click)
left_button.bind("<ButtonRelease>", handle_left_on_release)
right_var = BooleanVar()
right_var.set(False)
right_button = Button(
    directions_frame,
    text='Right',
    width=20,
    height=2,
    font=font_configuration_md,
    bg=secondaryColor,
    state='disabled',
    # command=right_clicked
)
right_button.bind("<ButtonPress>", handle_right_click)
right_button.bind("<ButtonRelease>", handle_right_on_release)
grab_var = BooleanVar()
grab_var.set(False)
grab_button = Button(
    grab_frame,
    text='Grab',
    width=20,
    height=3,
    font=font_configuration_md,
    bg=secondaryColor,
    state='disabled',
    # command=grab_clicked
)
grab_button.bind("<ButtonPress>", handle_grab_click)
grab_button.bind("<ButtonRelease>", handle_grab_on_release)

unlatch_var = BooleanVar()
unlatch_var.set(False)
unlatch_button = Button(
    grab_frame,
    text='Ungrab',
    width=20,
    height=3,
    font=font_configuration_md,
    bg=secondaryColor,
    state='disabled',
    # command=unlatch_clicked
)
unlatch_button.bind("<ButtonPress>", handle_unlatch_click)
unlatch_button.bind("<ButtonRelease>", handle_unlatch_on_release)
head_up_var = BooleanVar()
head_up_button = Button(
    head_frame,
    text='Head up',
    width=20,
    height=3,
    font=font_configuration_md,
    bg=secondaryColor,
    state='disabled',
    # command=head_up_clicked
)

head_up_button.bind("<ButtonPress>", handle_head_up_click)
head_up_button.bind("<ButtonRelease>", handle_head_up_on_release)

head_down_var = BooleanVar()
head_down_button = Button(
    head_frame,
    text='Head down',
    width=20,
    height=3,
    font=font_configuration_md,
    bg=secondaryColor,
    state='disabled',
    # command=head_down_clicked
)

head_down_button.bind("<ButtonPress>", handle_head_down_click)
head_down_button.bind("<ButtonRelease>", handle_head_down_on_release)

stop_button = Button(
    # stop_frame,
    main,
    text='Stop',
    width=20,
    font=font_configuration_lg,
    command=handle_stop_click
)
stop_button.configure(bg='#FF0000', fg=whiteColor)
# configuration udp
# Entries
ip_var = StringVar()
ip_var.trace_add("write", lambda name, index, mode,
                 ip_var=ip_var: handle_ip_text_change(ip_var))

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

# Labels
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
# Buttons
submit_button = Button(
    main,
    text='Enregistrer',
    width=buttons_width,
    font=font_configuration_lg,
    command=handle_configuration_save
)

# scale fram

scale_frame = Frame(
    main,
    bg=bgColor,
    highlightbackground=bgColor,
    highlightthickness=0
)
# scale label

scale_label = Label(
    scale_frame,
    text="Speed : ",
    font=font_configuration_lg

)
scale_label.configure(
    bg=bgColor,
    fg=whiteColor
)
# scale
speed_var = DoubleVar()
speed_scale = Scale(
    scale_frame,
    from_=100,
    to=300,
    bg=bgColor,
    fg=whiteColor,
    orient=HORIZONTAL,
    variable=speed_var
)


first_window_pack()
main.mainloop()
