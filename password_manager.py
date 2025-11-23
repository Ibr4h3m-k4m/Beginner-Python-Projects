from cryptography.fernet import Fernet

"""def write_key():
    key = Fernet.generate_key()
    with open('key.key' , "wb") as key_file:
        key_file.write(key)

write_key()"""

def load_key():
    file = open("key.key",'rb')
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

def add():
    name = input("Please Input the Account name: ")
    pwd = input("And the Password for this account: ")
    with open("passwords.txt",'a') as f:
        f.write(name + "|" +  fer.encrypt(pwd.encode()).decode() + "\n")  

def view():
    with open("passwords.txt",'r') as f:
        for line in f.readlines():
            data = line.rstrip() # to remove the \n 
            user ,pwd = data.split("|")
            print("User:", user , "| Password:", fer.decrypt(pwd.encode()).decode() )


while 1:
    mode = input("Would you like to add a new password or view existing ones (view,add), press q to quit? ").lower()
    if mode =="q":
        break
    
    if mode =="view":
        view()
    elif mode =="add":
        add()
    else:
        print("Invalid option!")
        continue