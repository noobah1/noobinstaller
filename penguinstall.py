# import stuff
import tkinter
import customtkinter
from tkinter import *
import webbrowser
from PIL import Image, ImageTk, ImageDraw
import time
#d["mint"] += 1 = 0
#d["ubuntu"] += 1
#d["pop"] += 1
#d["elementary"] += 1
#d["debian"] += 1
#d["manjaro"] += 1
#d["fedora"] += 1
#d["garuda"] += 1
#d["arch"] += 1
#d["gentoo"] += 1

d = {'mint': 0, 'ubuntu': 0, 'pop': 0, 'elementary': 0, 'debian': 0, 'manjaro': 0, 'fedora': 0, 'garuda': 0, 'arch': 0, 'gentoo': 0}

#defining questionsx
q1 = None
q2 = None
q3 = None
q4 = None

# functions
def questionscreen1(): # complete!
    global q1 #declaring questions as global
    # function to clear the screen and print selected option (for debug purposes)
    def clearscreen1():
        selection = str(q1.get())
        print(selection)
        # if selection == 1: # windows
        if q1.get() == 1:
            d["mint"] += 1
            d["manjaro"] += 1
            d["garuda"] += 1
            d["arch"] += 1
            d["gentoo"] += 1
        elif q1.get() == 2: # mac
            d["ubuntu"] += 1
            d["pop"] += 1
            d["elementary"] += 1
            d["debian"] += 1
            d["fedora"] += 1
            d["garuda"] += 1
            d["arch"] += 1
            d["gentoo"] += 1
        else:
            print("idklmaoooo")
        questiontitle1.place_forget()
        continuebutton.place_forget()
        rb1.place_forget()
        rb2.place_forget()
        rb3.place_forget()

    # clear the title screen elements
    imgbgs.place_forget()
    startbutton.place_forget()
    # self explanatory
    print("question screen 1 display successful")
    # BACKGROUND IMAGE
    global imgbgref
    imgbgref = None
    imgbgref = ImageTk.PhotoImage(Image.open('./images/backgrounds/bg.png'))
    global imgbg
    imgbg = None
    imgbg = Label(main, image=imgbgref)
    imgbg.place(x = -0.5, y = -0.5)
    # adds question screen
    questiontitle1 = Label(main, font=Font_title, bg='#f5f5f5', fg='#4a4a4a', text='Which OS do\nyou prefer?')
    questiontitle1.place(relx = 0.265, rely = 0.25, anchor = CENTER)
    # selection buttons
    q1 = IntVar()
    rb1=customtkinter.CTkRadioButton(main, text=' Windows', font = Font_checkbox, text_color='#4a4a4a', bg_color='#f5f5f5', radiobutton_width=50, radiobutton_height=50, corner_radius=10, border_width_checked=10, variable=q1, value=1)
    rb2=customtkinter.CTkRadioButton(main, text=' MacOS', font = Font_checkbox, text_color='#4a4a4a', bg_color='#f5f5f5', radiobutton_width=50, radiobutton_height=50, corner_radius=10, border_width_checked=10, variable=q1, value=2)
    rb3=customtkinter.CTkRadioButton(main, text=" I don't know", font = Font_checkbox, text_color='#4a4a4a', bg_color='#f5f5f5', radiobutton_width=50, radiobutton_height=50, corner_radius=10, border_width_checked=10, variable=q1, value=3)
    rb1.place(relx = 0.15, rely = 0.4, anchor = W)
    rb2.place(relx = 0.15, rely = 0.5, anchor = W)
    rb3.place(relx = 0.15, rely = 0.6, anchor = W)
    # continue button
    continuebutton = Button(main, text='Continue', bg='#f5f5f5', fg='#4a4a4a', font=Font_button, width=10, bd=15, relief=RAISED, command=lambda: [clearscreen1(), questionscreen2()])
    continuebutton.place(relx = 0.265, rely = 0.8, anchor = CENTER)

    #animegirl
    global imgfgref
    global imgfgs
    imgfgs = None
    imgfgref = None
    imgfgref = ImageTk.PhotoImage(Image.open('./images/backgrounds/animegirl.png'))
    imgfgs = Label(main, image=imgfgref, highlightthickness=0, bd=0)
    imgfgs.place(relx = 0.55, y = 130)


