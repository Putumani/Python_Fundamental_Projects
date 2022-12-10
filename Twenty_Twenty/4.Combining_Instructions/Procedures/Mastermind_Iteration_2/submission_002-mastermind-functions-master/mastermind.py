import random

code = [0,0,0,0] 
correct_digits_and_position = 0
correct_digits_only = 0
correct = False
turns = 0
answer = 0

def create_code():
    global code
    code = [0,0,0,0] 
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value

    #print(code)
def print_instructions():

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')

def get_user_input():
    global answer
    global correct
    global turns
    global correct_digits_and_position
    global correct_digits_only
    
    
    answer = input("Input 4 digit code: ")
    if len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")
        

    correct_digits_and_position = 0
    correct_digits_only = 0

    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
        

def show_results():
    global correct_digits_and_position
    global correct_digits_only
    global turns
    
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
    turns += 1

    
    
def take_turns():

    global correct_digits_and_position
    global correct
    global turns
    
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: '+str(12 - turns))

def show_code():

    print('The code was: '+str(code))

def run_game():

    global correct
    correct = False
    create_code()
    print_instructions()
    
    while not correct and turns < 12:
        get_user_input()
        show_results()
        take_turns()   
    show_code()


if __name__ == "__main__":
    run_game()
