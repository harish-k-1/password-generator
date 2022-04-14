from random import *
pass_len = int(input("Password Length: "))
numbers = ['1','2','3','4','5','6','7','8','9','0']
lchar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uchar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','#','$','%','^','&','*']
combined = numbers + lchar + uchar + symbols

rand_num=choice(numbers)
rand_lchar=choice(lchar)
rand_uchar=choice(uchar)
rand_sym=choice(symbols)
temp_pass = rand_num + rand_lchar + rand_uchar + rand_sym

for i in range(pass_len-4):
    temp_pass = temp_pass + choice(combined)  #temp_pass is a string

arr=[]
for i in temp_pass:
    arr.append(i)    #convert to list and shuffle
shuffle(arr)

passw=''.join(arr)  #again converting back to string
print(passw)

inp=input("Do you want to save this password?(Y/N)\t")
if inp == "Y" or "y":
    f = open("passfile.txt","a")
    note = input("Leave a note:\t")
    f.write(f"\n{note}: {passw}")
    f.close()