#Anthony Colon Jake Rowe

def getusername_paswd():
    validboth = True
    #We need to use inputs for user and password
    username=input("Username:")
    password=input("Password:")  #We can write the rules here if needed but not in directions

#This is where we have to validate using if and if not any statements for user name and password
    SpecialChar=['#','@','%','*']
    if len(password)<8:
        validboth = False
    if not any(char.isdigit() for char in password): #This should be for if there us no numbers
        validboth = False
    if not any(char.isupper() for char in password): #Requires uppercase in password
        validboth = False
    if not any(char.islower() for char in password): #Requires lowercase
        validboth = False
    if not any(char in SpecialChar for char in password):
        validboth = False
    if not any(char in SpecialChar for char in password):
        validboth = False

    if validboth:
        print('Valid username of: ' + username)
        print('Valid password of: ' + password)
        return username, password
    else:
        print('Invalid username of: ' + username)
        print('Invalid password of: ' + password)
        return None, None

def secure_store(username, password):
    print(username + password)
    eusername = username
    epassword = password
    f = open("crednetial.dat", "a")
    f.write(eusername + epassword)
    f.close()

def main():
    username = ""
    password = ""
    username, password = getusername_paswd();
    secure_store(username, password);

if __name__ == "__main__":
    main()
