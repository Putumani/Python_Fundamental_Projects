import random


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index]
    return word


def select_random_letter_from(word):
    random_index = random.randint(0, len(word) - 1)
    letter = word[random_index]
    print('Guess the word: ' + word[:random_index] + "_" + word[random_index+1:])
    return letter, random_index


def get_user_input():

    letter_input = input('Guess the missing letter: ')
    return letter_input


def show_answer(answer, selected_word, missing_letter_index):
    """
    TODO Step 1 - Show better results messages
    """
    print("The word was: " + selected_word)
    if answer in selected_word:
        print ("Well done! You are awesome!")
    else : 
        print ("Wrong! Do better next time.")
    pass


# TODO: Step 2
def ask_file_name():
    """
    TODO Step 2 - Update to prompt user for filename to use for words
    """
    
    input_ = input("Words file? [leave empty to use short_words.txt] :")
    if input_ == "hello.txt":
        return "hello.txt"
    else:
        return "short_words.txt" 


def run_game(file_name):
    """
    You can leave this code as is, and only implemented above where the code comments prompt you.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    missing_letter, letter_index = select_random_letter_from(word)
    answer = get_user_input()
    show_answer(answer, word, letter_index)


if __name__ == "__main__":
    words_file = ask_file_name()
    run_game(words_file)

