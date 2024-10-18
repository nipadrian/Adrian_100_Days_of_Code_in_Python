from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    eu = eu_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message = "Please make sure you haven't left any fields empty")
    else:


    #messagebox.showinfo(title="title", message="message")
        is_okay = messagebox.askokcancel(title=website,message = f"These are the details entered: \n Email: {eu} "
                                                    f"\n Password: {password} \n Is it okay to save?")

    if is_okay:
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

generate_pw_button = Button(text = "Generate Password", command = generate_password, highlightthickness=0)
generate_pw_button.grid(column=2,row=3)

add_button = Button(text = "Add",width = 36, command = save, highlightthickness=0)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()