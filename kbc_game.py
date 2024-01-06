'''
Creating a "Kaun Banega Crorepati(KBC)" program
'''


print("<------------>   \"Kaun Banega Crorepati?\" Game starts!   <------------>")


question_list = [
    "What is Your name?",
    "What is your age? \n a.25 b.30 \n c.27 d.40",
    "What is the capital of \"Turkey\"? \n a.Istanbul b.Kolkata \n c.New York d.Dhaka",
    "What is the currency of \"China\"? \n a.Yuan b.Pound \n c.Dollar d.Euro"
]
answers = [25, "Istanbul", "Yuan"]

print(question_list[0])
name = input()

print("Okay! Let's Get Started,", name)

amount1 = 0
amount2 = 0
amount3 = 0

print(question_list[1])
answer2 = input().lower()
if answer2 == 'a' or answer2 == '25':
    amount1 = 2000
    print("Congratulations! You have won $",amount1)
else:
    print("You Lose The Game!")

print(question_list[2])
answer3 = input().lower()
if answer3 == 'a' or answer3 == 'istanbul':
    amount2 = 3000
    print("Congratulations! You have won $",amount2)
else:
    print("You Lose The Game!")

print(question_list[3])
answer4 = input().lower()
if answer4 == 'a' or answer4 == 'yuan':
    amount3 = 4000
    print("Congratulations! You have won $",amount3)
else:
    print("You Lose The Game!")

total_amount = amount1 + amount2 + amount3
print("You Have Earned $", total_amount)
