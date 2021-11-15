"""
Purpose of this application is to create simple QR codes. When searching for online solution for free
simple QR code generators, usually those websites require personal information, surveys or they are filled with ads.

Created by: Stjepan Maric
contact: stjepan.maric1994@gmail.com

How to use:
    Select one of 10 versions of QR code, basically, select how your QR code will look like.
    Select size of your QR code in range from 1 to 10 , 1 being the smallest and 10 being the biggest.
    Select border around your QR code in range from 1 to 10, again 1 being the smallest and 10 being the biggest.
    Select background color of your QR code.
    Select foreground color of your QR code.
    Input text you want to display once QR code is scanned.
    Click on  'Create and save QR code' button and select location where you want to store QR code.
When selecting background and foreground color of your QR code, make sure you pick good contrast between dark and light
color. Sometimes devices are not able to recognise QR code if contrast is not good.

I hope you will find this program useful. :)
"""
import qrcode
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.colorchooser import askcolor
import os


def background_color_picker() -> None:
    """
    Used to change background color of background color button picker

    :return: None
    """
    my_color = askcolor()[1]  # open color picker window and assign value to my_color variable
    button_background_color.configure(bg=my_color)  # configure background color of button to selected value


def foreground_color_picker() -> None:
    """
    Used to change background color of foreground color button picker

    :return: None
    """
    my_color = askcolor()[1]  # open color picker window and assign value to my_color variable
    button_foreground_color.configure(bg=my_color)  # configure background color of button to selected value


def create_and_save_file(user_version: int, user_size: int, user_border: int, user_text_data: str, user_bg_color: str,
                         user_fill_color: str) -> None:
    """
    Used to create QR code on given parameters and save it on specific user selected location.

    :param user_version: user inputted version of QR code
    :param user_size: user inputted size of QR code
    :param user_border: user inputted size of border around QR code
    :param user_text_data: user inputted text that will be displayed in QR code (when scanned)
    :param user_bg_color: user inputted background color of QR code
    :param user_fill_color: user inputted foreground color of QR code
    :return: None
    """
    version = user_version.get()  # get int value from Spinbox widget
    size = user_size.get()  # get int value from Spinbox widget
    border = user_border.get()  # get int value from Spinbox widget
    text_data = user_text_data.get("1.0", "end-1c")  # get str value from text box from first character to last
    bg_color = user_bg_color.cget('bg')  # get the resource value for a KEY given as string
    fg_color = user_fill_color.cget('bg')  # get the resource value for a KEY given as string

    print(f"version: {version}, size: {size}, border: {border},text_data: {text_data}, "
          f" bg_color: {bg_color}, fg_color: {fg_color}")
    qr = qrcode.QRCode(version=version, box_size=size, border=border)  # pass values to QR code
    qr.add_data(text_data)  # pass data to qr code (text_data)
    qr.make(fit=True)  # fit=True is find the best fit for the data to avoid data overflow errors
    img = qr.make_image(back_color=bg_color, fill_color=fg_color)  # Make an image from the QR Code data

    files = [('PNG', '*.png'), ('JPEG', '*.jpg')]  # supported file types and file extensions
    file_path = filedialog.asksaveasfilename(filetypes=files, defaultextension=files)  # Ask for a filename to save as
    try:
        filename = os.path.basename(file_path)  # get the base name in specified path
        img.save(file_path)  # save created image to specified file_path

    except(AttributeError, FileNotFoundError):
        print("Save operation cancelled")
        return


def show_help_info():
    """
    Used to show info in message box to the user
    :return: None
    """
    # pop up message box
    messagebox.showinfo(
        title="Help",
        message="""How to use: 
        1. Select QR code version in values from 1 to 10
        2. Select QR code size in values from 1 to 10
        3. Select QR code border size in values from 1 to 10
        4. Select QR code background color from color picker
        5. Select QR code foreground color from color picker
        6. Click on 'Create and save QR code' 
        7. Select specific location where to save QR code image.""")


# Create window with title and geometry
win = Tk()
win.title('QR Code Generator')
win.geometry("500x400+10+10")

# create label widgets
select_version_label = Label(win, text='Version')
select_size_label = Label(win, text='Size')
select_border_size_label = Label(win, text='Border size')

# create Spinbox widgets
select_version_value = Spinbox(win, from_=0, to=10)
select_size_value = Spinbox(win, from_=0, to=10)
select_border_size_value = Spinbox(win, from_=0, to=10)

# place label and spinbox widgets on specific locations inside window
select_version_label.place(x=100, y=50)
select_version_value.place(x=200, y=50)

select_size_label.place(x=100, y=100)
select_size_value.place(x=200, y=100)

select_border_size_label.place(x=100, y=150)
select_border_size_value.place(x=200, y=150)

# create buttons and assign commands to them
button_background_color = Button(win, text='Pick background color', command=lambda: background_color_picker())
button_foreground_color = Button(win, text='Pick foreground color', command=lambda: foreground_color_picker())

# place buttons on specific location inside window
button_background_color.place(x=75, y=200)
button_foreground_color.place(x=275, y=200)

# create label and text box and place them on specific locations inside window
input_text_label = Label(win, text='Qr code text')
input_text_label.place(x=100, y=250)
textBox = Text(win, height=3, width=20)
textBox.place(x=200, y=250)

# create button, place button on specific location inside window and assign command to it
button_create = Button(win, text='Create and save QR code', fg='Green', height=2,
                       command=lambda: create_and_save_file(select_version_value, select_size_value,
                                                            select_border_size_value, textBox, button_background_color,
                                                            button_foreground_color))
button_create.place(x=175, y=325)

# create button, place button on specific location inside window and assign command to it
button_help = Button(win, text='Help',
                     command=lambda: show_help_info())
button_help.place(x=0, y=0)

# mainloop simply, is method in the main window that executes what we wish to execute in an application
win.mainloop()
