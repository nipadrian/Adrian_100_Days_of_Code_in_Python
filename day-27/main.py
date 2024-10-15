from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height = 300)
window.config(padx = 100, pady = 200)

# Label

my_label = Label(text = "I am a label",font = ("Arial", 24, "bold"))
my_label.grid(column = 0, row = 0)

my_label["text"] = "New Text"
my_label.config(text = "New Text")
my_label.config(padx=50,pady=50)

# Button

def button_clicked():
    typed_input = input.get()
    my_label.config(text = typed_input)

button = Button(text = "Click Me", command = button_clicked)
button.grid(column = 1,row = 1)

button2 = Button(text = "new button", command = button_clicked)
button2.grid(column = 2, row = 0)

# Entry

input = Entry(width = 10)
input.grid(column = 3, row = 3)
print(input.get())


window.mainloop()