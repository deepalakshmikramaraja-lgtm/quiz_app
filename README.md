# Quiz App

A command-line quiz application built with Python.

## Features
- Multiple choice questions with 4 options each
- Questions shuffled randomly every round
- Instant correct/wrong feedback after each answer
- Shows the correct answer when you get it wrong
- Final score displayed at the end
- Play again option without restarting the program
- Questions stored separately in a JSON file — easy to add more!

## How to Run
python quiz_app.py

## How to Add More Questions
Open questions.json and add a new entry following this format:
{
    "question": "Your question here?",
    "options": ["1. Option A", "2. Option B", "3. Option C", "4. Option D"],
    "answer": 1
}

## What I Learned
- Learned how to use random.shuffle() to randomise a list and how the order changes every time the program runs
- Understood how return True/False from a function lets other parts of the code make decisions based on the result
- Learned how to store structured data like quiz questions in a JSON file and load them into Python at runtime
- Practised accessing nested data — getting a specific option using options[answer - 1] from inside a dict
- Built a complete quiz game loop with score tracking and a play again option using only core Python concepts

## Built With
- Python 3
- JSON for storing questions
- random module for shuffling 
