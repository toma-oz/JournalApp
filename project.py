from prompts import *
import database
from datetime import date
import csv
import sys
import os
import time


def main():
    
    while True:

        # Load welcome page
        response = General.welcome_message()
        if response == '2':
            General.exit()
            
        # Check if username is in users.csv; if not, call create_account()
        user_name = validate_username()
        if user_name == False:
            if create_account():
                continue
        
        # Check if password matches username; if not, load wrong password screen
        if not validate_password(user_name):
            if LogIn.wrong_password() == 'n':
                General.exit()
            else:
                continue
        
        else:
            break
        
    # Check for user folder and previous logs; if logs exist, grab a list of them
    is_existing_user = database.check_directory(user_name)
    logs_present = database.check_logs(user_name)
    if logs_present:
        logs = database.get_logs(user_name)
        

    while True:
        
        # If new user or no previous logs, do not show view previous logs button
        if not is_existing_user or logs_present == 1:
            Menu.new_user()
            create_log(user_name)
            
        # If previous logs exist, load normal user menu and parse response
        option = Menu.user()
        if option == '1':
            create_log(user_name)
        elif option == '2':
            view_log(user_name)


def validate_username():

    # Load username prompt
    username = LogIn.landing()

    # Check that username is in users.csv
    with open('users.csv') as database:
        content = csv.DictReader(database)
        try:
            for row in content:
                if username == row['name']:
                    return username
        except IndexError:
            return False
        return False

    
def validate_password(name):
    
    # Load password prompt
    password = LogIn.existing_account()

    # Check that password matches current user name
    with open('users.csv') as database:
        content = csv.DictReader(database)
        for row in content:
            if name == row['name'] and password == row['password']:
                return True
        return False


def create_account():
    
    # Load unrecognized username page
    option = LogIn.new_account()


    # Exit if '3', continue loop if '2', call create_account if '1' and store name,password in csv
    if option == '3':
        General.exit()
    elif option == '2':
        return True
        
    elif option == '1':
        username, password = LogIn.create_account()
        mylist = [username, password]
        with open('users.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(mylist)

        return True


def create_log(name):

    # Create new log
    contents, journal_name = Logs.new_log()
    
    # Create log txt file with name in the format: customname_date.txt
    with open(f'logs/{name}/{journal_name}_{date.today()}.txt', "w") as user_journal:
            for line in contents:
                user_journal.write(f'{line}\n')
                
    os.system('clear')
    print('Journal Created! 🍰 🥳')

def view_log(name):

    # Grab list of previous logs
    loglist = database.get_logs(name)

    # Show view logs menu and open log with name associated to number in prompt
    option = Logs.view_logs(loglist)
    try:
        with open(f'logs/{name}/{loglist[int(option) - 1]}') as journal:
            for line in journal:
                print(line)

        print('(ctrl-c to resume.)')
        try:
            time.sleep(10000000)
        except (EOFError, KeyboardInterrupt):
            pass

    except IndexError:
        return False





if __name__ == '__main__':
    main()