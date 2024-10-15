from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 500, height = 300)
window.config(padx = 100, pady = 200)

# Labels

miles_label = Label(text = "Miles",font = ("Arial", 24))
miles_label.grid(column = 2, row = 0)
miles_label.config(padx = 20, pady = 20)

equal_label = Label(text = "is equal to",font = ("Arial", 24))
equal_label.grid(column = 0, row = 1)
equal_label.config(padx = 20, pady = 20)

km_label = Label(text = "Km",font = ("Arial", 24))
km_label.grid(column = 2, row = 1)
km_label.config(padx = 20, pady = 20)

converted_num = Label(text = "0", font = ("Arial", 24))
converted_num.grid(column = 1, row = 1)
converted_num.config(padx = 20, pady = 20)

# Button

def button_clicked():
    miles_input = float(input.get())
    miles_input *= 1.60934
    converted_num.config(text = miles_input)

button = Button(text = "Calculate", command = button_clicked)
button.grid(column = 1,row = 2)
button.config(padx = 20, pady = 5)

# Entry

input = Entry(width = 20)
input.grid(column = 1, row = 0)

window.mainloop()