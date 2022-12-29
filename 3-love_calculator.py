#This code written very seriously in an afford to make easier to caculate true love in a way that published on buzzfeed, in case you need it
#Article URL --> https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love
#Challenge URL --> https://app.codingrooms.com/management/assignments/364926/overview

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

x = name1.lower()
y = name2.lower()

val_true4x = int(x.count("t") + x.count("r") + x.count("u") + x.count("e"))
val_true4y = int(y.count("t") + y.count("r") + y.count("u") + y.count("e"))

love4x = int(x.count("l") + x.count("o") + x.count("v") + x.count("e"))
love4y = int(y.count("l") + y.count("o") + y.count("v") + y.count("e"))

true_toral = val_true4x + val_true4y
love_total = love4x + love4y

score = int(f"{true_toral}{love_total}")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
