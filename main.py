from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_letter=[choice(letters) for _ in range(randint(3, 6))]
    password_symbol=[choice(symbols) for _ in range(randint(2, 4))]
    password_number=[choice(numbers) for _ in range(randint(2, 4))]
    password_list+=password_letter+password_number+password_symbol

    shuffle(password_list)

    password="".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name=website_entry.get()
    email_username=email_username_entry.get()
    password=password_entry.get()


    if len(website_name)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please dont leave any field empty")
    else:
        is_okay = messagebox.askokcancel(title=website_name,message=f"These are the details entered: \n Email: {email_username} \n Password: {password} \n Is it okay to save?")

        if is_okay:
                with open("data.txt","a") as f:
                    f.write(f"{website_name} | {email_username} | {password} \n")
                    website_entry.delete(0,END)
                    email_username_entry.delete(0,END)
                    password_entry.delete(0,END)
                    email_username_entry.insert(0,"isha@gmail.com")
                    website_entry.focus()



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=400,height=400)
logo=PhotoImage(file=r"C:\Users\ishas\Downloads\password-manager-start\logo.png")
canvas.create_image(200,200,image=logo)
canvas.grid(row=0,column=1)
website_label=Label(text="Website:")
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
website_label.grid(row=1,column=0)
email_username_label=Label(text="Email/Username:")
email_username_label.grid(row=2,column=0)
email_username_entry=Entry(width=35)
email_username_entry.insert(0,"isha@gmail.com")
email_username_entry.grid(row=2,column=1,columnspan=2)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)
generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()
