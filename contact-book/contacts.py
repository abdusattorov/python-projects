contacts = {
    'Johnny' : {'name': 'John Doe', 'number':'202-456-1414', 'address': '1600 Pennsylvania Avenue NW, Washington, D.C.'},
    'Diana' : {'name': 'Diana Miares', 'number':'90-000-00-00', 'address': '67 Navoiy, Shayhontohur, Tashkent'}
    }

def welcome():
    print("========================================")
    print("Contacts book".center(40))
    print("========================================")
    print("\nOptions:\n/s - search;\n/a - add a new entry;\n/l - show all;\n/q - quit.\n")


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
        else:
            print("Wrong Command!!!")
            print("Restarting...")


main()
