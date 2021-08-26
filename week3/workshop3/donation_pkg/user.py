def login(database, username, password):
    while True:
        if 'admin' in username and 'password' in password:
            print("Welcome, ", username)
        else:
            print("Login Failed.")
            
