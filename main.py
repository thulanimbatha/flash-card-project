from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# --------------------UI--------------------------------------
# setup display window
window = Tk()
window.title("Flash Card Project")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# create canvas + add photo to canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=flash_card)
# TEXT 
canvas.create_text(400, 160, text="Title", fill="black", font=("Times New Roman", 30, "italic"))
canvas.create_text(400, 263, text="Word", fill="black", font=("Times New Roman", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
wrong_img = PhotoImage(file="./images/wrong.png")   # Make button a clickable photo
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")   # Make button a clickable photo
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=1)





window.mainloop()