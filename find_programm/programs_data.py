import sqlite3
import json
import urllib.request
import colorama 
import requests
import time
import asyncio
import array
import requests
import json
import colorama
import schedule
from requests.exceptions import RequestException
from http.client import RemoteDisconnected
#programs json files 
import sqlite3
programs = {
'bugcrowd_json_url' : 'https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/bugcrowd_data.json',
'hackerone_json_url' : 'https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/hackerone_data.json',
'federacy_json_url' : 'https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/federacy_data.json',
'hackenproof_json_url' : 'https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/hackenproof_data.json',
'intigriti_json_url' : 'https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/intigriti_data.json',
'yeswehack_json_url':'https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/yeswehack_data.json'
}

#create DTABASEx

programs_db = sqlite3.connect('../../programs.db')
cursor = programs_db.cursor()

all_targets = []
all_targets_res =[]
def check_in_scope (url : str , platform_num):
    urlib = request(programs[url])
    
    if platform_num == 1:   
        
        for i in range(len(urlib)) :
         targets= urlib[i]["targets"] 
         name = urlib[i]["name"]
         bounty = urlib[i]["max_payout"]
         platform = 'bugcrowd'
         if bounty != None:
          if bounty > 0 :   
            if platform != None :    
             if platform == 'bugcrowd':        
              for j in range(len(targets['in_scope'])):
                 if (targets['in_scope'][j]['type'] == 'other' or  targets['in_scope'][j]['type'] == 'website'):#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):     
                    all_targets.append(targets['in_scope'][j]["target"])
                    all_targets_res.append(str(urlib[i]["url"]+' -> '+urlib[i]["targets"]["in_scope"][j]["target"]))
                        #  all_targets.append(urlib[i]["targets"]["in_scope"][j]["target"])
        print(colorama.Fore.GREEN + f"  * Getting Data from {platform} was seccussfully done."+colorama.Style.RESET_ALL)
        time.sleep(2)
       
      #  urlib[i]['offers_bounties'] == True and urlib[i]['submission_state'] == 'open' :
       #         targets_create_table(urlib[i]["name"]  , 1, urlib[i]["targets"] , 'hackerone')
        
    if platform_num == 2:   
        
        for i in range(len(urlib)) :
            
            targets= urlib[i]["targets"] 
            name = urlib[i]["name"]
            platform = 'hackerone'
            
            if urlib[i]['offers_bounties'] == True and urlib[i]['submission_state'] == 'open' :     
                
                if platform == 'hackerone':      
                      
                 for j in range(len(targets['in_scope'])):
                     
                   if targets['in_scope'][j]['asset_type'] == 'URL' or targets['in_scope'][j]['asset_type']== 'WILDCARD' or targets['in_scope'][j]['asset_type'] == 'OTHER' or targets['in_scope'][j]['asset_type'] == 'CIDR':
                       
                     #all_targets.append()
                     all_targets.append(urlib[i]["targets"]["in_scope"][j]["asset_identifier"])
                     all_targets_res.append(str(urlib[i]["url"]+' -> '+urlib[i]["targets"]["in_scope"][j]["asset_identifier"]))
                        #all_targets.append(urlib[i]["targets"]["in_scope"][j]["target"])
        print(colorama.Fore.GREEN + f"  * Getting Data from {platform} was seccussfully done."+colorama.Style.RESET_ALL)       
        time.sleep(2)
     
                            #  all_targets.append(urlib[i]["targets"]["in_scope"][j]["target"])
                            
    
    if platform_num == 3:   
        
        for i in range(len(urlib)) :
         targets= urlib[i]["targets"] 
         name = urlib[i]["name"]
         platform = 'federacy'
         if urlib[i]['offers_awards'] == True:  
                
             if platform == 'federacy':    
                     
              for j in range(len(targets['in_scope'])):
        
                 if (targets['in_scope'][j]['type'] == 'other' or  targets['in_scope'][j]['type'] == 'website' or  targets['in_scope'][j]['type'] == 'api'):#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):
                    
                    all_targets.append(urlib[i]["targets"]["in_scope"][j]["target"])
                    all_targets_res.append(str(urlib[i]["url"]+' -> '+urlib[i]["targets"]["in_scope"][j]["target"]))
        print(colorama.Fore.GREEN + f"  * Getting Data from {platform} was seccussfully done."+colorama.Style.RESET_ALL)       
        time.sleep(2)


    if platform_num == 4:   
                
        for i in range(len(urlib)) :
         targets= urlib[i]["targets"] 
         name = urlib[i]["name"]
         platform = 'hackenproof'    
         
         if platform == 'hackenproof':           
              for j in range(len(targets['in_scope'])):
                
                    if targets['in_scope'][j]['type'] == 'Web' and targets['in_scope'][j]['reward'] == 'Bounty':#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):
                   
                        all_targets.append(urlib[i]["targets"]["in_scope"][j]["target"])

                        all_targets_res.append(str(urlib[i]["url"]+' -> '+urlib[i]["targets"]["in_scope"][j]["target"]))
        print(colorama.Fore.GREEN + f"  * Getting Data from {platform} was seccussfully done."+colorama.Style.RESET_ALL)       
        time.sleep(2)
               
 
    if platform_num == 5:   
                
        for i in range(len(urlib)) :
         targets= urlib[i]["targets"] 
         name = urlib[i]["name"]
         platform = 'intigriti'   
             
         if urlib[i]['status'] == 'open' and urlib[i]['min_bounty']['value']>0: 
                       
            for j in range(len(targets['in_scope'])):
                
                if (targets['in_scope'][j]['type'] == 'url' or targets['in_scope'][j]['type'] == 'wildcard'):#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):

                    all_targets.append(urlib[i]["targets"]["in_scope"][j]["endpoint"])

                    all_targets_res.append(str(urlib[i]["url"]+' -> '+urlib[i]["targets"]["in_scope"][j]["endpoint"]))
        print(colorama.Fore.GREEN + f"  * Getting Data from {platform} was seccussfully done."+colorama.Style.RESET_ALL)       
        time.sleep(2)
                      
 
 
    if platform_num == 6:   
                
        for i in range(len(urlib)) :
         targets= urlib[i]["targets"] 
         name = urlib[i]["name"]
         platform = 'yeswehack' 
           
         if urlib[i]['min_bounty'] is not None:
    
            if urlib[i]['disabled'] == False and urlib[i]['min_bounty']>0:
                        
                for j in range(len(targets['in_scope'])):
                    
                    if (targets['in_scope'][j]['type'] == 'web-application' or targets['in_scope'][j]['type'] == 'other' or targets['in_scope'][j]['type'] == 'api'):
                        
                        all_targets.append(urlib[i]["targets"]["in_scope"][j]["target"])
                        all_targets_res.append(str("https://yeswehack.com/"+urlib[i]["name"]+' -> '+urlib[i]["targets"]["in_scope"][j]["target"]))

        print(colorama.Fore.GREEN + f"  * Getting Data from {platform} was seccussfully done."+colorama.Style.RESET_ALL)       
        time.sleep(2)
  
               
        
        
