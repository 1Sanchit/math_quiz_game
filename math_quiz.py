import random

print("welcome to n the Math Quiz Game!")
name = input("Enter your Name:")

score = 0

for i in range(1,6):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    op = random.choice(['+','-','*'])

    if op == '+':
          ans = num1 + num2
    elif op == '-':
         ans = num1 - num2
    else:
       ans = num1 * num2

    print(f"Question {i}: {num1} {op} {num2} = ?")
    user = int(input("your answer: "))

    if user == ans:
        print("correct!\n")
        score += 1
    else:
       print(f"wrong! correct answer was {ans}\n")

print(f"{name}, your score is {score}/5.")

