from random import *
from string import *
import pyperclip
import time

def generate_password(pass_len):
    symbols = "!@#$%^&*"
    combined = digits + ascii_lowercase + ascii_uppercase + symbols
    temp_pass=choice(digits)+choice(ascii_lowercase)+choice(ascii_uppercase)+choice(symbols)

    for i in range(pass_len-4):
        temp_pass += choice(combined)

    arr=list(temp_pass)  #convert to list in order to shuffle
    shuffle(arr)
    passw=''.join(arr)  #again converting back to string
    print(passw)

    inp=input("Do you want to save this password?(Y/N)\t")
    if inp == "Y" or inp == "y":
        f = open("passfile.txt","a")
        note = input("Leave a note:\t")
        f.write(f"{note}: {passw}\n")
        pyperclip.copy(passw)
        print("Password copied to clipboard")
        f.close()
        time.sleep(10)
    else:
        inp2=input("Do you want another password?(Y/N)\t")
        if inp2=="Y" or inp2=="y":
            generate_password(pass_len)

if __name__ == "__main__":
    pass_len = int(input("Password Length: "))
    generate_password(pass_len)