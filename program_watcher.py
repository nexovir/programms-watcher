import argparse
import os
import requests
import time
import sqlite3
import subprocess
from find_programm.programs_data import *
import colorama
from find_programm.set_sql_targets import set_sql_targets

# Function to send messages, with options for Telegram integration, colored output, and logging
def sendmessage(message: str, telegram: bool = True, colour: str = "YELLOW", logger: bool = True):
    color = getattr(colorama.Fore, colour, colorama.Fore.YELLOW)
    print(color + message + colorama.Style.RESET_ALL)
    named_tuple = time.localtime()
    time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
    
    if logger:
        with open('logger.txt', 'a') as file:
            file.write(f"{message} -> {time_string}\n")
    
    if telegram:
        message = message.replace(' ', '+')
        command = f'curl -X POST "https://api.telegram.org/bot<your_bot_token>/sendMessage" -d "chat_id=<your_chat_id>&text={message}"'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()

# Function to clean the specified file
def file_cleaner(filename: str):
    clean_file = input(f"{colorama.Fore.YELLOW}Do you want to clean {colorama.Fore.RED}{filename}{colorama.Fore.YELLOW}? (yes/no): ").strip().lower()
    
    if clean_file in ['yes', 'y']:
        with open(filename, 'w') as f:
            f.truncate(0)
        sendmessage(f"File {filename} has been cleaned.", telegram=False, logger=True)
    
    elif clean_file in ['no', 'n']:
        sendmessage(f"No changes made to {filename}", telegram=False, logger=True)
    
    else:
        sendmessage("Invalid input. No changes made.", telegram=False, logger=True, colour="RED")

# Parse command-line arguments
parser = argparse.ArgumentParser(description='A powerful watcher for bug bounty programs')
parser.add_argument('-ts', '--sendtelegram', help='Enable sending Telegram bot messages?', metavar="", default=0, required=True)
parser.add_argument('-t', '--time', help='Time interval for checking new programs (default: 6 hours)', metavar="", default=6, required=False)

args = parser.parse_args()

update_time = args.time
telegram_send = args.sendtelegram

# Function to update the database and send notifications
def update_data_base():
    sendmessage('Getting new targets, please wait...')
    
    check_in_scope('hackerone_json_url', 2)
    time.sleep(3)
    check_in_scope('bugcrowd_json_url', 1)   
    time.sleep(3)
    check_in_scope('federacy_json_url', 3)
    time.sleep(3)
    check_in_scope('intigriti_json_url', 5)
    time.sleep(3)
    check_in_scope('yeswehack_json_url', 6)        
    
    sendmessage('New targets fetched successfully.')
    time.sleep(2)
    sendmessage('Looking for new targets, please wait...')
    
    new_scopes = checking()

    for scope in new_scopes:
        sendmessage(scope, telegram=(telegram_send in ['yes', 'y']))
        time.sleep(1)

    sendmessage("Target check completed.")

    if len(new_scopes) > 0:
        sendmessage("Deleting old database. Please wait...") 
        try:
            deleting_tables()
        except sqlite3.Error as e:
            sendmessage(f"Could not delete database: {e}")
        
        time.sleep(1)
        sendmessage("Creating database. Please wait...")
        try:
            creating_tables()
            hackerone_create_tables('hackerone_json_url')
            sendmessage("HackerOne updated.")
            
            burgcrowd_create_tables('bugcrowd_json_url')
            sendmessage("Bugcrowd updated.")
            
            federacy_create_tables('federacy_json_url')
            sendmessage("Federacy updated.")
            
            intigriti_create_tables('intigriti_json_url')
            sendmessage("Intigriti updated.")
            
            yeswehack_create_tables('yeswehack_json_url')
            sendmessage("YesWeHack updated.")
        
        except sqlite3.Error as e:
            sendmessage(f"Could not create table: {e}")
    else:
        sendmessage("No changes in the database.")

    sendmessage(f"DATABASE UPDATED SUCCESSFULLY at {time.strftime('%m/%d/%Y, %H:%M:%S', time.localtime())}")

# Clean logger file and start the watcher
file_cleaner('logger.txt')
sendmessage(f"Started watching for new programs. Update time: {update_time} hours, Telegram send: {telegram_send}", telegram=True)
update_data_base()

# Define the job for scheduled updates
def job():
    update_data_base()
    set_sql_targets()

# Schedule the update job
schedule.every(int(update_time)).hours.do(job)

# Continuous loop for scheduling
while True:
    schedule.run_pending()
    time.sleep(1)