def questionscreen2(): # complete!
    global q2
    def clearscreen2():
        selection = str(q2.get())
        print(selection)
        if q2.get() == 1:
            d["mint"] += 3
            d["ubuntu"] += 2
            d["pop"] += 1
        elif q2.get() == 2:
            d["mint"] += 2
            d["ubuntu"] += 3
            d["pop"] += 2
            d["elementary"] += 1
        elif q2.get() == 3:
            d["mint"] += 1
            d["ubuntu"] += 2
            d["pop"] += 3
            d["elementary"] += 2
            d["debian"] += 1
        elif q2.get() == 4:
            d["ubuntu"] += 1
            d["pop"] += 2
            d["elementary"] += 3
            d["debian"] += 2
            d["manjaro"] += 1
        elif q2.get() == 5:
            d["pop"] += 1
            d["elementary"] += 2
            d["debian"] += 3
            d["manjaro"] += 2
            d["fedora"] += 1
        elif q2.get() == 6:
            d["elementary"] += 1
            d["debian"] += 2
            d["manjaro"] += 3
            d["fedora"] += 2
            d["garuda"] += 1
        elif q2.get() == 7:
            d["debian"] += 1
            d["manjaro"] += 2
            d["fedora"] += 3
            d["garuda"] += 2
            d["arch"] += 1
        elif q2.get() == 8:
            d["manjaro"] += 1
            d["fedora"] += 2
            d["garuda"] += 3
            d["arch"] += 2
            d["gentoo"] += 1
        elif q2.get() == 9:
            d["fedora"] += 1
            d["garuda"] += 2
            d["arch"] += 3
            d["gentoo"] += 2
        elif q2.get() == 10:
            d["garuda"] += 1
            d["arch"] += 2
            d["gentoo"] += 3
        questiontitle2.place_forget()
        questionsubtitle2.place_forget()
        continuebutton2.place_forget()
        scale.place_forget()
        snl.place_forget()
    print("question screen 2 display successful")
    # adds question screen
    questiontitle2 = Label(main, font=Font_title, bg='#f5f5f5', fg='#4a4a4a', text='How familiar\nare you with\nLinux?')
    questiontitle2.place(relx = 0.265, rely = 0.25, anchor = CENTER)
    questionsubtitle2 = Label(main, font =Font_button, bg='#f5f5f5', fg='#4a4a4a', text='1 - Not at all\n10 - Very familiar')
    questionsubtitle2.place(relx = 0.265, rely = 0.5, anchor = CENTER)
    # selection scale
    q2 = IntVar()
    snl = Label(main, font=Font_button, bg='#f5f5f5', fg='#4a4a4a', text='h', textvariable=q2) # snl stands for slidernumberlabel
    snl.place(relx = 0.265, rely = 0.7, anchor = CENTER)
    def slidernumber():
        thething = 1
        if q2.get() == 1:
            snl.config(text='1')
        elif q2.get() == 2:
            snl.config(text='2')
        elif q2.get() == 3:
            snl.config(text='3')
        elif q2.get() == 4:
            snl.config(text='4')
        elif q2.get() == 5:
            snl.config(text='5')
        elif q2.get() == 6:
            snl.config(text='6')
        elif q2.get() == 7:
            snl.config(text='7')
        elif q2.get() == 8:
            snl.config(text='8')
        elif q2.get() == 9:
            snl.config(text='9')
        elif q2.get() == 10:
            snl.config(text='10')
    scale = customtkinter.CTkSlider(main, variable=q2, width=300, height=50, from_=1, to=10, orientation="horizontal", number_of_steps=9, border_width=10, bg_color='#f5f5f5',  button_color='#a1a1a1', button_hover_color='#dddddd', command=slidernumber)
    scale.place(relx = 0.265, rely = 0.65, anchor = CENTER)
    # continue button
    continuebutton2 = Button(main, text='Continue', bg='#f5f5f5', fg='#4a4a4a', font=Font_button, width=10, bd=15, relief=RAISED, command=lambda: [clearscreen2(), questionscreen3()])
    continuebutton2.place(relx = 0.265, rely = 0.8, anchor = CENTER)