def checking():
    
    add_scope = []
    
    for k in range(len(all_targets)):
        
        x = programs_db.execute("SELECT * FROM TARGETS WHERE targets=?", (all_targets[k],))
        if x.fetchone():
            print(all_targets[k] + colorama.Fore.RED+'-> [exists in database]'+colorama.Style.RESET_ALL)
        else:
            add_scope.append(all_targets_res[k])   
            print(all_targets[k] + colorama.Fore.GREEN+'-> [NEW SCOPE ADDED]'+colorama.Style.RESET_ALL)         

    return add_scope                     
            
        

def deleting_tables():
        cursor.execute('''DROP TABLE IF EXISTS YESWEHACK''')
        cursor.execute('''DROP TABLE IF EXISTS BUGCROWD''')
        cursor.execute('''DROP TABLE IF EXISTS HACKERONE''')
        cursor.execute('''DROP TABLE IF EXISTS FEDERACY''')
        cursor.execute('''DROP TABLE IF EXISTS HACKENPROOF''')
        cursor.execute('''DROP TABLE IF EXISTS INTIGRITI''')
        cursor.execute('''DROP TABLE IF EXISTS YESWEHACK''')


    #create TABLES
def creating_tables():
        cursor.execute('''CREATE TABLE IF NOT EXISTS TARGETS
            (id INTEGER PRIMARY KEY UNIQUE, name TEXT , bounty TEXT , targets TEXT , platform TEXT)''')
            
        cursor.execute('''CREATE TABLE IF NOT EXISTS OUT_OF_SCOPE
            (id INTEGER PRIMARY KEY UNIQUE, name TEXT , bounty TEXT  , targets TEXT , platform TEXT)''')
            
        cursor.execute('''CREATE TABLE IF NOT EXISTS BUGCROWD
            (id INTEGER PRIMARY KEY UNIQUE, name TEXT, url TEXT, allows_disclosure TEXT 
            , managed_by_bugcrowd TEXT , safe_harbor TEXT , targets TEXT, max_payout INTEGER )''')
            
        cursor.execute('''CREATE TABLE IF NOT EXISTS HACKERONE
            (id INTEGER PRIMARY KEY UNIQUE, allows_bounty_splitting TEXT, average_time_to_bounty_awarded INTEGER, average_time_to_first_program_response INTEGER 
            , average_time_to_report_resolved INTEGER , handle TEXT , managed_program TEXT , name TEXT , offers_bounties TEXT , offers_swag TEXT,
            response_efficiency_percentage INTEGER , submission_state TEXT , url TEXT , website TEXT , targets TEXT )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS FEDERACY
            (id INTEGER PRIMARY KEY UNIQUE, name TEXT , offers_awards TEXT , url TEXT , targets TEXT)''')
            
        cursor.execute('''CREATE TABLE IF NOT EXISTS HACKENPROOF
            (id INTEGER PRIMARY KEY UNIQUE, name TEXT , url TEXT , archived TEXT , triaged_by_hackenproof TEXT , targets TEXT)''')
            
        cursor.execute('''CREATE TABLE IF NOT EXISTS INTIGRITI
            (id INTEGER PRIMARY KEY UNIQUE, name TEXT , company_handle TEXT , handle TEXT , url TEXT , status TEXT , confidentiality_level TEXT ,min_bounty INTEGER , max_bounty INTEGER , targets TEXT )''')
            
        cursor.execute('''CREATE TABLE IF NOT EXISTS YESWEHACK
            (id INTEGER PRIMARY KEY UNIQUE, name TEXT , public TEXT , disabled TEXT , managed TEXT , min_bounty INTEGER  , max_bounty INTEGER , targets TEXT )''')



