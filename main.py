from questions import questions
from functions import ask_question

def main():

    score = 0

    print("Hello, welcome to Maddie's linear equations quiz! There are five questions. Good luck!!")

    for question, answer in questions:
        score += ask_question(question, answer)

    print("End of quiz!")
    print("You have scored", score, "out of", len(questions))

main()