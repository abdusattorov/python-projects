from random import randint
from words import verbs


def get_random_word():
    rand_num = randint(0, 633)
    return verbs[rand_num]


def display(letters, word):
    
    temp = list('-' * len(word))

    for i in range(len(letters)):
        for j in range(len(word)):
            if letters[i] == word[j]:
                temp[j] = letters[i]

    print("\n", "".join(temp))
    return "".join(temp)


def main():
    
    while True:

        strength = 10
        letters = []
        word = get_random_word()
        print(f"\n🤖: The word I have thought of has {len(word)} letters")

        while strength > 0:
            user_input = input("\n🤖: Enter a letter\n>>> ")
            letters.append(user_input)
            print(f"Your guesses: {letters}")

            if user_input not in word:
                strength -= 1
                print("Oops! Wrong guess.")

            print(f"Your strength: {strength}")

            temp = display(letters, word)

            if temp == word:
                print("You won!!!")
                break

        if strength == 0:
            print(f"You lost :(\nThe word was {word}")

        again = True

        while True:
            temp = input("Do you want to play again?\n[y/n]\n>>> ")
            if temp == 'n':
                again = False
                break
            elif temp == 'y':
                again = True
                break
            else:
                print("Wrong input!!! Enter 'y' or 'n'?")
            
        if not again:
            break


main()
