
import random,pyperclip

def passwordGenerator(l):
    generated_password = ""
    for i in range(1, l+1):
        generated_password += random.choice(combined_list)
    print(generated_password)
    prompt = input("Do you want to copy it to your clipboard?(y/n): ")
    if prompt == 'y' or prompt ==  'yes':
        pyperclip.copy(generated_password)
        print("Copied succefully! GO paste it now")
    else:
        print("Thank you for using!")




Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
Lcase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
Ucase_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
Symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

combined_list = Lcase_characters + Ucase_characters + Symbols + Digits
random.shuffle(combined_list)



try:
    user_length = int(input("Lengt--> "))
    if user_length >= 8:
        passwordGenerator(user_length)
    else:
        print("Lenght is too less")
except ValueError:
    print("Lenght in number no string.")


