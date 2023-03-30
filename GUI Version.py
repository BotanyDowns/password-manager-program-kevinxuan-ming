from tkinter import*
root= Tk()
root.title("Password Manager")
root.geometry ("300x300")

unpw = {}

def frame1():
    global frame1

    frame1= Frame (root, bg='lime')
    frame1.grid(row=0,column=0,sticky='nsew')

    #placing the objects in frame1
    lblsign_up = Label (frame1, text = "Sign Up")
    lblsign_up.grid(row=0, column=0)

    
    lblUser = Label (frame1,text = "Username")
    lblUser.grid(row=1,column=0)

    entryUser=Entry (frame1)
    entryUser.grid (row=1,column=1)

    lblPass = Label (frame1,text="Password")
    lblPass.grid (row= 2, column=0)

    entryPass = Entry (frame1,show='*')
    entryPass.grid (row=2, column=1)

    btnLogin= Button (frame1, text = 'Log in', command= frame3)
    btnLogin.grid(row=3,column=1)

def frame3():
    global frame3
    
    frame3 = Frame (root, bg= 'blue')
    frame3.grid (row=0, column=0, sticky = 'nsew')

    root.title("Account Created!")
    lbloption = Label (frame3, text = "What are you after?")
    lbloption.grid (row=0, column=0)

    btnaddpassword = Button (frame3, text= ' Add Password', command= frame2)
    btnaddpassword.grid(row=1, column=0)

    btnviewpasswords = Button (frame3, text = 'View Password(s)', command = print  (unpw))
    btnviewpasswords.grid(row=2, column=0)

    btnlogout= Button (frame3, text = 'Log Out', command = frame4)
    btnlogout.grid (row=3, column =0)


def frame4():
    global frame4
    root.title ("Password Manager")

    frame4= Frame (root, bg='lime')
    frame4.grid(row=0,column=0,sticky='nsew')

    #placing the objects in frame4
    lblsign_up = Label (frame4, text = "Sign Up")
    lblsign_up.grid(row=0, column=0)

    
    lblUser = Label (frame4,text = "Username")
    lblUser.grid(row=1,column=0)

    entryUser=Entry (frame4)
    entryUser.grid (row=1,column=1)

    lblPass = Label (frame4,text="Password")
    lblPass.grid (row= 2, column=0)

    entryPass = Entry (frame4,show='*')
    entryPass.grid (row=2, column=1)

    btnLogin= Button (frame4, text = 'Log in', command= frame3)
    btnLogin.grid(row=3,column=1)
    

def frame2():
    global frame2
    frame2 = Frame (root, bg ='red')
    frame2.grid (row=0,column=0 , sticky= 'nsew')

    lblmessage = Label (frame2, text = "Add Passoword")
    lblmessage.grid(row=0, column =0)

    lblAccount = Label (frame2,text="Website")
    lblAccount.grid(row=1,column=0)

    global entryAccount
    entryAccount= Entry(frame2)
    entryAccount.grid(row=1, column=1)

    lblPass= Label (frame2, text = "Password")
    lblPass.grid (row=2, column=0)

    global entryPass
    entryPass = Entry(frame2)
    entryPass.grid(row=2, column=1)

    btnEnter = Button (frame2, text = "Add", command=lambda:accounts())

    btnEnter.grid (row=3,column=1)

    btngoback = Button (frame2,text = 'Go back', command=frame5)
    btngoback.grid (row=3, column=0)



def frame5():
    global frame5
    
    frame5 = Frame (root, bg= 'blue')
    frame5.grid (row=0, column=0, sticky = 'nsew')

    root.title("Account Created!")
    lbloption = Label (frame5, text = "What are you after?")
    lbloption.grid (row=0, column=0)

    btnaddpassword = Button (frame5, text= ' Add Password', command= frame2)
    btnaddpassword.grid(row=1, column=0)

    btnviewpasswords = Button (frame5, text = 'View Password(s)', command = print(unpw))
    btnviewpasswords.grid(row=2, column=0)

    btnlogout= Button (frame5, text = 'Log Out', command = frame4)
    btnlogout.grid (row=3, column =0)



def accounts():
    unpw[entryAccount.get()]=entryPass.get()
    print("Website: " ,entryAccount.get(),"Password: " ,entryPass.get())
    entryAccount.delete(0,END)
    entryPass.delete(0,END)
    
frame1()
    

root.mainloop()