def request(url: str, retries: int = 20, delay: int = 5) -> dict:
    """
    Sends an HTTP GET request to the specified URL and retries on failure.
    
    :param url: The URL to send the request to.
    :param retries: Number of retry attempts in case of failure.
    :param delay: Delay between retries in seconds.
    :return: Parsed JSON data from the response if successful, None otherwise.
    """
    attempts = 0
    while attempts < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
            data = response.json()  # Automatically parses JSON
            print(f"{colorama.Fore.GREEN}Connection OK{colorama.Style.RESET_ALL}")
            return data
        except (RequestException, json.JSONDecodeError) as e:
            print(f"{colorama.Fore.RED}Failed to retrieve data: {e}. Retrying in {delay} seconds...{colorama.Style.RESET_ALL}")
            attempts += 1
            time.sleep(delay)
        except Exception as e:
            print(f"{colorama.Fore.RED}An unexpected error occurred: {e}{colorama.Style.RESET_ALL}")
            break
    print(f"{colorama.Fore.RED}Failed to retrieve data after {retries} attempts.{colorama.Style.RESET_ALL}")
    return None



# def request(url : str) :
#     try :
#         response = requests.get(programs[url])
#         response.raise_for_status()  # این خط خطاهای HTTP را چک می‌کند
#         data = response.json()
#     except NameError as e :
#         print (f"{colorama.Fore.RED} {e}")
#     except requests.exceptions.RequestException as e:
#         print (f"{colorama.Fore.RED} {e}")
#     return data


