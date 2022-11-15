import subprocess
import sys
import time

import wikipedia

# sets language to czech,
# you can find a list of languages
# with wikipedia.languages()
wikipedia.set_lang('cs')


def clear_screen():
    """
    Clears CMD window.
    """
    if sys.platform.startswith('win'):
        subprocess.call(['cmd.exe', '/C', 'cls'])
    else:
        subprocess.call(['clear'])


def check_if_article_exists(user_input: str):
    """
    Takes in the user input and checks if the article exists.
    :param user_input: str:
    :return: article text: str
    """
    search = wikipedia.search(user_input)
    for i in search:
        if i.lower() == user_input.lower():
            article = wikipedia.summary(user_input.lower())
            return article


def menu():
    """
    Runs the whole app in a while loop
    unless you stop it.
    """
    while True:
        user_input = input('Zadejte název článku (nebo napište ukončit pro ukončení): ')
        if user_input == 'ukončit':
            print('Aplikace se teď ukončí!')
            # sleeps for 1 second before shutdown
            time.sleep(1)
            break

        result = check_if_article_exists(user_input)

        if result:
            print(result)
        # if the article does not exist, it will search for the input
        # and print a list where the word is found
        else:
            article_list = wikipedia.search(user_input)

            if article_list:
                print(f"Článek neexistuje, ale slovo '{user_input}' můžete nalézt v těchto článcích:")
                for i in article_list:
                    print(i)
            # if the word is not found at all it will print about it
            else:
                print(f"Výraz '{user_input}' nebyl na stránce nalezen.")
        input('Pro pokračování stiskněte Enter')
        clear_screen()


if __name__ == '__main__':
    menu()
