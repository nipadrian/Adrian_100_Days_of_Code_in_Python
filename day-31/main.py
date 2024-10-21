from unittest.mock import right

from tkinter import *
import random
import pandas
import math

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
df_dict = {}

# ---------------------------- Import Data ------------------------------- #

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("data/french_words.csv")
    df_dict = original_data.to_dict(orient="records")
else:
    df_dict= df.to_dict(orient='records')





# ---------------------------- Change words ------------------------------- #

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(df_dict)
    canvas.itemconfig(card_title, text="French", font=("Ariel", 60, "italic"), fill = "black")
    canvas.itemconfig(card_text, text=current_card["French"], font=("Ariel", 60, "italic"),fill = "black")
    canvas.itemconfig(card_front, image=image_front)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    df_dict.remove(current_card)
    data = pandas.DataFrame(df_dict)
    data.to_csv("data/words_to_learn.csv", index = False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title, text="English", font=("Ariel", 60, "italic"),fill = "white")
    canvas.itemconfig(card_text, text=current_card["English"], font=("Ariel", 60, "italic"), fill = "white")
    canvas.itemconfig(card_front, image = image_back)

def words_to_learn():
    pass


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg= BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Card images
image_front = PhotoImage(file="images\card_front.png")
image_back = PhotoImage(file="images\card_back.png")

# Right/Wrong images
image_right = PhotoImage(file="images/right.png")
image_wrong = PhotoImage(file="images\wrong.png")


canvas = Canvas(width= 800, height = 526)
card_front = canvas.create_image(400,263, image = image_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
card_title = canvas.create_text(400,150,text="Title",font = ("Ariel",40,"italic"))
card_text = canvas.create_text(400,263,text="Word",font = ("Ariel",60,"italic"))


next_card()

# Label



# Buttons
right_button = Button(image = image_right, command= is_known,bg = BACKGROUND_COLOR,highlightthickness=0)
right_button.grid(column=1,row=1)

wrong_button = Button(image = image_wrong, command = next_card, bg = BACKGROUND_COLOR,highlightthickness=0)
wrong_button.grid(column=0,row=1)



window.mainloop()