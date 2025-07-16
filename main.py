from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?', '\\', '|', '`', '~']

    nr_letters = random.randint(8,10)
    nr_numbers = random.randint(2,4)
    nr_symbols = random.randint(2,4)


    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_nums = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symb = [random.choice(letters) for _ in range(nr_symbols)]

    password_list = password_letters + password_symb + password_nums

    random.shuffle(password_list)
    password = ''.join(password_list)
    passInput.insert('0',password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = websiteInput.get()
    email = emailInput.get()
    password = passInput.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title='Warning',message='Please fill in all the fields')
    else:
        messageBoxOutput = messagebox.askokcancel(title=website,message=f'Email:{email}\nPassword:{password}')
        if messageBoxOutput:
            f = open('passwords.txt','a')
            f.write(f'{email} || {password} || {website}\n')
            emailInput.delete(0,'end')
            passInput.delete(0, 'end')
            websiteInput.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(pady=20,padx=20,bg="#fff")
mypassLogo = PhotoImage(file='logo.png')

canvas = Canvas(window,width=400,height=400,bg="#fff",highlightthickness=0)
myimg = canvas.create_image(200,200,image=mypassLogo)
canvas.grid(row=0,column=1)

websiteLabel = Label(text="Website:",font=("Inter",16),bg="#fff",fg="#000")
websiteLabel.grid(row=1,column=0)

emailLabel = Label(text="Email / Username:",font=("Inter",16),bg="#fff",fg="#000")
emailLabel.grid(row=2,column=0)

passLabel = Label(text="Password:",font=("Inter",16),bg="#fff",fg="#000")
passLabel.grid(row=3,column=0)

websiteInput = Entry(width=35,background="#fff",fg="#000",highlightcolor="#e8e8e8",highlightthickness=0.5)
websiteInput.grid(row=1,column=1,sticky="EW",columnspan=2)

emailInput = Entry(width=35,background="#fff",fg="#000",highlightcolor="#e8e8e8",highlightthickness=0.5)
emailInput.insert(0,'loginmmail@gmail.com')
emailInput.grid(row=2,column=1,sticky="EW",columnspan=2)

passInput = Entry(width=21,background="#fff",fg="#000",highlightcolor="#e8e8e8",highlightthickness=0.5)
passInput.grid(row=3,column=1,sticky="EW")

genButton = Button(text='Generate',bg="#fff",highlightthickness=0,relief='flat',bd=0,command=pass_gen)
genButton.grid(row=3,column=2,sticky="EW")

saveButton = Button(text='Save',bg="#fff",highlightthickness=0,relief='flat',bd=0,command=save_password)
saveButton.grid(row=4,column=1,columnspan=2,sticky="EW")




window.mainloop()