def questionscreen3():
    global q3
    # function to clear the screen (will be used by continuebutton)
    def clearscreen3():
        #selection = "selected option " + str(q3.get())
        #print(selection)
        if q3_1.get() == 1: #gaming
            d["mint"] += 2
            d["ubuntu"] += 1
            d["pop"] += 2
            d["elementary"] += 1
            d["debian"] += 1
            d["manjaro"] += 1
            d["fedora"] += 1
            d["garuda"] += 2
            d["arch"] += 2
            d["gentoo"] += 1
        elif q3_2.get() == 2: #programming
            d["mint"] += 1
            d["ubuntu"] += 1
            d["pop"] += 1
            d["elementary"] += 1
            d["debian"] += 2
            d["manjaro"] += 2
            d["fedora"] += 2
            d["garuda"] += 1
            d["arch"] += 2
            d["gentoo"] += 2
        elif q3_3.get() == 3: #work
            d["mint"] += 2
            d["ubuntu"] += 2
            d["pop"] += 1
            d["elementary"] += 2
            d["debian"] += 2
            d["manjaro"] += 1
            d["fedora"] += 1
            d["garuda"] += 1
            d["arch"] += 1
            d["gentoo"] += 1
        questiontitle3.place_forget()
        continuebutton3.place_forget()
        cb1b.place_forget()
        cb2b.place_forget()
        cb3b.place_forget()
    # self explanatory
    print("question screen 3 display successful")
    # adds question screen
    questiontitle3 = Label(main, font=Font_title, bg='#f5f5f5', fg='#4a4a4a', text='What are you\ngoing to use\nLinux for?')
    questiontitle3.place(relx = 0.265, rely = 0.25, anchor = CENTER)
    # selection buttons (multiple select)
    q3_1 = IntVar()
    q3_2 = IntVar()
    q3_3 = IntVar()
    cb1b=customtkinter.CTkCheckBox(main, text='Gaming', font = Font_checkbox, text_color='#4a4a4a', bg_color='#f5f5f5', checkbox_width=50, checkbox_height=50, corner_radius=10, variable=q3_1)
    cb2b=customtkinter.CTkCheckBox(main, text='Programming', font = Font_checkbox, text_color='#4a4a4a', bg_color='#f5f5f5', checkbox_width=50, checkbox_height=50, corner_radius=10, variable=q3_2)
    cb3b=customtkinter.CTkCheckBox(main, text='Work', font = Font_checkbox, text_color='#4a4a4a', bg_color='#f5f5f5', checkbox_width=50, checkbox_height=50, corner_radius=10, variable=q3_3)
    cb1b.place(relx = 0.15, rely = 0.4, anchor = W)
    cb2b.place(relx = 0.15, rely = 0.5, anchor = W)
    cb3b.place(relx = 0.15, rely = 0.6, anchor = W)
    # continue button
    continuebutton3 = Button(main, text='Continue', bg='#f5f5f5', fg='#4a4a4a', font=Font_button, width=10, bd=15, relief=RAISED, command=lambda: [clearscreen3(), questionscreen4()]) # CHANGE TO 4!!!!!!
    continuebutton3.place(relx = 0.265, rely = 0.8, anchor = CENTER)


