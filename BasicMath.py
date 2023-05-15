import random
import time

right = 0  # initialize the number of right inputs to 0
wrong = 0  # initialize the number of wrong inputs to 0

while True:
    num1 = random.randint(1, 10)  # generate a random number between 1 and 10
    num2 = random.randint(1, 10)  # generate another random number between 1 and 10
    operator = random.choice(['+', '-'])  # randomly choose between addition and subtraction

    # calculate the result of the math problem
    if operator == '+':
        result = num1 + num2
    else:
        result = num1 - num2
    time.sleep(1)

    # check if the result exceeds 10 or is negative
    if result > 10 or result < 0:
        continue  # skip this math problem and generate a new one

    # present the math problem to the user
    print(f"""
###############################
       What is {num1} {operator} {num2}?
###############################""")
    
    # get the user's answer
    answer = input("Enter your answer:  ")

    # check if the user wants to quit
    if answer == 'q':
        break

    # check if the answer is an integer
    try:
        answer = int(answer)
    except ValueError:
        print("That's not a number!  Try again.")
        continue  # skip this math problem and generate a new one

    # check if the answer is correct
    if answer == result:
        print("Correct!")
        right += 1  # increment the number of right inputs
    else:
        print(f"Incorrect. The correct answer is {result}.")
        wrong += 1  # increment the number of wrong inputs

# calculate the percentage of right inputs
total = right + wrong
if total == 0:
    percentage = 0
else:
    percentage = (right / total) * 100

# print the final results
print(f"Total right: {right}")
print(f"Total wrong: {wrong}")
print(f"Grade: {percentage:.2f}%")
