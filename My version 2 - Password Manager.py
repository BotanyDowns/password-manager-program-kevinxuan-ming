

# Creating empty dictionaries to store accounts and passwords
passwords = {}
users = {}



print("""Welcome to Password Manager!
(Hint: sign up first if first time)""")

def menu():
    choice = input("""Select your options below:
1. Log in
2. Sign up
3. Exit
Option: """)
    return choice

def menu2():
    choice = input("""Which function are you looking for?:
1. Add new passwords
2. View passwords
3. Log out
Option: """)
    if choice in ['1','2','3']:
        return choice
    else:
        print ("Invalid answer please try again.")
    
def log_in():
    while True:
        username1 = input("Enter username: ")
        password1 = input("Enter password: ")
        if username1 in users and users[username1] == password1:
            print("Account found!")
            while True:
                choice=menu2()
                if choice =="1":
                    add_password(username1)
                elif choice == "2":
                    view_passwords(username1)
                elif choice =="3":
                    break
                else:
                    print("Invalid answer please try again.")
                        
            
            return
                    
        else:
            print("Account not found.")
            menu()
            
def sign_up():
    username2 = input("Enter username: ")
    password2 = input("Enter password: ")
    print ("Account created")
    
    users[username2] = password2



def add_password(username):
    web = input ("Enter website or app: ")
    password3 = input ("Enter password: ")
    print ("Detail added to the account.")
    if username not in passwords:
        passwords[username] = {}
    passwords[username][web] = password3



def view_passwords(username):
    if username in passwords:
        print(passwords[username])
    else:
        print("No passwords found for this user.")

def main():
    while True:
        choice = menu()
        if choice == "1":
            log_in()
        elif choice == "2":
            sign_up()
        elif choice == "3":
            break       
        else:
            print("Invalid choice, please try again.")

# Call the main function to start the program
main()


    
    




            
    
        

