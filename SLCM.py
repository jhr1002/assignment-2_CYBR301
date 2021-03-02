#Anthony Colon Jake Rowe
import base64
from Cryptodome.Cipher import AES
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
    data = b'password'
    key = b'1234567890123456'
    cipher = AES.new(key, AES.MODE_EAX)
    ciphered_data, tag = cipher.encrypt_and_digest(data)

    encoded_data = base64.b64encode(ciphered_data)

    f = open("assignment-2_CYBR301/credential.dat", "ab")
    f.write(username.encode())
    f.write(encoded_data)
    f.flush()
    f.close()

    #file = open("assignment-2_CYBR301/credential.dat", "wb")
    #file.write(cipher.nonce)
    #file.write(tag)
    #file.write(ciphered_data)
    #file.write("\n\n\n")
    #file.flush()
    #file.close()
    print("Username and Password stored in credential.dat")
def main():
    username, password = getusername_paswd();
    if username != None:
        if password != None:
            secure_store(username, password);

if __name__ == "__main__":
    main()
