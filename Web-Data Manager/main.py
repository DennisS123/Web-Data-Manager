from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for letter in range(nr_letters)]
    password_list += [random.choice(numbers) for number in range(nr_numbers)]
    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
                "email": email,
                "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered: \n Email: {email}"
                                                              f"\n Password: {password} \n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
def find_password():
    website = website_input.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError or  KeyError:
        messagebox.showwarning(title="Error", message="No Data File found.")
    else:
        try:
            website_data = data[website]
        except KeyError:
            messagebox.showwarning(title="Error", message="No details for the website exists.")
        else:
            password = website_data["password"]
            email = website_data["email"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")





# ---------------------------- UI SETUP ------------------------------- #


screen = Tk()
screen.config(padx=50, pady=50)
screen.title("Password Manager")
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
website_text = Label(text='Website:')
website_text.grid(row=1, column=0)
username_text = Label(text="Email/Username:")
username_text.grid(row=2, column=0)
password_text = Label(text="Password:")
password_text.grid(row=3, column=0)
website_input = Entry(width=35)
website_input.grid(row=1, column=1)
website_input.focus()
username_input = Entry(width=35,)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "ddda4158@gmail.com")
password_input = Entry(width=35)
password_input.grid(row=3, column=1, columnspan=2)
generate = Button(text="Generate Password", width=14, command=generate_password)
generate.grid(row=3, column=3, columnspan=2)
add = Button(width=29, text="Add", command=save_password)
add.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", width=14, command=find_password)
search.grid(column=2, row=1, columnspan=2)
screen.mainloop()
