from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
WHITE="#FFFFFF"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK_GREEN="#3d5300"
YELLOW = "#f7f5dd"
ORANGE="#F09319"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list=[random.choice(letters+numbers+symbols) for _ in range(random.randint(18,22))]
    random.shuffle(password_list)
    password="".join(password_list)
    return password

def create_password():
    pw_entry.delete(0,END)
    pw=generate_password()
    pw_entry.clipboard_clear()
    pw_entry.clipboard_append(pw_entry.get())
    pw_entry.insert(0,pw)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    if len(website_entry.get())==0 or len(pw_entry.get())==0 or len(email_entry.get())==0:
        warning=messagebox.showinfo(title="Invalid entry",message="You can not leave empty areas.")
    else:
        is_ok=messagebox.askokcancel(title="Title",
                               message=f"There are the information you entered:\nWebsite: {website_entry.get()}\n"
                                       f"Email: {email_entry.get()}\nPassword: {pw_entry.get()}\n"
                                       f"Do you want to save it?")
        if is_ok:
            with open("data.txt","a") as file:
                file.write(website_entry.get() + " | " + email_entry.get() + " | " + pw_entry.get()+"\n")
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                pw_entry.delete(0,END)
                website_entry.focus()
        else:
            return

# ---------------------------- UI SETUP ------------------------------- #
#Creating window
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg=WHITE)

#Inserting logo
canvas=Canvas(width=200,height=200,bg=WHITE,highlightthickness=0)
image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)

#Texts
website_text=Label(text="Website:",bg=WHITE)
website_text.grid(row=1,column=0)

email_text=Label(text="Email/Username:",bg=WHITE)
email_text.grid(row=2,column=0)

pw_text=Label(text="Password:",bg=WHITE)
pw_text.grid(row=3,column=0)

#Entries
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)

website_entry.focus()


email_entry=Entry(width=35)
email_entry.insert(END,"@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)

pw_entry=Entry(width=20)
pw_entry.grid(row=3,column=1)

#Buttons
generate_button=Button(text="Generate Password",command=create_password)
generate_button.grid(row=3,column=2)

add_button=Button(text="Add",command=save_info,width=36)
add_button.grid(row=4,column=1,columnspan=2)




window.mainloop()