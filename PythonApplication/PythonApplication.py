#Experiments With Python - Maths Quiz#
#Adam Stanton#

from Question import Question

exitCondition = False
totalQuestions = 10
questionsRemaining = totalQuestions - 1
questionsCorrect = 0

q = Question

print("Welcome to this simple Python maths quiz! Please answer the following questions!\n")

while exitCondition == False:
    
    q.RefreshQuestion()
    
    userInput = Question.TryInput()

    if userInput == q.solution:
        questionsCorrect += 1
        print("Correct! " + str(questionsRemaining) + " questions left!")
    else:
        print("Incorrect! " + str(questionsRemaining) + " questions left!")

    if questionsRemaining > 0:
        questionsRemaining -= 1
    else:
        exitCondition = True

print("\nThanks For Playing! You Answered " + str(questionsCorrect) + " out of " + str(totalQuestions) + " Correctly!")

