from tkinter import *
from tkinter import messagebox
import pyperclip
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    error = ""
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        with open("passwords.json", "r") as data_file:
            # reading the old data
            data = json.load(data_file)
            # updating the old data with the new data
            data.update(new_data)

        with open("passwords.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
            web_entry.delete(0, END)
            pass_entry.delete(0, END)
        web_entry.focus()



def pass_finder():
    pass


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.config(padx=20)
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.config(padx=20)
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.config(padx=20)
pass_label.grid(column=0, row=3)

add_button = Button(width=38, text="Add", command=save)
add_button.config(padx=20)
add_button.grid(column=1, row=4, columnspan=2)

pass_button = Button(text="Generate Password", command=pass_gen)
pass_button.grid(column=2, row=3)

web_entry = Entry(width=32)
web_entry.grid(column=1, row=1)
web_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "dvision_st@yahoo.com")

pass_entry = Entry(width=32)
pass_entry.grid(column=1, row=3)

search_button = Button(width=9, text="Search", command=pass_finder)
search_button.grid(column=2, row=1)
search_button.config(padx=20)

window.mainloop()
