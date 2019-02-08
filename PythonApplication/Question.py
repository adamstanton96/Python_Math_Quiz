import random

class Question(object):
    """Definition of a simple mathematical formula"""

    value_1 = 0     #First value of formula
    value_2 = 0     #Second value of formula
    solution = 0    #Solution to formula
    operator = ""   #Symbol of active operator

    #//Constructor//#
    def __init__(self):
        RefreshQuestion()

    #//Generates a new question//#
    def RefreshQuestion():

        Question.value_1 = random.randint(0,101)        #Randomly generates first value
        Question.value_2 = random.randint(0,101)        #Randomly generates second value
        value_operator = random.randint(0,2)   #Defines operator used randomly

        if value_operator == 0:
            Question.operator = "+"
            Question.solution = Question.value_1 + Question.value_2
        elif value_operator == 1:
            Question.operator = "-"
            Question.solution = Question.value_1 - Question.value_2
        elif value_operator == 2:
            Question.operator = "*"
            Question.solution = Question.value_1 * Question.value_2

    #//Returns a valid integer input by the user using recursive exception handling//#
    def TryInput():
        try:
            userInput = int(input(Question.ToString()))
        except ValueError:
            print('You did not enter a valid integer as your answer. Please try again')
            userInput = Question.TryInput()
        return userInput

    #//Returns The Question In Readable Format//#
    def ToString():
        return str(Question.value_1) + " " + Question.operator + " " + str(Question.value_2) + " = "
        