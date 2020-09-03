from tkinter import *

def fun():
    #username and password will be autowritten upon calling below autologin function
    def autologin():      
        username.set("vinayak")
        password.set("password123")

    # Initiaizing tkinter
    login_screen = Tk()

    #Setting GUI Geometry
    login_screen.title("Auto login with python")

    #Creating a text lebel widget and packing it
    Label(login_screen, text = "Please enter login details").pack()

    Label(login_screen, text = "Username").pack()

    #declaring a string type variable to store username from entry widget
    username = StringVar()

    #declaring a string type variable to store password from entry widget
    password = StringVar()

    #Creating a entry widget to take username from user
    username_login_entry = Entry(login_screen, textvariable = username)
    #Packing entry widget on GUI screeen
    username_login_entry.pack()

    # Creating a text label widget and packing it
    l1 = Label(login_screen, text = "password").pack()

    #Creating a entry widget to take password from user
    password_login_entry = Entry(login_screen, textvariable = password)

    #Packing entry widget on GUI screeen
    password_login_entry.pack()

    #adding button to call autologin function
    Button(login_screen, text = "Apply auto fill", command = autologin).pack()
    
    #adding button to application screen to ask user to login
    Button(login_screen, text = "Login Now", width = 10, height = 1).pack(pady=10)

    #Running the mainloop when the code is ready
    login_screen.mainloop()

fun()


    