#chek if url or not!
def ifurl(url:str , type : str) ->bool: 
    
    if type == 'other' or type == 'website':
        x = requests.get('http://data.iana.org/TLD/tlds-alpha-by-domain.txt')
        tlds = x.text.split("\n")
        
        for i in range(len(tlds)):
        
            index = url.find('.'+tlds[i])
            if index>0:
                print(url+"  " + "✓")
                return True
                break
            else:
                continue
        if index<0:
            return False

    
#create TARGETS TABLE
def targets_create_table (name , bounty , targets , platform ):
    try:
        if bounty != None:
            if bounty >0 :     
                if platform == 'bugcrowd':        
                    for j in range(len(targets['in_scope'])):
                        
                        if (targets['in_scope'][j]['type'] == 'other' or  targets['in_scope'][j]['type'] == 'website'):#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):
                                
                            print(targets['in_scope'][j]['target']+'  '+ '[+]')
                                
                            try:
                                cursor.execute("INSERT OR REPLACE INTO TARGETS  (name , bounty , targets , platform) VALUES ( ? ,? , ? , ?)",
                                (name, bounty ,targets['in_scope'][j]['target'] , platform )) 
                    
                            except:
                                pass
                                                        
                elif platform == 'hackerone':
                    for j in range(len(targets['in_scope'])):
                        if (targets['in_scope'][j]['asset_type'] == 'URL' or targets['in_scope'][j]['asset_type'] == 'WILDCARD' or targets['in_scope'][j]['asset_type'] == 'OTHER' or targets['in_scope'][j]['asset_type'] == 'CIDR'):
                            print(targets['in_scope'][j]['asset_identifier']+'  '+ '[+]')

                            try:
                                cursor.execute("INSERT OR REPLACE INTO TARGETS  (name , bounty , targets , platform) VALUES (? , ? , ? , ?)",
                                (name, bounty ,targets['in_scope'][j]['asset_identifier'] , platform )) 
                
                            except:
                                pass
                        
                elif platform == 'federacy':
                    for j in range(len(targets['in_scope'])):
                            if (targets['in_scope'][j]['type'] == 'other' or  targets['in_scope'][j]['type'] == 'website' or  targets['in_scope'][j]['type'] == 'api'):#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):
                                
                                print(targets['in_scope'][j]['target']+'  '+ '[+]')
                                
                                try:
                                    cursor.execute("INSERT OR REPLACE INTO TARGETS  (name , bounty , targets , platform) VALUES ( ? ,? , ? , ?)",
                                    (name, bounty ,targets['in_scope'][j]['target'] , platform )) 
                    
                                except:
                                    pass
                elif platform == 'hackenproof':
                    for j in range(len(targets['in_scope'])):
                        
                            if targets['in_scope'][j]['type'] == 'Web' and targets['in_scope'][j]['reward'] == 'Bounty':#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):
                                
                                print(targets['in_scope'][j]['target']+'  '+ '[+]')
                                
                                try:
                                    cursor.execute("INSERT OR REPLACE INTO TARGETS  (name , bounty , targets , platform) VALUES ( ? ,? , ? , ?)",
                                    (name, bounty ,targets['in_scope'][j]['target'] , platform )) 
                    
                                except:
                                    pass                       
                        
                elif platform == 'intigriti':
                    for j in range(len(targets['in_scope'])):
                        
                            if (targets['in_scope'][j]['type'] == 'url' or targets['in_scope'][j]['type'] == 'wildcard'):#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):
                                
                                print(targets['in_scope'][j]['endpoint']+'  '+ '[+]')
                                
                                try:
                                    cursor.execute("INSERT OR REPLACE INTO TARGETS  (name , bounty , targets , platform) VALUES ( ? ,? , ? , ?)",
                                    (name, bounty ,targets['in_scope'][j]['endpoint'] , platform )) 
                    
                                except:
                                    pass      
                                                
                elif platform == 'yeswehack':
                    for j in range(len(targets['in_scope'])):
                            if (targets['in_scope'][j]['type'] == 'web-application' or targets['in_scope'][j]['type'] == 'other' or targets['in_scope'][j]['type'] == 'api'):#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):
                                print(targets['in_scope'][j]['target'])
                                print(targets['in_scope'][j]['target']+'  '+ '[+]')
                                
                                try:
                                    cursor.execute("INSERT OR REPLACE INTO TARGETS  (name , bounty , targets , platform) VALUES ( ? ,? , ? , ?)",
                                    (name, bounty ,targets['in_scope'][j]['target'] , platform )) 
                    
                                except:
                                    pass                     
    except KeyError as e :
        print(e)
    programs_db.commit()
           
