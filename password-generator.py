from random import *
from string import *
import pyperclip
import time

pass_len = int(input("Password Length: "))
numbers = digits
lchar = ascii_lowercase
uchar = ascii_uppercase
symbols = "!@#$%^&*"
combined = numbers + lchar + uchar + symbols
temp_pass = choice(numbers)+choice(lchar)+choice(uchar)+choice(symbols)

for i in range(pass_len-4):
    temp_pass = temp_pass + choice(combined)

arr=list(temp_pass)  #convert to list and shuffle
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