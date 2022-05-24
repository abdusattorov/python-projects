from random import randint


def user_plays():
    print("\n🤖: I am thinking of a number in range 1 to 10... \nCan you guess it?\n")
    target = randint(1, 10)
    user_attempt = 1

    while True:

        guess = int(input(">>> "))

        if guess > target:
            print("🤖: You guessed too high! Try again...")
        elif guess < target:
            print("🤖: You guessed too low! Try again...")
        elif guess == target:
            print(f"🤖: Woah!!! My number was {target} and it took you {user_attempt} attempts to get it right.\n")
            break

        user_attempt += 1

    return user_attempt


def cpu_plays():
    print("🤖: Now it's my turn to guess :)")
    input("🤖: Click any key if you have thought of a number in range 1 to 10\n>>> ")
    cpu_attempt = 1
    start = 1
    end = 10

    while True:

        guess = randint(start, end)

        print(f"\n🤖: Is it {guess}?")
        hint = input("🤖: Click [C] if correct, [+] if your number is higher, [-] if your number is lower\n>>> ").upper()

        if hint == 'C':
            print(f"🤖: I got it right after {cpu_attempt} attempts.")
            break
        elif hint == '+':
            start = guess+1
        elif hint == '-':
            end = guess

        cpu_attempt += 1

    return cpu_attempt


def main():

    while True:
        user = user_plays()
        cpu = cpu_plays()

        if user < cpu:
            print("🤖: You won!!! Congratulations 🎉")
        elif user > cpu:
            print("🤖: I won 😎")
        else:
            print("🤖: It's a draw. Nice game 🤝")

        play_again = input("Do you want to play again? [1] - yes / [0] - no\n>>> ")

        if play_again == '0':
            break
        elif play_again == '1':
            pass
        else:
            break


main()