def questionscreen4():
    global q4
    # function to clear the screen (will be used by continuebutton)
    def clearscreen4():
        selection = "selected option " + str(q4.get())
        print(selection)
        if q4.get() == 1: #Nvidia
            d["mint"] += 1
            d["ubuntu"] += 2
            d["pop"] += 3
            d["elementary"] += 1
            d["debian"] += 1
            d["manjaro"] += 1
            d["fedora"] += 2
            d["garuda"] += 2
            d["arch"] += 2
            d["gentoo"] += 1
        elif q4.get() == 2: #AMD
            d["mint"] += 1
            d["ubuntu"] += 1
            d["pop"] += 2
            d["elementary"] += 1
            d["debian"] += 1
            d["manjaro"] += 3
            d["fedora"] += 2
            d["garuda"] += 1
            d["arch"] += 2
            d["gentoo"] += 1
        elif q4.get() == 3: #idk
            d["mint"] += 1
            d["ubuntu"] += 1
            d["pop"] += 1
            d["elementary"] += 1
            d["debian"] += 1
            d["manjaro"] += 1
            d["fedora"] += 1
            d["garuda"] += 1
            d["arch"] += 1
            d["gentoo"] += 1
        questiontitle4.place_forget()
        continuebutton4.place_forget()
        rb1b.place_forget()
        rb2b.place_forget()
        rb3b.place_forget()
    # self explanatory
    print("question screen 4 display successful")
    # adds question screen
    questiontitle4 = Label(main, font=Font_title, bg='#f5f5f5', fg='#4a4a4a', text='What GPU does\nyour system\nhave?')
    questiontitle4.place(relx = 0.265, rely = 0.25, anchor = CENTER)
    # selection buttons
    q4 = IntVar()
    rb1b=customtkinter.CTkRadioButton(main, text='Nvidia', font = Font_checkbox, text_color='#4a4a4a', bg_color='#f5f5f5', radiobutton_width=50, radiobutton_height=50, corner_radius=10, border_width_checked=10, variable=q4, value=1)
    rb2b=customtkinter.CTkRadioButton(main, text='AMD', font = Font_checkbox, text_color='#4a4a4a', bg_color='#f5f5f5', radiobutton_width=50, radiobutton_height=50, corner_radius=10, border_width_checked=10, variable=q4, value=2)
    rb3b=customtkinter.CTkRadioButton(main, text='I do not know\n/Integrated', font = Font_checkbox, text_color='#4a4a4a', bg_color='#f5f5f5', radiobutton_width=50, radiobutton_height=50, corner_radius=10, border_width_checked=10, variable=q4, value=3)
    rb1b.place(relx = 0.15, rely = 0.4, anchor = W)
    rb2b.place(relx = 0.15, rely = 0.5, anchor = W)
    rb3b.place(relx = 0.15, rely = 0.6, anchor = W)
    continuebutton4 = Button(main, text='Continue', bg='#f5f5f5', fg='#4a4a4a', font=Font_button, width=10, bd=15, relief=RAISED, command=lambda: [clearscreen4(), questionscreen5()])
    continuebutton4.place(relx = 0.265, rely = 0.8, anchor = CENTER)


