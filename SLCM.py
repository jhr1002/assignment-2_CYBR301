#Anthony Colon Jake Rowe

def getusername_paswd():
    #We need to use inputs for user and password
    username=input("Username:")
    password=input("Password:")  #We can write the rules here if needed but not in directions

#This is where we have to validate using if and if not any statements for user name and password
    if len(password)<8:
        validboth = False
    if not any(char.isdigit() for char in password): #This should be for if there us no numbers
        validboth = False
    if not any(char.isupper() for char in password): #Requiers uppercase in password
        validboth = False
    if not any(char.islower() for char in password): #Requiers lowercase
        validboth = False

    if validboth:
        return username, password
    else:
        return None,None


