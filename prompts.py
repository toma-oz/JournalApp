import sys
import os
import time
from datetime import date

class LogIn:

    @classmethod
    def landing(self):
        os.system('clear')
        print('========')
        print('Log In')
        print('========')
        return input('USERNAME: ')
    
    @classmethod
    def new_account(self):
        os.system('clear')
        print('=======================================================================================')
        print('Username is not registered. Would you like to create a new account, try again, or exit?')
        print('=======================================================================================')        
        print('[1] Create account ')
        print('[2] Try again ')
        print('[3] Exit ')
        return input('Enter option: ')

    @classmethod
    def create_account(self):
        os.system('clear')        
        print('==============')
        print('Create account ')
        print('==============')        
        user = input('Username: ')
        password = input('Password: ')
        os.system('clear')
        print('Account created! 🍰 🎉')
        time.sleep(1)
        return user, password
    
    @classmethod
    def wrong_password(self):
        os.system('clear')        
        print('================================================')
        print('Password incorrect. Would you like to try again?')
        print('================================================')        
        print('[y] ')
        print('[n] ')
        return input('Enter option: ')

    @classmethod
    def existing_account(self):
        return input('Password: ')

class General:

    @classmethod
    def welcome_message(self):
        os.system('clear')
        print('=====================')
        print('Welcome to JournalApp')
        print('=====================')
        print('[1] Log in ')
        print('[2] Exit ')
        option = input('Enter option: ')
        
        return option

    @classmethod
    def exit(self):
            os.system('clear')
            print('Goodbye :) 🍪')
            time.sleep(.7)
            os.system('clear')
            print('Goodbye :) 🍪🍪')
            time.sleep(.7)
            os.system('clear')
            print('Goodbye :) 🍪🍪🍪')
            time.sleep(.7)
            os.system('clear')
            sys.exit()

class Menu():

    @classmethod
    def new_user(self):
        os.system('clear')        
        print('=========================')
        print('Welcome to JournalApp :))')
        print('=========================')        
        print('[1] Create new entry')
        print('[2] Exit')
        user_input = input('Enter option: ')
        if user_input == '2':
            General.exit()
    
    @classmethod
    def user(self):
        os.system('clear')        
        print('=========================')
        print('Welcome to JournalApp :))')
        print('=========================')        
        print('[1] Create new entry')
        print('[2] View old entries')
        print('[3] Exit')
        user_input = input('Enter option: ')
        if user_input == '3':
            General.exit()

        return user_input

class Logs:

    @classmethod
    def new_log(self):
        os.system('clear')
        print(f'{date.today()} Log (ctrl d to finish)')
        print()
        print()
        contents = []
        while True:
            try:
                line = input()
            except (EOFError, KeyboardInterrupt):
                os.system('clear')
                journal_name = input('Journal name: ')
                break
            contents.append(line)
        return contents, journal_name

    @classmethod
    def view_logs(self, logs):
    
        logslist = logs
        os.system('clear')        
        print('==============')
        print('View your logs')
        print('==============')        
        for log in logslist:
            print(f'[{logslist.index(log) + 1}] {log}')
        print(f'[{logslist.index(logslist[-1]) + 2}] Back')
        option = input('Enter option: ')
        os.system('clear')
        return option