def questionscreen5(): # complete!
    global q5
    def clearscreen5():
        selection = str(q5.get())
        print(selection)
        if q5.get() == 1:
            d["mint"] += 3
            d["ubuntu"] += 2
            d["pop"] += 1
            d["elementary"] += 1
            d["debian"] += 1
            d["manjaro"] += 1
            d["fedora"] += 1
            d["garuda"] += 1
            d["arch"] += 1
            d["gentoo"] += 1
        elif q5.get() == 2:
            d["mint"] += 2
            d["ubuntu"] += 3
            d["pop"] += 2
            d["elementary"] += 1
            d["debian"] += 1
            d["manjaro"] += 1
            d["fedora"] += 1
            d["garuda"] += 1
            d["arch"] += 1
            d["gentoo"] += 1
        elif q5.get() == 3:
            d["mint"] += 1
            d["ubuntu"] += 2
            d["pop"] += 3
            d["elementary"] += 2
            d["debian"] += 1
            d["manjaro"] += 1
            d["fedora"] += 1
            d["garuda"] += 1
            d["arch"] += 1
            d["gentoo"] += 1
        elif q5.get() == 4:
            d["mint"] += 1
            d["ubuntu"] += 1
            d["pop"] += 2
            d["elementary"] += 3
            d["debian"] += 2
            d["manjaro"] += 1
            d["fedora"] += 1
            d["garuda"] += 1
            d["arch"] += 1
            d["gentoo"] += 1
        elif q5.get() == 5:
            d["mint"] += 1
            d["ubuntu"] += 1
            d["pop"] += 1
            d["elementary"] += 2
            d["debian"] += 3
            d["manjaro"] += 2
            d["fedora"] += 1
            d["garuda"] += 1
            d["arch"] += 1
            d["gentoo"] += 1
        elif q5.get() == 6:
            d["mint"] += 1
            d["ubuntu"] += 1
            d["pop"] += 1
            d["elementary"] += 1
            d["debian"] += 2
            d["manjaro"] += 3
            d["fedora"] += 2
            d["garuda"] += 1
            d["arch"] += 1
            d["gentoo"] += 1
        elif q5.get() == 7:
            d["mint"] += 1
            d["ubuntu"] += 1
            d["pop"] += 1
            d["elementary"] += 1
            d["debian"] += 1
            d["manjaro"] += 2
            d["fedora"] += 3
            d["garuda"] += 2
            d["arch"] += 1
            d["gentoo"] += 1
        elif q5.get() == 8:
            d["mint"] += 1
            d["ubuntu"] += 1
            d["pop"] += 1
            d["elementary"] += 1
            d["debian"] += 1
            d["manjaro"] += 1
            d["fedora"] += 2
            d["garuda"] += 3
            d["arch"] += 2
            d["gentoo"] += 1
        elif q5.get() == 9:
            d["mint"] += 1
            d["ubuntu"] += 1
            d["pop"] += 1
            d["elementary"] += 1
            d["debian"] += 1
            d["manjaro"] += 1
            d["fedora"] += 1
            d["garuda"] += 2
            d["arch"] += 3
            d["gentoo"] += 2
        elif q5.get() == 10:
            d["mint"] += 1
            d["ubuntu"] += 1
            d["pop"] += 1
            d["elementary"] += 1
            d["debian"] += 1
            d["manjaro"] += 1
            d["fedora"] += 1
            d["garuda"] += 1
            d["arch"] += 2
            d["gentoo"] += 3
        questiontitle5.place_forget()
        questionsubtitle5.place_forget()
        continuebutton5.place_forget()
        scale.place_forget()
        snl.place_forget()
    print("question screen 5 display successful")
    # adds question screen
    questiontitle5 = customtkinter.CTkLabel(main, font=Font_title_alt, fg_color='transparent', text_color="#4a4a4a", text='How\ncustomisable\nwould you like\nyour OS to be?')
    questiontitle5.place(relx = 0.265, rely = 0.25, anchor = CENTER)
    questionsubtitle5 = Label(main, font=Font_button, bg='#f5f5f5', fg='#4a4a4a', text='1 - I just want\nit to work\n10 - I want full\ncustomisability ')
    questionsubtitle5.place(relx = 0.265, rely = 0.5, anchor = CENTER)
    # selection scale
    q5 = IntVar()
    snl = Label(main, font=Font_button, bg='#f5f5f5', fg='#4a4a4a', text='h', textvariable=q5) # snl stands for slidernumberlabel
    snl.place(relx = 0.265, rely = 0.7, anchor = CENTER)
    def slidernumber():
        thething = 1
        if q5.get() == 1:
            snl.config(text='1')
        elif q5.get() == 2:
            snl.config(text='2')
        elif q5.get() == 3:
            snl.config(text='3')
        elif q5.get() == 4:
            snl.config(text='4')
        elif q5.get() == 5:
            snl.config(text='5')
        elif q5.get() == 6:
            snl.config(text='6')
        elif q5.get() == 7:
            snl.config(text='7')
        elif q5.get() == 8:
            snl.config(text='8')
        elif q5.get() == 9:
            snl.config(text='9')
        elif q5.get() == 10:
            snl.config(text='10')
    scale = customtkinter.CTkSlider(main, variable=q5, width=300, height=50, from_=1, to=10, orientation="horizontal", number_of_steps=9, border_width=10, bg_color='#f5f5f5', button_color='#a1a1a1', button_hover_color='#dddddd')
    scale.place(relx = 0.265, rely = 0.65, anchor = CENTER)
    # continue button
    continuebutton5 = Button(main, text='Continue', bg='#f5f5f5', fg='#4a4a4a', font=Font_button, width=10, bd=15, relief=RAISED, command=lambda: [clearscreen5(), resultscreen()])
    continuebutton5.place(relx = 0.265, rely = 0.8, anchor = CENTER)

    print(d)

