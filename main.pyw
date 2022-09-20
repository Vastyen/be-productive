
import tkinter
import customtkinter
import os
import tkinter.font
from tkinter import messagebox

started = False

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("System")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.resizable(False, False)

photo = tkinter.PhotoImage(file="icon.png")
app.iconphoto(False, photo)


app.iconbitmap("favicon.ico")

width = 600  # Width
height = 600  # Height

screen_width = app.winfo_screenwidth()  # Width of the screen
screen_height = app.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

app.geometry('%dx%d+%d+%d' % (width, height, x, y))

app.title('Be Productive')


def button_function():
    global started
    started = True
    print("Started")
    messagebox.showinfo(message="Be Productive has Started", title="Be Productive")
    app.wm_state('iconic')
    os.system("start closer.exe")

def button_function2():
    global started
    if (started):
        os.system("taskkill /F /IM closer.exe")
        started = False
        print("Down")
    else:
        messagebox.showinfo(message="You need to start to stop it.", title="Be Productive")


text_var2 = tkinter.StringVar(value="It's time to be free.")

label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var2,
                               width=120,
                               height=25,
                               corner_radius=8, text_font=("Latin Modern Mono Light", 30))
label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)


text_var3 = tkinter.StringVar(value="We know it's hard to say no")

label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var3,
                               width=120,
                               height=25,
                               corner_radius=8, text_font=("Latin Modern Mono Light", 20))
label.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)



# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(
    master=app, text="Start", command=button_function, text_font=("Latin Modern Mono Light", 35), fg_color="green", hover_color=("gray"))
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER,                                 width=170,
             height=80)

button2 = customtkinter.CTkButton(
    master=app, text="Stop", command=button_function2, text_font=("Latin Modern Mono Light", 35), fg_color="red", hover_color=("gray"))
button2.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER,                                 width=160,
             height=70)

app.mainloop()

