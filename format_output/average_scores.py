'''
Program: AVERAGE_SCORES.py
Author: Joshua M. McGinley
Last date modified: 09/07/2022

Write the manual tests and program average_scores.py to read in one person's names, first and last, their age and three scores out of 100. Take the three scores and find the average, storing into a variable.

    Create a project Module 2, add directories format_output.
    In format folder, make average_scores.py

It's time to write the main in your average_scores.py.

    Prompt the user for what is expected for each input
    Store into local variables last_name, first_name.
    Use a constant to represent the number of scores you will prompt the user to input
    Prompt the user for the scores, storing them in local variable or variables.
        You can keep separate variables for each score, or you keep a running total in one variable.
    Calcuate the average using the variables.
    Print the output, with last name followed by a comma and the first name followed by an integer age and
    then the average scores with 2 decimal places.
        Example output:
        Rodriguez, Linda age: 21 average grade: 92.50
        Add doctring to the top of your file, add comments at the bottom with observed output after a few manual
        test runs of your code.
    Submit your average_scores.py

Note: Be sure to format your output string like the above. If the user is promted and enters John Smith for their
first and last name, 25 for their age, and test scores of 70,80, and 90 your code should output: Smith, John age:
25 average grade: 80.00 And if they entered Jane Doe, 33 and scores of 95, 100, and 105 it should output:
Doe, Jane age: 33 average grade: 100.00
'''

import constants  #Import the module constants.py

#Taking and storing input
first_name = input('What is your first name? ')  #Take input and store it as first_name
last_name = input('What is your last name? ')  #Take input and store it as last_name
age = int(input('What is your age? '))  #Take input and store it as age

score_1 = float(input('Now enter score: '))  #Take input and store as float in score_1
score_2 = float(input('Now enter score: '))  #Take input and store as float in score_2
score_3 = float(input('Now enter score: '))  #Take input and store as float in score_3

#Finding and storing average of three scores#
average_grade = (score_1 + score_2 + score_3) / constants.NUMBER_OF_SCORES  #Add score_1, score_2, score_3, and#
                                                                            #divide by the constant NUMBER_OF_SCORES#
#Printing output to screen#
print(last_name, end='')  #Print last_name to screen append next line
print(',', first_name, 'age: ', end='')  #Print , first_name age: append next line
print(age, 'average grade:', end='')  #Print age average grade: append next line
print(f'{average_grade: 5.2f}')  #Print average_grade formated as decimal totla of five digits with only two digits#
                                 #after the decimal#

##############################################################################################################################################
##Observed output from testing################################################################################################################
##############################################################################################################################################
##What is your first name? Allen               #What is your first name? Jack              #What is your first name? William
##What is your last name? Ginsberg             #What is your last name? Kerouac            #What is your last name? Burroughs
##What is your age? 70                         #What is your age? 47                       #What is your age? 83
##Now enter score: 60                          #Now enter score: 39.2                      #Now enter score: 15
##Now enter score: 70                          #Now enter score: 87.5                      #Now enter score: 30
##Now enter score: 50                          #Now enter score: 222                       #Now enter score: 888
##Ginsberg, Allen age: 70 average grade: 60.00 #Kerouac, Jack age: 47 average grade: 116.23#Burroughs, William age: 83 average grade: 311.00
##############################################################################################################################################
