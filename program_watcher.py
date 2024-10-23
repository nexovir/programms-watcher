import argparse
import os
from typing import Final
import requests
import time
import sqlite3
import time
import subprocess
from find_programm.programs_data import *
import colorama
import time

from find_programm.set_sql_targets import set_sql_targets



def sendmessage (message : str , telegram : bool = True, colour : str = "YELLOW" , logger : bool = True):
    
    color = getattr(colorama.Fore, colour, colorama.Fore.YELLOW)
    print(color + message + colorama.Style.RESET_ALL)
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
    if logger == True :
        with open ('logger.txt' , 'a') as file :
            file.write (message+' -> '+ time_string+'\n')
    if telegram == True :
        message = message.replace(' ','+')
        command = f'curl -X POST "https://api.telegram.org/bot6348870305:AAHawStCiN6XfiAu_ZwQJU-x8C1XtKjZ2XA/sendMessage" -d "chat_id=5028701156&text={message}"'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()  
         
def file_cleaner(filename:str):

    clean_file = input(f"{colorama.Fore.YELLOW}Do you want to clean {colorama.Fore.RED}{filename}{colorama.Fore.YELLOW}? (yes/no): ").strip().lower()

    if clean_file == 'yes' or clean_file == 'y':

        with open(f'{filename}', 'w') as f:
            f.truncate(0)  

        sendmessage(f"file {filename} has been cleaned." , telegram=False , logger=True)

    elif clean_file == 'no' or clean_file == 'n':

        sendmessage(f"No changes made at {filename}" , telegram=False , logger=True)
            
    else:
        sendmessage("Invalid input. No changes made." , telegram=False , logger=True , colour="RED")


parser = argparse.ArgumentParser(description='a powerfull watcher for bug bouty programms')

parser.add_argument('-ts', '--sendtelegram', help='want to send telegram bot ? ',metavar="" , default= 0 , required=True)
parser.add_argument('-t', '--time', help='time for checking new programms defult : 6',metavar="" , default= 6 , required=False)

args = parser.parse_args()

update_time = args.time
telegram_send = args.sendtelegram

def update_data_base() :
    sendmessage('Getting new targets please wait ...')
    check_in_scope('hackerone_json_url',2)
    time.sleep(3)
    check_in_scope('bugcrowd_json_url',1)   
    time.sleep(3)
    check_in_scope('federacy_json_url',3)
    time.sleep(3)
    check_in_scope('intigriti_json_url',5)
    time.sleep(3)
    check_in_scope('yeswehack_json_url',6)        

    sendmessage('Getting new targets was seccussfully done')
    time.sleep(2)
    sendmessage('Looking for new targets please wait ...')

    new_scopes =checking()

    for k in range(len(new_scopes)):
        if (telegram_send == 'yes' or telegram_send =='y'):
            sendmessage(new_scopes[k] , telegram=True)
        else :
            sendmessage(new_scopes[k] , telegram=False)
        time.sleep(1)

    sendmessage("Checking new targets was successfully done")

    if bool(len(new_scopes) == 0) is False:
    
        sendmessage("Delete Old Data Base Please wait ...") 
        try :
            deleting_tables()
        except sqlite3.Error as e:
            sendmessage(f"I cant Delete Data Base Because {e}")
            
        time.sleep(1)
        sendmessage("Creating DataBase Please wait ...") 
        try:
            creating_tables()
        
        except sqlite3.Error as e:
            sendmessage(f"I cant Create Data Base Because {e}")

        sendmessage("Create Database Was successfully done")
        sendmessage("Now I going to Updating All Programms Please Wait...")
        
        try:       

            hackerone_create_tables('hackerone_json_url')
            
            sendmessage("UPDATING hackerone is done ...")
                    
            burgcrowd_create_tables('bugcrowd_json_url')
                
            sendmessage("UPDATING burgcrowd is done ...")
            
            federacy_create_tables('federacy_json_url')
                
            sendmessage("UPDATING federacyacy is done ...")
                    
            # hackenproof_create_tables('hackenproof_json_url')
            
            # sendmessage("UPDATING  hackenproof is done ...")
            
            intigriti_create_tables('intigriti_json_url')
            
            sendmessage("UPDATING intigriti is done ...")
        
            yeswehack_create_tables('yeswehack_json_url')
        
            sendmessage("UPDATING yeswehack is done ...")


        except sqlite3.Error as e:
            sendmessage(f"I cant Create table Because {e}")
        
    else :
      sendmessage("No Changes in Data Base :)")

    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)



    sendmessage(f"DATABASE UPDATED SUCCESSFULLY at ({time_string})")

file_cleaner('logger.txt')

sendmessage (f"You Start Watching for New Programms , update_time : {update_time} , telegram_send : {telegram_send}" , telegram=True)
update_data_base()


def job():
    update_data_base()
    set_sql_targets()



schedule.every(int(update_time)).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
   
    
    
    
    
    
    
    
    
    
