""" This program asks the user for a quiz score
    and converts that numeric score to a letter grade.

    author: Fatih IZGI
    date: 07-Feb-2020
    version: python 3.6.9
"""

while True: # loop until getting a valid input from the user
    try:
        score: float = float(input("Enter a score to convert it to a letter grade: "))

        if 0 <= score <= 100:
            break # end loop if input is valid
        else:
            print("The score should be between [0 and 100]") # warn user about the ranges
    except ValueError: # warn user about bad input
        print("Value Error! You should enter a number!")

letter_grade: str = "" # define a variable to store the letter grade

if score >= 93:
    letter_grade = "A"
    print(f'Your letter grade is "{letter_grade}" (93 <= {score} < 100)')
elif 90 <= score < 93:
    letter_grade = "A-"
    print(f'Your letter grade is "{letter_grade}" (90 <= {score} < 93)')
elif 87 <= score < 90:
    letter_grade = "B+"
    print(f'Your letter grade is "{letter_grade}" (87 <= {score} < 90)')
elif 83 <= score < 87:
    letter_grade = "B"
    print(f'Your letter grade is "{letter_grade}" (83 <= {score} < 87)')
elif 80 <= score < 83:
    letter_grade = "B-"
    print(f'Your letter grade is "{letter_grade}" (80 <= {score} < 83)')
elif 70 <= score < 80:
    letter_grade = "C"
    print(f'Your letter grade is "{letter_grade}" (70 <= {score} < 80)')
elif score < 70:
    letter_grade = "F"
    print(f'Your letter grade is "{letter_grade}" (0 <= {score} < 70)')
