# Quiz App
# A command-line quiz app built with Python that tests your general knowledge
# with randomised questions and instant feedback.
# Built with Python | Question stored in questions.json
import random
import json
import os
FILENAME = "questions.json"
# Load questions from JSON file
def load_questions():
    """ # Load questions from JSON file, return empty list if file doesn't exist"""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        return json.load(f)

#Displays the question and user can attend the quiz
def ask_question(question):
    """
    The user can start the quiz.The question will be displayed with options
    The user can select from the list.If correct then the score adds up accordingly
    for wrong answer the correct answer will be displayed
    """
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)
    try:
        user_answer = int(input("Enter your option number (1-4): "))
    except ValueError:
        print("Invalid input, skipping question.")
        return False
    if user_answer == question["answer"]:
        print("Correct! ✓")
        return True
    else:
        option_no = question['answer']
        correct = question["options"][option_no - 1]
        print(f"Wrong! Correct answer was {correct}")
        return False
#loads the question and asks the question
def main():
    """
    Loads the questions and user can take up the quiz
    asks the user if they want to quiz.
    """
    questions = load_questions()
    score = 0
    random.shuffle(questions)
    for question in questions:
        if ask_question(question):
          score += 1
    print(f"\nQuiz Over! You scored {score} out of {len(questions)}!")
    next_chance = input("Would you like to play again? (yes/no): ")
    if next_chance.lower() == "yes":
        main()
    else:
        print("Thank you for playing!")

main()