# Our quiz!
score=0

def quiz():
    global score
    global name
    name = input("Enter your name here: ")


    question1()
    question2()
    question3()

    print(name, "scored", score, "points, try again")
    if score == 3:
        print("Winner")

    else:
        print("Loser")

    

    

    
def question1():
    global score
    global name
    print("Here is your first question,", name)
    print(" ")
    print("==========================================================================")
    print(" ")
    print("1)What is The most popular cheese?")
    print("A. Blue Cheese")
    print("B. Goats Cheese")
    print("C. Cottage Cheese")
    print("D. Harry Tiltmans homemade cheese")

    answer = input("Answer:")

    if answer.upper() == "D":
        score == score+1
        print("Well Done, Have a singular point!")

    else:
        print("Your wrong Mate")
def question2():
    global score
    global name
    print(" ")
    print("==========================================================================")
    print(" ")
    print("2) What is Donald Trumps youngest son named?")
    print("A. Sassy")
    print("B. Barron")
    print("C. Legolas")
    print("D. Lezley")
    print("E. Donald Trump Junior Junior")

    answer = input("Answer: ")

    if answer.upper() == "B":
        score=score+2
        print("Well Done mate, have another point")

    else:
        print("You've only gone at got it wrong!")

def question3():
    global score
    global name
    print(" ")
    print("==========================================================================")
    print(" ")
    print("3) which car is the most expensive")
    print("A. BMW i8")
    print("B. Corvette z06")
    print("C. nissan skyline gtr 2016")
    print("D. Ford Mustang 2016")

    answer = input("Answer: ")

    if answer.upper() == "A":
        score=score + 1
        print("Nice one mate, have another point!")

    else:
        print("Mission failed, try harder next time:( ")


    


# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