#out of scope
def out_of_scope (name , bounty , targets , platform ):
    
    if bounty != None:
        if bounty >0 :     
            if platform == 'bugcrowd':        
                for j in range(len(targets['out_of_scope'])):
                    
                    if (targets['out_of_scope'][j]['type'] == 'other' or  targets['out_of_scope'][j]['type'] == 'website'):#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):
                            
                        print(targets['out_of_scope'][j]['target']+'  '+ '[-]')
                            
                        try:
                            cursor.execute("INSERT OR REPLACE INTO OUT_OF_SCOPE  (name , bounty , targets , platform) VALUES ( ? ,? , ? , ?)",
                            (name, bounty ,targets['out_of_scope'][j]['target'] , platform )) 
                
                        except:
                            pass
                        
        elif platform == 'hackerone':
            for j in range(len(targets['out_of_scope'])):
                if targets['out_of_scope'][j]['asset_type'] == 'URL':
                    
                    print(targets['out_of_scope'][j]['asset_identifier']+'  '+ '[-]')

                    try:
                        cursor.execute("INSERT OR REPLACE INTO OUT_OF_SCOPE  (name , bounty , targets , platform) VALUES (? , ? , ? , ?)",
                        (name, bounty ,targets['out_of_scope'][j]['asset_identifier'] , platform )) 
        
                    except:
                         pass
                     
        elif platform == 'federacy':
                    for j in range(len(targets['out_of_scope'])):
                            if (targets['out_of_scope'][j]['type'] == 'other' or  targets['out_of_scope'][j]['type'] == 'website'):#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):
                                
                                print(targets['out_of_scope'][j]['target']+'  '+ '[-]')
                                
                                try:
                                    cursor.execute("INSERT OR REPLACE INTO OUT_OF_SCOPE  (name , bounty , targets , platform) VALUES ( ? ,? , ? , ?)",
                                    (name, bounty ,targets['out_of_scope'][j]['target'] , platform )) 
                    
                                except:
                                    pass    

        elif platform == 'hackenproof':
            for j in range(len(targets['out_of_scope'])):
                
                    if targets['out_of_scope'][j]['type'] == 'Web' and targets['out_of_scope'][j]['reward'] == 'Bounty':#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):
                        
                        print(targets['out_of_scope'][j]['target']+'  '+ '[-]')
                        
                        try:
                            cursor.execute("INSERT OR REPLACE INTO OUT_OF_SCOPE  (name , bounty , targets , platform) VALUES ( ? ,? , ? , ?)",
                            (name, bounty ,targets['out_of_scope'][j]['target'] , platform )) 
            
                        except:
                            pass                       

        elif platform == 'intigriti':
            for j in range(len(targets['out_of_scope'])):
                
                    if targets['out_of_scope'][j]['type'] == 'url':#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):
                        
                        print(targets['out_of_scope'][j]['endpoint']+'  '+ '[-]')
                        
                        try:
                            cursor.execute("INSERT OR REPLACE INTO OUT_OF_SCOPE  (name , bounty , targets , platform) VALUES ( ? ,? , ? , ?)",
                            (name, bounty ,targets['out_of_scope'][j]['endpoint'] , platform )) 
            
                        except:
                            pass   
                        
        elif platform == 'yeswehack':
            for j in range(len(targets['out_of_scope'])):
                
                    if targets['out_of_scope'][j]['type'] == 'web-application' or targets['out_of_scope'][j]['type'] == 'other':#and ifurl(targets['in_scope'][j]['target'],targets['in_scope'][j]['type']):
                        
                        print(targets['out_of_scope'][j]['target']+'  '+ '[-]')
                        
                        try:
                            cursor.execute("INSERT OR REPLACE INTO OUT_OF_SCOPE  (name , bounty , targets , platform) VALUES ( ? ,? , ? , ?)",
                            (name, bounty ,targets['out_of_scope'][j]['target'] , platform )) 
            
                        except:
                            pass                   
                
                                              
    programs_db.commit()                           
    

