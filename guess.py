import random
import sys


def get_user_secret():
    try:
        user_input = int(input("Enter your secret number (1-10): "))
    except ValueError:
        print("Please enter integers only.")
        sys.exit()
    else:
        if 1 <= user_input <= 10:
            return user_input
        else:
            print("Please enter values between 1-10.")
            sys.exit()


def guess_secret(user_secret):
    won = False
    # set seed -> system time
    random.seed()

    # list for already guessed numbers
    guess_list = []
    for tries in range(1, 11):

        while True:
            guess = random.randint(1, 10)

            # already guessed?
            if guess in guess_list:
                continue
            else:
                guess_list.append(guess)
                break

        # uncomment below to see all the numbers guessed by computer
        # print(guess_list)

        if guess == user_secret:
            won = True
            if tries == 1:
                print("You are great")
            print(f"Secret Number is: {guess}")
            print(f"Number of tries: {tries}")
            break
    if not won:
        print("Nasty Defeat")


if __name__ == "__main__":
    guess_secret(get_user_secret())
