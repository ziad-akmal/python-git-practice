options_list = ['a', 'b', 'c', 'd']
yes_no_list = ['y' , 'n']
answers_list = ['a', 'c', 'b', 'b', 'd', 'c', 'b', 'b', 'a', 'c', 'c', 'b', 'c', 'd', 'b','b']
num_of_qustions = 16

def quiz_start():
    score = 0
    corr_ans_index = 0

    with open(r"C:\Users\DELL\OneDrive\Desktop\question_manager\questions.txt","r") as my_questions_file:
        my_questions_file.readline()
        my_questions_file.readline()

        for i in range(num_of_qustions):
            question_lines = []
            line = my_questions_file.readline()

            while line.strip() != "":
                question_lines.append(line)
                line = my_questions_file.readline() # for increment by one line.

            for line in question_lines:
                print(line, end="")

            answer = input("Answer: ").strip().lower()

            while answer not in options_list:
                answer = input("Please choose a valid option from (a/b/c/d).\n")

            if answer == answers_list[corr_ans_index]:
                score += 1

            corr_ans_index += 1

        print(f"Your final score is ({score}/{num_of_qustions}).")

        try_again = input("Do you want to try again? type 'y' for yes or 'n' for no.\n").strip().lower()

        if try_again == 'y':
            quiz_start()

        else:
            print("Quiz closed.")


# Printing the 2-line intro.
with open(r"C:\Users\DELL\OneDrive\Desktop\question_manager\questions.txt","r") as my_questions_file:

    for i in range(2):
        print(my_questions_file.readline(), end="")

    start_quiz = input("Do you want to continue? type 'y' for yes or 'n' for no.\n").strip().lower()

    while start_quiz not in yes_no_list:
        start_quiz = input("You didn't enter a valid option. Please type 'y' for yes or 'n' for no.\n")

    if start_quiz == 'y':
        quiz_start()

    else:
        print("Quiz closed.")