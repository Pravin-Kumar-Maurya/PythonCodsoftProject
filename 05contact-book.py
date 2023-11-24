from tkinter import *

contacts = {}  # Dictionary to store contacts

# Function to add a contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    if name.strip() != "":
        if name not in contacts:
            contacts[name] = {'Phone': phone, 'Email': email}
            update_display("Contact added: " + name)
        else:
            update_display("Contact already exists!")
    else:
        update_display("Name cannot be empty!")

# Function to delete a contact
def delete_contact():
    name = entry_name.get()
    if name in contacts:
        del contacts[name]
        update_display("Contact deleted: " + name)
    else:
        update_display("Contact does not exist!")

# Function to search for contacts
def search_contact():
    keyword = entry_search.get().lower()
    search_result = {name: details for name, details in contacts.items() if keyword in name.lower() or keyword in details['Phone']}
    if search_result:
        display_search_result(search_result)
    else:
        update_display("No matching contacts found!")

# Function to update the display information
def update_display(message):
    label_display.config(text=message)
    update_contact_list()

# Function to update the contact list in the listbox
def update_contact_list():
    listbox.delete(0, END)
    for name in contacts:
        listbox.insert(END, name)

# Function to update the search result in the listbox
def display_search_result(search_result):
    listbox.delete(0, END)
    for name in search_result:
        listbox.insert(END, name)

# Create the main window
root = Tk()
root.title("Contact Book")
root.minsize("390","480")  # Set window size
root.maxsize("390","480")

#icon
Image_icon = PhotoImage(file="images/contact.png")
root.iconphoto(False,Image_icon)

# Create a listbox to display tasks
t_title=Label(root,text="Contact Book",font=("arial",20,"bold"),bg="#32405b",fg="white",width=22)
t_title.pack(ipady=5,ipadx=2)

# Label to display information
label_display = Label(root, text="", fg="red", font=16)
label_display.pack()

# Create and place labels and entry fields for contact details
name_frame = Frame(root)
label_name = Label(name_frame, text="Name:",font=16, width=6)
label_name.pack(side=LEFT)
entry_name = Entry(name_frame, width=35, font=16, bd=3)
entry_name.pack(side=LEFT, ipady=5)
name_frame.pack(ipady=2,pady=5)

phone_frame = Frame(root)
label_phone = Label(phone_frame, text="Phone:", font=16, width=6)
label_phone.pack(side=LEFT)
entry_phone = Entry(phone_frame, width=35, font=16, bd=3)
entry_phone.pack(side=LEFT, ipady=5)
phone_frame.pack(ipady=2)

email_frame = Frame(root)
label_email = Label(email_frame, text="Email:", font=16, width=6)
label_email.pack(side=LEFT)
entry_email = Entry(email_frame, width=35, font=16, bd=3)
entry_email.pack(side=LEFT, ipady=5)
email_frame.pack(ipady=2)

# Create a frame for buttons
button_frame = Frame(root)
button_frame.pack(pady=2)

# Button to add a contact
add_button = Button(button_frame, text="Add Contact", command=add_contact, font=16, width=19, bd=3)
add_button.pack(side=LEFT,padx=1,ipadx=2)

# Button to delete a contact
delete_button = Button(button_frame, text="Delete Contact", command=delete_contact, font=16, width=20, bd=3)
delete_button.pack(side=LEFT,ipadx=2)

# Create a frame for search field and button
search_frame = Frame(root)
search_frame.pack(pady=2)

# Entry field for search
entry_search = Entry(search_frame, width=34, font=16, bd=3)
entry_search.pack(side=LEFT,ipady=4,ipadx=2)

# Button to search contacts
search_button = Button(search_frame, text="Search", command=search_contact , font=16, height=1, width=6,bg="#32405b",fg="white", bd=3)
search_button.pack(side=LEFT)

# Create a listbox to display contacts
listbox = Listbox(root, width=42, font=16, height=10,bd=3)
listbox.pack()

root.mainloop()
