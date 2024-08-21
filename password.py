#add neccesary libraries
import random
import string
#generate length of password and options for wahat to include
length = int(input("How long would you like your password to be "))
print('''Please Pick An Option:
      1. Digits
      2. Special Characters
      3. Upper Case Letters''')
   # give the password a name
password = ""
   # create the loop for the options and assign what each does
while(True):
    choice = int(input("Please Select Your Choice Now "))
    if (choice == 1):
       #give them digits
        password += string.ascii_letters
    elif(choice == 2):
       # give them special characters
        password += string.punctuation
    elif(choice == 3):
        #give them upper case characters
        password += string.digits
    else:
        break
#create the password
password = ''.join(random.choice(password) for _ in range(length))      
print("Your password is", password)
        