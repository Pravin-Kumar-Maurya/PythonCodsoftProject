from tkinter import *
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)

    label_user_choice.config(text=f"Your choice: {user_choice}")
    label_computer_choice.config(text=f"Computer's choice: {computer_choice}")
    label_result.config(text=result)

def rock_button_click():
    play_game("rock")

def paper_button_click():
    play_game("paper")

def scissors_button_click():
    play_game("scissors")

# Create the main window
root = Tk()
root.minsize("410","270")
root.maxsize("410","270")
root.title("Rock Paper Scissors Game")
#icon
Image_icon = PhotoImage(file="images/rock.png")
root.iconphoto(False,Image_icon)

# Create a listbox to display tasks
t_title=Label(root,text="Rock-Paper-Scissors Game",font=("arial",20,"bold"),bg="#32405b",fg="white",width=23)
t_title.pack(ipadx=2,ipady=5,pady=2)

# Create GUI elements
label_instructions = Label(root, text="Choose rock, paper, or scissors:",font=16, background="white", width=44, height=2)
label_instructions.pack()

f = Frame(root)

button_rock = Button(f, text="Rock", command=rock_button_click, font=16 , width=13, background="white")
button_rock.pack(ipadx=2,ipady=5,side=LEFT)

button_paper = Button(f, text="Paper", command=paper_button_click, font=16, width=14, background="white")
button_paper.pack(ipadx=3,ipady=5,side=LEFT)

button_scissors = Button(f, text="Scissors", command=scissors_button_click,font=16, width=13, background="white")
button_scissors.pack(ipadx=2,ipady=5,side=LEFT)

f.pack(pady=2)

label_user_choice = Label(root, text="", background="white", font=16, width=44, height=2)
label_user_choice.pack()

label_computer_choice = Label(root, text="", background="white", font=16, width=44, height=2)
label_computer_choice.pack()

label_result = Label(root, text="", background="white", font=16, width=44, height=2)
label_result.pack()

root.mainloop()