def resultscreen():
    best_distro = max(d, key=d.get)
    best_distro_name = 'a' # a is placeholder until it gets filled in
    install_link = 'a'
    imgbg.place_forget()
    imgfgs.place_forget()

    imgframe = customtkinter.CTkFrame(master=main, width=1000, height=563, fg_color='#4a4a4a', border_width=50, corner_radius=10)
    imgframe.place(relx = 0.93, rely = 0.5, anchor = E)

    # Create a reference for the image to avoid garbage collection
    global img_reference
    img_reference = None

    if best_distro == 'mint':
        best_distro_name = 'Linux Mint'
        img_reference = ImageTk.PhotoImage(Image.open('./images/distros/mint.png'))
        distroimage = Label(imgframe, image=img_reference, bd=0)
        distroimage.pack()
    elif best_distro == 'ubuntu':
        best_distro_name = 'Ubuntu'
        img_reference = ImageTk.PhotoImage(Image.open('./images/distros/ubuntu.png'))
        distroimage = Label(imgframe, image=img_reference, bd=0)
        distroimage.pack()
    elif best_distro == 'pop':
        best_distro_name = 'Pop!_OS'
        img_reference = ImageTk.PhotoImage(Image.open('./images/distros/popos.png'))
        distroimage = Label(imgframe, image=img_reference, bd=0)
        distroimage.pack()
    elif best_distro == 'elementary':
        best_distro_name = 'Elementary OS'
        img_reference = ImageTk.PhotoImage(Image.open('./images/distros/elementary.png'))
        distroimage = Label(imgframe, image=img_reference, bd=0)
        distroimage.pack()
    elif best_distro == 'debian':
        best_distro_name = 'Debian'
        img_reference = ImageTk.PhotoImage(Image.open('./images/distros/debian.png'))
        distroimage = Label(imgframe, image=img_reference, bd=0)
        distroimage.pack()
    elif best_distro == 'manjaro':
        best_distro_name = 'Manjaro'
        img_reference = ImageTk.PhotoImage(Image.open('./images/distros/manjaro.png'))
        distroimage = Label(imgframe, image=img_reference, bd=0)
        distroimage.pack()
    elif best_distro == 'fedora':
        best_distro_name = 'Fedora'
        img_reference = ImageTk.PhotoImage(Image.open('./images/distros/fedora.png'))
        distroimage = Label(imgframe, image=img_reference, bd=0)
        distroimage.pack()
    elif best_distro == 'garuda':
        best_distro_name = 'Garuda Linux'
        img_reference = ImageTk.PhotoImage(Image.open('./images/distros/garuda.png'))
        distroimage = Label(imgframe, image=img_reference, bd=0)
        distroimage.pack()
    elif best_distro == 'arch':
        best_distro_name = 'Arch Linux'
        img_reference = ImageTk.PhotoImage(Image.open('./images/distros/arch.png'))
        distroimage = Label(imgframe, image=img_reference, bd=0)
        distroimage.pack()
    elif best_distro == 'gentoo':
        best_distro_name = 'Gentoo'
        img_reference = ImageTk.PhotoImage(Image.open('./images/distros/gentoo.png'))
        distroimage = Label(imgframe, image=img_reference, bd=0)
        distroimage.pack()

        distroimage.pack()

    global resultscreen, resulttitle, result

    def download():
        # Change distro names to the proper names
        nonlocal install_link
        if best_distro == 'mint':
            install_link = 'https://mirrors.cicku.me/linuxmint/iso/stable/22/linuxmint-22-cinnamon-64bit.iso'
        elif best_distro == 'ubuntu':
            install_link = 'https://releases.ubuntu.com/24.04/ubuntu-24.04-desktop-amd64.iso'
        elif best_distro == 'pop':
            if q4.get() == 1: # Nvidia
                install_link = 'https://iso.pop-os.org/22.04/amd64/nvidia/42/pop-os_22.04_amd64_nvidia_42.iso'
            elif q4.get() == 2: # AMD
                install_link = 'https://iso.pop-os.org/22.04/amd64/intel/42/pop-os_22.04_amd64_intel_42.iso'
            elif q4.get() == 3: # idk/integrated
                install_link = 'https://iso.pop-os.org/22.04/amd64/intel/42/pop-os_22.04_amd64_intel_42.iso'
        elif best_distro == 'elementary':
            install_link = 'https://fra1.dl.elementary.io/download/MTcyMzAxOTYxOA==/elementaryos-7.1-stable.20230926rc.iso'
        elif best_distro == 'debian':
            install_link = 'https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.6.0-amd64-netinst.iso'
        elif best_distro == 'manjaro':
            install_link = 'https://manjaro.org/products/download/x86'
        elif best_distro == 'fedora':
            install_link = 'https://download.fedoraproject.org/pub/fedora/linux/releases/40/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-40-1.14.iso'
        elif best_distro == 'garuda':
            install_link = 'https://iso.builds.garudalinux.org/iso/latest/garuda/dr460nized/latest.iso?r2=1'
        elif best_distro == 'arch':
            install_link = 'https://geo.mirror.pkgbuild.com/iso/2024.08.01/archlinux-2024.08.01-x86_64.iso'
        elif best_distro == 'gentoo':
            install_link = 'https://distfiles.gentoo.org/releases/amd64/autobuilds/20240804T163558Z/livegui-amd64-20240804T163558Z.iso'
        webbrowser.open(install_link)
        # shows message upon pressing the button
        message = Label(main, font = Font_main, text='Check your web browser!', bg="#181818",fg="#f5f5f5")
        message.place(relx=0.2, rely=0.54, anchor=CENTER)

    def goback():
        resultscreenl.place_forget()
        downloadbutton.place_forget()
        backbutton.place_forget()
        imgframe.place_forget()
        message.place_forget()
        imgbgs.place(x = -0.5, y = -0.5)
        startbutton.place(relx = 0.51, rely = 0.4, anchor = CENTER)
        distroimage.pack_forget()
        main.configure(bg='#f5f5f5')

    # Show result screen
    main.configure(bg='#181818')
    resultscreenl = Label(main, font = Font_title, bg="#181818", fg="#f5f5f5", text=f'The best distro\nfor you should\nbe: {best_distro_name}!')
    resultscreenl.place(relx=0.2, rely=0.4, anchor=CENTER)
    downloadbutton = Button(main, text='Download', bg='#f5f5f5', fg='#4a4a4a', font=Font_button, width=10, bd=15, relief=RAISED, command=download)
    downloadbutton.place(relx = 0.2, rely = 0.6, anchor = CENTER)

    backbutton = customtkinter.CTkButton(main, text='Go back', bg_color='#181818', fg_color='#181818', width=5, font=Font_main, command=goback, corner_radius=0)
    backbutton.place(relx = 0, rely = 0, anchor = NW)

