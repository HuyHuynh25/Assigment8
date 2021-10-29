########################################################################
 ##
 ## CS 101 Lab
 ## Program 8
 ## Name: Huynh Gia Huy-Jim Huynh
 ## Email: hghydv@umsystem.edu
 ##
 ## PROBLEM : Create write a program to allow the user to enter 2 types of grades;
 ## Tests and Programs.  Each of our scores is assumed to be out of 100, so we only need the users score.
 ## In order to calculate the final score, we multiply the mean score of the tests by 0.6 and add it to
 ## the mean of assignments multiplied by 0.4.
 ## ALGORITHM :
 ##      Step 1: Start
 ##      Step 2: import math and time
 ##      Step 3: Define function menu()
 ##      Step 4: Define function mean(n)
 ##      Step 5: Define function standard_dev(m,n)
 ##      Step 6: Define function display(test,assignment)
 ##      Step 7: Call function get_output_file(minimum_mpg, file_data)
 ##      Step 10: Make a loop if it's True
 ##      Step 11: Call function menu()
 ##      Step 12: Make an if function if user_input equal '1-6' and 'D' and 'Q'
 ##      Step 13: If the loop is False make user type input again.
 ##      Step 14: End
 ##ERROR HANDLING:
 ##      N/A
 ##
 ## OTHER COMMENTS:
 ##      Any special comments
 ##
 ########################################################################
import math
import time
def menu():
    print()
    print('{:^50}'.format('Grade Menu'))
    print('1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Tests')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Q - Quit')
def mean(n):
    sum = 0
    for i in n:
        sum += i
    mean = sum / len(n)
    return mean
def standard_dev(m,n):
    sum = 0
    for i in n:
        sum += (i - m) ** 2
    stan = math.sqrt((sum/len(n)))
    return stan
def display(test,assignment):
    print('{:<20}{:<8}{:<8}{:<8}{:<8}{}'.format('Type', '#', 'min', 'max', 'avg', 'std'))
    print('=' * 55)
    num_test = len(test)
    num_assignment = len(assignment)
    test_weight = 0
    assignment_weight = 0
    if num_test == 0:
        print()
        print('{:<20}{:<8}{:<8}{:<8}{:<8}{}'.format('Tests','0','n/a','n/a','n/a','n/a'))
    else:
        min_test = min(test)
        max_test = max(test)
        test_mean = mean(test)
        test_stan = standard_dev(test_mean, test)
        test_weight += test_mean * 0.6
        print('{:<20}{:<8}{:<8}{:<8}{:<8.2f}{:.2f}'.format('Tests',num_test, min_test, max_test,test_mean, test_stan))
    if num_assignment == 0:
        print('{:<20}{:<8}{:<8}{:<8}{:<8}{}'.format('Programs','0','n/a','n/a','n/a','n/a'))
    else:
        min_assignment = min(assignment)
        max_assignment = max(assignment)
        assignment_mean = mean(assignment)
        assignment_stan = standard_dev(assignment_mean, assignment)
        assignment_weight += assignment_mean * 0.4
        print('{:<20}{:<8}{:<8}{:<8}{:<8.2f}{:.2f}'.format('Programs', num_assignment, min_assignment, max_assignment,
                                                           assignment_mean, assignment_stan))
        print('The weighted score is {:.2f}'.format(assignment_weight + test_weight))
if __name__ == "__main__":
    test = []
    assignment = []
    while True:
        menu()
        print()
        time.sleep(1.5)
        user_input = str(input('==> '))
        if user_input == '1':
            score = float(input("Enter the new Test score 0-100 ==> "))
            while score < 0:
                score = float(input("Enter the new Test score 0-100 ==> "))
            test.append(score)
        elif user_input == '2':
            score = float(input("Enter the Test to remove 0-100 ==> "))
            score_remove = False
            for i in test:
                if i == score:
                    test.remove(score)
                    score_remove = True
            if score_remove == False:
                print('Could not find that score to remove')
        elif user_input == '3':
            print('Clearing')
            time.sleep(1)
            print('........')
            test.clear()
            time.sleep(1)
            print('Tests was cleared')
        elif user_input == '4':
            score = float(input("Enter the new Assignment score 0-100 ==> "))
            while score < 0:
                score = float(input("Enter the new Assignment score 0-100 ==> "))
            assignment.append(score)
        elif user_input == '5':
            score = float(input("Enter the Assignment to remove 0-100 ==> "))
            score_remove = False
            for i in assignment:
                if i == score:
                    assignment.remove(score)
                    score_remove = True
            if score_remove == False:
                print('Could not find that score to remove')
        elif user_input == '6':
            print('Clearing')
            time.sleep(1)
            print('........')
            assignment.clear()
            time.sleep(1)
            print('Assignments was cleared')
        elif user_input == 'd' or user_input == 'D':
            display(test, assignment)
        elif user_input == 'q' or user_input == 'Q':
            print('Have a nice day!!')
            break
        else:
            print('The input you entered was invalid')