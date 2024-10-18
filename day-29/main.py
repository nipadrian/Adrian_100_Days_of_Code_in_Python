from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    eu = eu_entry.get()
    password = password_entry.get()
    with open("data.txt","a") as data_file:
        data_file.write(f"{website} | {eu} | {password}\n")
        website_entry.delete(0,END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height = 200)
my_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = my_img)
canvas.grid(column = 1, row = 0)

# Label

website_label = Label(text = "Website:")
website_label.grid(column=0, row = 1)


eu_label = Label(text = "Email/Username:")
eu_label.grid(column=0, row = 2)


password_label = Label(text = "Password:")
password_label.grid(column=0, row = 3)


# Entry

website_entry = Entry(width=55)
website_entry.grid(column=1,row=1,columnspan = 2)
website_entry.focus()

eu_entry = Entry(width=55)
eu_entry.grid(column=1,row=2,columnspan = 2)
eu_entry.insert(0,"nipnipnip@gmail.com")

password_entry = Entry(width=37)
password_entry.grid(column=1,row=3)

# Buttons

def gen_pw():
    pass

generate_pw_button = Button(text = "Generate Password", command = gen_pw, highlightthickness=0)
generate_pw_button.grid(column=2,row=3)

add_button = Button(text = "Add",width = 36, command = save, highlightthickness=0)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()