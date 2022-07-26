from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# -------------------create new flash card------------------

# read the csv file
data = pandas.read_csv("./data/spanish_words.csv")
# convert csv file to dictionary
total_words = data.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card
    global flip_timer

    # cancel current 3 sec window
    window.after_cancel(flip_timer)
    current_card = random.choice(total_words)
    # change/config title and word
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["spanish"], fill="black")
    # change card back to card_front
    canvas.itemconfig(card_background, image=flash_card_front)
    # invoke new 3 second window
    flip_timer = window.after(3000, func=flip_card)

# -------------------flip-the-card---------------------------
def flip_card():
    # change card to show English word
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["english"], fill="white")
    # change image
    canvas.itemconfig(card_background, image=flash_card_back)

# -------------------remove-known-words-from-total-words---------
def known_words():
    total_words.remove(current_card)
    # create new csv file containing remaining words
    words_left = pandas.DataFrame(total_words)
    words_left.to_csv("./data/words_to_learn.csv")
    # call next_card function
    next_card()

# --------------------UI--------------------------------------
# setup display window
window = Tk()
window.title("Flash Card Project")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# add 3 sec delay - card changes after 3 secs
flip_timer = window.after(3000, func=flip_card)

# create canvas + add photo to canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front = PhotoImage(file="./images/card_front.png")
flash_card_back = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=flash_card_front)
# TEXT 
card_title = canvas.create_text(400, 160, text="Title", fill="black", font=("Times New Roman", 30, "italic"))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=("Times New Roman", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
wrong_img = PhotoImage(file="./images/wrong.png")   # Make button a clickable photo
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")   # Make button a clickable photo
right_button = Button(image=right_img, highlightthickness=0, command=known_words)
right_button.grid(column=1, row=1)

# after all is created, call function to generate spanish word
next_card()



window.mainloop()