#bugcrowd Create Table

def burgcrowd_create_tables (url : str) :
    
    urlib = request(programs[url])
    
    for i in range(len(urlib)) :
        try:
            targets_create_table(urlib[i]["name"]  , urlib[i]["max_payout"], urlib[i]["targets"], 'bugcrowd')
            out_of_scope(urlib[i]["name"]  , urlib[i]["max_payout"], urlib[i]["targets"], 'bugcrowd')

        except sqlite3.Error as e:
             print (f"error as {e}")    
        cursor.execute("INSERT OR REPLACE INTO BUGCROWD  (name , url , allows_disclosure , managed_by_bugcrowd , safe_harbor , targets , max_payout) VALUES (?, ? , ? , ? , ? , ? , ?)",
        (urlib[i]["name"], urlib[i]["url"] ,urlib[i]["allows_disclosure"] , urlib[i]["managed_by_bugcrowd"] ,urlib[i]["safe_harbor"],str(urlib[i]["targets"]), urlib[i]["max_payout"])) 

    programs_db.commit()


#hackerone Create Table

def hackerone_create_tables (url : str) :
    urlib = request(programs[url])
    
    for i in range(len(urlib)) :
        
        targets_create_table(urlib[i]["name"]  , 1, urlib[i]["targets"] , 'hackerone')
        out_of_scope(urlib[i]["name"]  , 1, urlib[i]["targets"] , 'hackerone')

        cursor.execute('''INSERT OR REPLACE INTO HACKERONE  (allows_bounty_splitting , average_time_to_bounty_awarded , average_time_to_first_program_response , average_time_to_report_resolved , handle , managed_program
        ,name ,offers_bounties , offers_swag , response_efficiency_percentage , submission_state , url ,website ,targets ) VALUES (?, ? , ? , ? , ? , ? , ? ,? ,? ,? ,? ,? ,? ,?)''',
        (urlib[i]["allows_bounty_splitting"], urlib[i]["average_time_to_bounty_awarded"] ,urlib[i]["average_time_to_first_program_response"] , urlib[i]["average_time_to_report_resolved"] ,urlib[i]["handle"], urlib[i]["managed_program"], urlib[i]["name"], urlib[i]["offers_bounties"],
        urlib[i]["offers_swag"], urlib[i]["response_efficiency_percentage"], urlib[i]["submission_state"], urlib[i]["url"], urlib[i]["website"], str(urlib[i]["targets"]))) 

    programs_db.commit()
    

#federacy Create Table

def federacy_create_tables (url : str) :
    urlib = request(programs[url])
    
    for i in range(len(urlib)) :
        try:
            if urlib[i]['offers_awards'] == True:
                targets_create_table(urlib[i]["name"]  , 1, urlib[i]["targets"] , 'federacy')
                out_of_scope(urlib[i]["name"]  , 1, urlib[i]["targets"] , 'federacy')
        
        except sqlite3.Error as e:
             print (f"error as {e}")
                     
        cursor.execute('''INSERT OR REPLACE INTO FEDERACY  (name , offers_awards , url , targets ) VALUES (?, ? , ? ,?)''',
        (urlib[i]["name"], urlib[i]["offers_awards"] ,urlib[i]["url"] , str(urlib[i]["targets"]))) 

    programs_db.commit()
    

#hackenproof Create Table

