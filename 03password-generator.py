import random
import string
from tkinter import *

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Create gui
def generate_password_gui():
    def generate():
                try:
                    desiered_length = int(entry.get())
                    if desiered_length <= 0 and desiered_length > 15:
                        result_label.config(text="Please enter a valid length (beween 0 to 16).")
                    else:
                        password = generate_password(desiered_length)
                        result_label.config(text="Generated Passwod : " + password)
                except ValueError:
                     result_label.config(text = "Enter a valid number for the length.")
    root = Tk()
    root.title("Password Generator")
    root.minsize("380","230")
    root.maxsize("380","230")

    #icon
    Image_icon = PhotoImage(file="images/pass.png")
    root.iconphoto(False,Image_icon)

    # Create a listbox to display tasks
    t_title=Label(root,text="Password Generator",font=("arial",20,"bold"),bg="#32405b",fg="white",width=21)
    t_title.pack(ipadx=5,ipady=5,pady=2)

    label=Label(root, text = "Enter the desierd length of Password :",font="arial 14",background="white",width="33")
    label.pack(pady=2,ipady=5,ipadx=2)

    entry = Entry(root,font="arial 16",border="2px",width="30")
    entry.pack(ipadx=3,ipady=5,pady=5)

    generate_button = Button(root,text = "Generate Password",font="arial 16",command = generate,background="white",width="30")
    generate_button.pack(ipadx=2)

    result_label = Label(root, text = '',background="white",font="arial 13",width="40",border="5px")
    result_label.pack(ipady=2,pady=5, padx=5)

    root.mainloop()

# Calling gui method
generate_password_gui()


                    