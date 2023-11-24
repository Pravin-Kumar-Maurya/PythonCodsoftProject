from tkinter import *
def add_task():
    task = entry.get()
    if task:
        listbox.insert(END,task)
        entry.delete(0,END)
def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

def update_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        updete_task = entry.get()
        if updete_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index,updete_task)
            entry.delete(0,END)

# Create the main window
root = Tk()
root.title("To-Do List")
root.minsize("420","410")
root.maxsize("420","410")

#icon
Image_icon = PhotoImage(file="images/todo.png")
root.iconphoto(False,Image_icon)

# Create a listbox to display tasks
t_title=Label(root,text="To DO LIST",font=("arial",25,"bold"),bg="#32405b",fg="white",width=20)
t_title.pack(ipadx=4,ipady=5)

listbox = Listbox(root,width=34,height=10,font=("arial",16),border=3)
listbox.pack(pady = 3)

# Create an entry for adding, updating and deleting tasks
entry_text = Frame(root)
entry_title=Label(entry_text,text="Task : ",font=("arial",16))
entry_title.pack(side=LEFT)

entry = Entry(entry_text,width=28,font=("arial",16),border=3)
entry.pack(side=LEFT,ipadx=2,ipady=5)

entry_text.pack()

# Create an entry for adding, updating and deleting button
button_frame = Frame(root)

add_button = Button(button_frame,text="Add Task",command=add_task,width=9,font=("arial",16),border=3)
update_button = Button(button_frame,text="Update Task",command=update_task,width=10,font=("arial",16),border=3)
delete_button = Button(button_frame,text="Delete Task",command=delete_task,width=12,font=("arial",16),border=3)

add_button.pack(padx=3,side='left')
update_button.pack(side='left')
delete_button.pack(padx=3,side='left')
button_frame.pack(pady=3)

# Run the main loop
root.mainloop()