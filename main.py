from cgitb import text
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# -------------------create new flash cards------------------

# read the csv file
data = pandas.read_csv("./data/spanish_words.csv")
# convert csv file to dictionary
words = data.to_dict(orient="records")

def next_card():
    current_card = random.choice(words)
    # change/config title and word
    canvas.itemconfig(card_title, text="Spanish")
    canvas.itemconfig(card_word, text=current_card["spanish"])


# --------------------UI--------------------------------------
# setup display window
window = Tk()
window.title("Flash Card Project")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# create canvas + add photo to canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=flash_card_front)
# TEXT 
card_title = canvas.create_text(400, 160, text="Title", fill="black", font=("Times New Roman", 30, "italic"))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=("Times New Roman", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
wrong_img = PhotoImage(file="./images/wrong.png")   # Make button a clickable photo
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")   # Make button a clickable photo
right_button = Button(image=right_img, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

# after all is created, call function to generate spanish word
next_card()



window.mainloop()