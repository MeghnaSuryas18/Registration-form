from tkinter import *

root = Tk()
root.title("Registration")
root.geometry("600x470")
root.resizable(False, False)

def register():
    name_info = nameValue.get()
    phone_info = phoneValue.get()
    gender_info = genderValue.get()
    email_info = emailValue.get()
    
    with open(name_info + ".txt", "w") as file:
        file.write("Name: " + name_info + "\n")
        file.write("Phone: " + phone_info + "\n")
        file.write("Gender: " + gender_info + "\n")
        file.write("Email: " + email_info + "\n")

    # Clear the input fields after registration
    nameValue.set("")
    phoneValue.set("")
    genderValue.set("")
    emailValue.set("")

# Create input variables
nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emailValue = StringVar()

# Title Label
Label(root, text="Python Registration Form", font="Arial 25").pack(pady=50)

# Labels and Entry fields
Label(root, text="Name", font=23).place(x=100, y=150)
Entry(root, textvariable=nameValue, font=20).place(x=250, y=150)

Label(root, text="Phone", font=23).place(x=100, y=200)
Entry(root, textvariable=phoneValue, font=20).place(x=250, y=200)

Label(root, text="Gender", font=23).place(x=100, y=250)
Entry(root, textvariable=genderValue, font=20).place(x=250, y=250)

Label(root, text="Email", font=23).place(x=100, y=300)
Entry(root, textvariable=emailValue, font=20).place(x=250, y=300)

# Register button
Button(root, text="Register", command=register, font=20).place(x=250, y=350)

root.mainloop()
