def ask_question(question, answer):

    while True:
        try:
            user_answer = int(input(question))

            if user_answer == answer:
                print("Correct, well done!\n")
                return 1
            
            else:
                print("Incorrect, please try again.")

        except ValueError:
            print("Please enter a number, not a letter.\n")