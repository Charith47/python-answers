# no of students in the class
NUMBER_OF_STUDENTS = 22


def get_input():
    marks = []
    for i in range(1, NUMBER_OF_STUDENTS + 1):
        try:
            user_input = int(input(f"Student idx[{i}] >> "))
        except ValueError:
            print("Please enter integers only.")
            break
        else:
            if 0 <= user_input <= 100:
                marks.append(user_input)
            else:
                print("Please enter values between 0-100.")
                break
    return marks


def display_bar_chart(marks):

    # check for empty list
    if len(marks) == 0:
        return

    index = 1
    print("\n\nSTUDENT MARKS\n")
    for mark in marks:
        print(f"student idx[{str(index).zfill(2)}]", end=" ")
        for i in range(0, mark + 1):
            print("*", end=" ")
        index += 1
        print()


if __name__ == "__main__":
    display_bar_chart(get_input())
