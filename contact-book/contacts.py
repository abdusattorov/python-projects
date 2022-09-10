contacts = {
    'Johnny' : {'name': 'John Doe', 'number':'202-456-1414', 'address': '1600 Pennsylvania Avenue NW, Washington, D.C.'},
    'Diana' : {'name': 'Diana Miares', 'number':'90-000-00-00', 'address': '67 Navoiy, Shayhontohur, Tashkent'}
    }

template = ['nickname', 'name', 'number', 'address']

def welcome():
    print("========================================")
    print("Contacts book".center(40))
    print("========================================")
    print("\nOptions:\n/s - search;\n/a - add a new entry;\n/l - show all;\n/q - quit.\n/u - update")


def print_match(i):

    print(
        '\n',
        f"Nickname: {i}\n",
        f"Full name: {contacts[i]['name']}\n",
        f"Phone number: {contacts[i]['number']}\n",
        f"Address: {contacts[i]['address']}\n"
        )


def yesNo():

    while True:
        yesNo = input("Do you want to override? [y/n]\n>>> ")
        if yesNo == 'y':
            return True
        elif yesNo == 'n':
            return False
        else:
            print("Invalid input!")


def addContact():

    nickname = input("Enter a nickname:\n - ")
    name = input("Enter a name:\n - ")
    number = input("Enter a phone number:\n - ")
    address = input("Enter an address:\n - ")
    add = False

    for i in contacts:
        if nickname.lower() == i.lower():
            print("\nEntry with such nickname already exists!\n")
            print_match(i)
            add = yesNo()
        elif name.lower() == contacts[i]['name']:
            print("\nEntry with such name already exists!\n")
            print_match(i)
            add = yesNo()
        else:
            add = True

    if add:
        contacts.update({nickname: {'name': name, 'number': number, 'address': address}})


def updateContact(nickname):

    # for nick in contacts:
    #     if nick == nickname:
    #         print("Do you want to change the nickname? [y/n]")
    #         change_nickname = input(">>> ")

    #         if change_nickname == 'y':
    #             new_nickname = input("What is the new nickname?\n>>> ")
    #         elif change_nickname == 'n':
    #             pass
            
    #         print("Do you want to change the name? [y/n]")

    print("what do you want to change?")
    print("/name\n/nickname\nnumber\naddress\n")
    user_input=input('>>> ')

    if user_input == '/nickname': 
        nick = input("Enter a nickname\n>>> ")
        new_nick = input("Enter a new nickname\n>>> ")
        contacts[new_nick] = contacts[nick]
        del contacts[nick]

    elif user_input == '/name':
        nick = input("Enter a nickname\n>>> ")
        new_name = input("Enter a new name\n>>> ")
        contacts[nick]['name'] = new_name

    elif user_input == '/number':
        nick = input("Enter a nickname\n>>> ")
        new_number = input("Enter a new number\n>>> ")
        contacts[nick]['number'] = new_number 

    elif user_input == '/address':
        nick = input("Enter a nickname\n>>> ")
        new_address = input("Enter a new address\n>>> ")
        contacts[nick]['address'] = new_address
        
    else:
        print("It is wrong :(")
        updateContact()


def searchContact():

    print("Enter a nickname/name/number:\n(example: Johnny or John Doe or 202-456-1414)")
    search_query = input(" - ")
    no_match = 1

    for i in contacts:

        if search_query.lower() == i.lower() or search_query.lower() ==  contacts[i]['name'].lower() or search_query.lower() == contacts[i]['number'].lower():
            no_match = 0
            print_match(i)
    
    if no_match:
        return print("\nNo Matches Found!\n")

            
def main():

    while True:
        
        welcome()
        
        choice = input(">>> ")

        if choice == '/s':
            searchContact()
        elif choice == '/a':
            addContact()
        elif choice == '/q':
            break
        elif choice == '/l':
            for i in contacts:
                print_match(i)
        elif choice == '/u':
            print("Enter the nickname of the person to be updated")
            update = input('>>> ')

            if update in contacts:
                updateContact(update)
            elif update not in contacts:
                print("Sorry, you entered a wrong nickname :(")
        

        else:
            print("Wrong Command!!!")
            print("Restarting...")


main()
