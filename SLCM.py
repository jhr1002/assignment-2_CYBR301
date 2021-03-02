#Anthony Colon Jake Rowe

def getusername_paswd():
    validboth = True

    username=input("Username:")
    password=input("Password:")

    SpecialChar=['#','@','%','*']
    Email=['@']
    if len(password)<8:
        validboth = False
    if not any(char.isdigit() for char in password):
        validboth = False
    if not any(char.isupper() for char in password):
        validboth = False
    if not any(char.islower() for char in password):
        validboth = False
    if not any(char in SpecialChar for char in password):
        validboth = False
    if not any(char in SpecialChar for char in password):
        validboth = False
    if not any(char in Email for char in username):
        validboth=False

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
