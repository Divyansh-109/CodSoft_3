import random
import string
small = string.ascii_lowercase  # Lowercase letters
capital = string.ascii_uppercase # Uppercase letters
digits = string.digits  # Numbers
symbols = string.punctuation # Symbolic Characters

# Function to generate random password of desired length
def generate_password(length):
    
    len_1 = round(length*(30/100))  # 30% of the length will be lowercase letters and 30% will be uppercase letters

    len_2 = round(length*(20/100))  # 20% of the length will be digits and 20% will be symbols
    
    password_list = []  # List to store the password
    for i in range(len_1):
        password_list.append(random.choice(small)) 
        password_list.append(random.choice(capital))

    for i in range(len_2):
        password_list.append(random.choice(digits))
        password_list.append(random.choice(symbols))

    random.shuffle(password_list) # Shuffle the list of characters
    password = "".join(password_list) # Convert the list to a string

    return password

# Function to generate custom password of desired length
def generate_password_custom(length, part_1, part_2, part_3):
    if part_1 + part_2 + part_3 == 100:
        len_1 = round(length*(part_1/100))  # Part 1 of the length will be letters

        len_2 = round(length*(part_2/100)) # Part 2 of the length will be digits

        len_3 = round(length*(part_3/100)) # Part 3 of the length will be symbols

    else:
        print("The sum of the parts of percent should be 100")
        return None
    password_list = []
    for i in range(int(len_1/2)):
        password_list.append(random.choice(small))
        password_list.append(random.choice(capital))
    
    for i in range(len_2):
        password_list.append(random.choice(digits))

    for i in range(len_3):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    password = "".join(password_list)
    return password
    
def main():
    print("\nWelcome to the password generator program.")
    print('''1. Generate Random Password(Press 1)
2. Generate Custom Password(Press 2)
3. Exit(Enter "q" or 3 to exit)''')

    while True: 
        choice = input("Enter your choice: ")
        
        if choice == "1":
            length = int(input("Enter the length of password: "))
            print("The generated password is: ",generate_password(length))
        elif choice == "2":
            length = int(input("Enter the length of password: "))
            part_1 = int(input("Enter the percent of letters in password: "))
            part_2 = int(input("Enter the percent of numbers in password: "))
            part_3 = int(input("Enter the percent of symbols in password: "))
            password = generate_password_custom(length,part_1,part_2,part_3)
            print("The generated password is: ",password)
        elif choice == "3" or choice == "q":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

main()

        
