import os
import time
import webbrowser

from data import Data


def menu():
    while True:
        try:
            menu_decision = int(input("\nWhat do you want to do?\n"
                                      "[1] Check Covid-19 data in your location (country)\n"
                                      "[2] Check Covid-19 data in another country\n"
                                      "[3] Read how to protect Yourself and Others\n"
                                      "[4] Exit\n\n"
                                      "Decision: "))
        except ValueError:
            print("\n--error-- WRONG VALUE\n")
            continue

        if menu_decision == 1 or menu_decision == 2:
            print("Please wait..")
            data = Data()
            cases = data.get_data(menu_decision)
            try:
                data.show_cases(cases)
            except TypeError:
                print('--error-- invalid country name')


        elif menu_decision == 3:
            webbrowser.open(os.path.realpath('recommendations.html'))

        elif menu_decision == 4:
            print("Goodbye")
            time.sleep(2)
            break

        else:
            print("\n--error-- choose between [1], [2], [3], [4]\n")


menu()