def hackenproof_create_tables (url : str) :
    urlib = request(programs[url])
   
    for i in range(len(urlib)) :
        try:
            targets_create_table(urlib[i]["name"]  , 1, urlib[i]["targets"] , 'hackenproof')
            out_of_scope(urlib[i]["name"]  , 1, urlib[i]["targets"] , 'hackenproof')

        except sqlite3.Error as e:
             print (f"error as {e}")       
        cursor.execute('''INSERT OR REPLACE INTO HACKENPROOF  (name , url , archived , triaged_by_hackenproof , targets ) VALUES (?, ? , ? , ? ,?)''',
        (urlib[i]["name"], urlib[i]["url"] ,urlib[i]["archived"] ,urlib[i]["triaged_by_hackenproof"] ,  str(urlib[i]["targets"]))) 

    programs_db.commit()
    


#intigriti Create Table

def intigriti_create_tables (url : str) :
    urlib = request(programs[url])

    for i in range(len(urlib)) :
        try :
            
            if urlib[i]['min_bounty']['value'] is not None:

                targets_create_table(urlib[i]["name"]  , 1, urlib[i]["targets"] , 'intigriti')
                out_of_scope(urlib[i]["name"]  , 1, urlib[i]["targets"] , 'intigriti')

                
        except sqlite3.Error as e:
             print (f"error as {e}")
        cursor.execute('''INSERT OR REPLACE INTO INTIGRITI  (name , company_handle , handle , url , status , confidentiality_level, min_bounty, max_bounty , targets) VALUES (? ,? ,? ,? ,? ,? ,? ,? ,?)''',
        (urlib[i]["name"], urlib[i]["company_handle"] ,urlib[i]["handle"] ,urlib[i]["url"] ,urlib[i]["status"] ,urlib[i]["confidentiality_level"] ,urlib[i]["min_bounty"]["value"] ,urlib[i]["max_bounty"]["value"]  ,  str(urlib[i]["targets"]))) 

    programs_db.commit()
    
    
#yeswehack Create Table

def yeswehack_create_tables (url : str) :
    urlib = request(programs[url])

    for i in range(len(urlib)) :

        targets_create_table(urlib[i]["name"]  , 1, urlib[i]["targets"] , 'yeswehack')
        out_of_scope(urlib[i]["name"]  , 1, urlib[i]["targets"] , 'yeswehack')
              
                

        #print(type(str(data[i]["targets"])))
        cursor.execute('''INSERT OR REPLACE INTO YESWEHACK  (name , public , disabled , managed , min_bounty , max_bounty, targets) VALUES (? ,? ,? ,? ,? ,? ,?)''',
        (urlib[i]["name"], urlib[i]["public"] ,urlib[i]["disabled"] ,urlib[i]["managed"] ,urlib[i]["min_bounty"] ,urlib[i]["max_bounty"] ,  str(urlib[i]["targets"]))) 

    programs_db.commit()


#targets Create Table

#def targets_create_table ():
    
#    cursor.execute('''CREATE TABLE IF NOT EXISTS TARGETS
#    (id INTEGER PRIMARY KEY UNIQUE, name TEXT , in_scope TEXT , out_scope TEXT)''')
    
 #   for i in programs :
  #      urlib = request(programs[i])
   #     print(urlib)
    #    for i in range(len(urlib)) :
     #     cursor.execute('''INSERT OR REPLACE INTO TARGETS  (name , in_scope , out_scope ) VALUES (? ,? , ?)''',
      #   (  )) 
          
   # programs_db.commit()
   # programs_db.close()
   
#deleting_tables()
#creating_tables()


#targets_create_table ()

#check_in_scope('bugcrowd_json_url',1)
#check_in_scope('hackerone_json_url',2)
#check_in_scope('federacy_json_url',3)
#check_in_scope('hackenproof_json_url',4)
#check_in_scope('intigriti_json_url',5)
#check_in_scope('yeswehack_json_url',6)

#checking()

#burgcrowd_create_tables('bugcrowd_json_url')
#hackerone_create_tables('hackerone_json_url')
#federacy_create_tables('federacy_json_url')
#hackenproof_create_tables('hackenproof_json_url')
#intigriti_create_tables('intigriti_json_url')
#yeswehack_create_tables('yeswehack_json_url')
