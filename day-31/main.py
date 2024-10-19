from unittest.mock import right

from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50)

# Card images
image_front = PhotoImage(file="images\card_front.png")
image_back = PhotoImage(file="images\card_back.png")

# Right/Wrong images
image_right = PhotoImage(file="images/right.png")
image_wrong = PhotoImage(file="images\wrong.png")


canvas = Canvas(width= 350, height = 350,bg = BACKGROUND_COLOR)
canvas.create_image(200,200, image = image_front)
canvas.grid(column=0,row=0,columnspan=1)

# Label

title_label = Label(text = "Title")

word_label = Label(text = "Word")

# Buttons
right_button = Button(image = image_right,width = 100, height = 100, highlightthickness=0, bg = BACKGROUND_COLOR)
right_button.grid(column=0,row=1)

wrong_button = Button(image = image_wrong,width = 100, height = 100, highlightthickness=0, bg = BACKGROUND_COLOR)
wrong_button.grid(column=1,row=1)



window.mainloop()