import subprocess
import sys
import time
import wikipedia

# sets language to czech,
# you can find a list of languages
# with wikipedia.languages()
wikipedia.set_lang('cs')

article_cache = {}
options_cache = {}
class Menu:


    def show_menu(self):
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

            try:
                if user_input in article_cache.keys():
                    print(article_cache.get(user_input))

                elif user_input in options_cache.keys():
                    print(f"Článek neexistuje, ale slovo '{user_input}' můžete nalézt v těchto článcích:")
                    for option in options_cache.get(user_input):
                        print(option)
                else:
                    result = self.check_if_article_exists(user_input)

                    if result:
                        article_cache[user_input] = result
                        print(result)
                    # if the article does not exist, it will search for the input
                    # and print a list where the word is found
                    else:
                        article_list = wikipedia.search(user_input)

                        if article_list:
                            options_cache[user_input] = article_list
                            print(f"Článek neexistuje, ale slovo '{user_input}' můžete nalézt v těchto článcích:")
                            for article in article_list:
                                print(article)
                        # if the word is not found at all it will print about it
                        else:
                            print(f"Výraz '{user_input}' nebyl na stránce nalezen.")

            except wikipedia.exceptions.DisambiguationError as de:
                print(f"Článek neexistuje, ale slovo '{user_input}' můžete nalézt v těchto článcích:")
                for i in de.options:
                    print(i)

            except wikipedia.exceptions.WikipediaException:
                print('Chyba! Nezadali jste text.')

            input('Pro pokračování stiskněte Enter')

            self.clear_screen()

    @staticmethod
    def clear_screen():
        """
        Clears CMD window.
        """
        if sys.platform.startswith('win'):
            subprocess.call(['cmd.exe', '/C', 'cls'])
        else:
            subprocess.call(['clear'])

    @staticmethod
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



if __name__ == '__main__':
    menu = Menu()
    menu.show_menu()
