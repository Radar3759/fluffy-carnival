#up to task 3 works
from donation_pkg import homepage
from donation_pkg import user

database = {
    "admin": "password",
}
donations = {}
authorized_user = ("")
homepage.show_homepage()
if authorized_user == "":
    print("Your must be logged in to donate.")
else:
    print("Logged in as:", authorized_user)  

option = input("Choose an option 1-5: ")

while True:  
    
    if option == "1":
        username = input("\nEnter Username: ")
        password = input("Enter Password: ")
        authorized_user = user.login(database, username, password) 
    elif option == "2": 
        username = input("\nEnter Username: ")
        password = input("Enter Password")
        
        print("TODO: Write Register Functionality")
    elif option == "3": 
        print("TODO: Write Donate Functionality") 
    elif option == "4": 
        print("TODO: Write Show Donations Functionality") 
    elif option == "5":
        print("Goodbye!")
        break

