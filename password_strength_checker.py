
def strength_checker(password,rating_counter):
    
    upper_counter,lower_counter,character_counter,numeric_counter = 0,0,0,0
    for i in password:
        if i.isupper():
            upper_counter += 1
        if i.islower():
            lower_counter += 1
        if i.isnumeric():
            numeric_counter += 1
        for character in characters:
            if i == character:
                character_counter = character_counter + 1
    if len(password) >= 8:
        print("[+] The lenght seems ok [+]")
        rating_counter += 1

    else:
        print("[-] Poor choice! not enough length[-] ")   
    print(rating_counter)
            
    if upper_counter >= 1 and lower_counter >= 1  and len(password)>=8:
        print("[+] Contains both upperscae and lowercase! Good ")
        rating_counter = rating_counter+ 1
        print(rating_counter)

    elif (upper_counter >= 1 or lower_counter >= 1)  and len(password)>=8:
        rating_counter += 0.5
        print(rating_counter)
        print("[+] Not bad at lease either upper or lcase [+]")
    elif((upper_counter >= 1 or lower_counter >= 1)  and len(password)<= 8):
        print("[-] Got the case work on length [-]")
    else:
        print(" [-] Again bad choice here [-] ")
    print(rating_counter)
    
    
    if numeric_counter >=3 and len(password)>=8:
        print("[+] Contains {} numbers! Good [+] ".format(numeric_counter))
        rating_counter += 1
        print(rating_counter)

    elif numeric_counter >=1  and len(password)>=8 :
        print("[+] At least a digit [+]")
    elif((numeric_counter >= 1)  and len(password)<= 8):
        print("[-] Got the digit work on length [-]")
        rating_counter += 0.5
        print(rating_counter)

    else:
        print("[-] no any digits [-]")
    
    print(rating_counter)
    
    if character_counter >=2 and  len(password)>=8:
        print("[+] Good more than a character [+] ")
        rating_counter += 1
        print(rating_counter)

    elif(character_counter == 1 and  len(password)>=8):
        print("[-] at least a chracter [-]")
        rating_counter += 0.5    

    elif(character_counter >=1 and  len(password)<=8):
        print("[-] Got the character work on length [-]")
    else:
        print("[-] Bad choice no chracters [-]")

    print("the final rating counter is :",end=" ")
    print(rating_counter)
    if rating_counter == 4:
        print("The pssword is strong!")
    elif rating_counter >=2.5:
        print("The password is ok")
    else:
        print("The password is poor")


rating= 0
characters = ("!@#$%^&*()_+{}:"">?<,./;'")
user_password = input("Enter the pass password: ")
strength_checker(user_password,rating)