# create the window
main = tkinter.Tk()
main.configure(bg='#f5f5f5')

titleframe = customtkinter.CTkFrame(master=main, width=1920, height=1080, fg_color='#181818')
titleframe.place(x = 0, y = 0, anchor = NW)

# window icon
icon = ImageTk.PhotoImage(Image.open('./images/icon.png'))
main.iconphoto(True, icon)

# make the window size normal
main.geometry('1920x1080')

main.overrideredirect(False)
main.resizable(False, False)

# set the fonts
Font_title = ("JetBrains Mono", 37, "bold")
Font_title_alt = ("JetBrains Mono", 47, "bold")
Font_big_title = ("JetBrains Mono", 60, "bold")
Font_main = ("JetBrains Mono", 12)
Font_button = ("JetBrains Mono", 30)
Font_checkbox = ("JetBrains Mono", 50)

# title screen
global imgbgsref
imgbgsref = None
imgbgsref = ImageTk.PhotoImage(Image.open('./images/backgrounds/startbg.png'))
imgbgs = Label(titleframe, image=imgbgsref)
imgbgs.place(x = -0.5, y = -0.5)

# start button (i dont think these comments are even necessary)
startbutton = Button(titleframe, text='Start', bg='#f5f5f5', fg='#4a4a4a', font=Font_button, width=10, bd=15, relief=RAISED, command=questionscreen1)
startbutton.place(relx = 0.51, rely = 0.4, anchor = CENTER)

main.title('Penguinstall')
# makes the whole thing work (yippee)
main.mainloop()
