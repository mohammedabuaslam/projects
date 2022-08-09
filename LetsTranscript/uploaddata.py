import sqlite3
import pandas as pd
from tqdm import tqdm
import secrets
import requests


listoftuples = []
logourls = []

dataset = pd.read_excel(r'C:\Users\abuas\Downloads\LetsTranscript DB\lets\modified2.xlsx', sheet_name='URLS')

def logourlmaker(website):
    if str(website) == 'Not Specified':
        sendthis = '../../../static/assets/img/defualtcompanylogo.png'
        logourls.append(sendthis)
        return sendthis
    logoassigner = requests.get('https://logo.clearbit.com/'+str(website))
    if logoassigner.status_code == 200:
        sendthis = 'https://logo.clearbit.com/'+str(website)+'?size=64&format=png'
    else:
        logoassigner = requests.get('https://www.google.com/s2/favicons?sz=64&domain_url='+str(website))
        if logoassigner.status_code == 200:
            sendthis = 'https://www.google.com/s2/favicons?sz=64&domain_url='+str(website)
        else:
            sendthis = '../../../static/assets/img/defualtcompanylogo.png'
    logourls.append(sendthis)
    return sendthis

for i in tqdm(range(0,len(dataset))):
    # logomaker = logourlmaker(dataset['Website'][i])
    passingdata = (str(dataset['Names'][i]),str(dataset['Rating'][i]),str(dataset['No_Of_Reviews'][i]),str(dataset['Service'][i]),'',str(dataset['City'][i]),
                    str(dataset['State'][i]),str(dataset['Country'][i]),str(dataset['Experience'][i]),str(dataset['Website'][i]),'nofollow noopener noreferrer',str(dataset['Phone'][i]),
                    secrets.token_hex(15),'','','',str(dataset['Description'][i]),str(dataset['Logo Urls'][i]))
    listoftuples.append(passingdata)



sqlite_insert_query = """INSERT INTO directory_Directory ('companyname','rating','reviewcount','industry',
                        'address','city','state','country','experience','website','reltype','phone','uniqueid','metatitle',
                        'metadescription','metakeywords','pagedescription','logourl')
                        VALUES
                        (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                        
# sqlite_insert_query = """INSERT INTO directory_Sidelinks ('industry','url')
#                         VALUES
#                         (?,?)"""

con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.executemany(sqlite_insert_query,listoftuples)
con.commit()
con.close()

# count = cur.execute(sqlite_insert_query,passingdata)


# cur.execute('DELETE FROM directory_Sidelinks;',);

# --------------------------------------------------------------------------------------------------------

sitemaps = ['/directory/usa/transcription-services/wyoming/','/directory/usa/transcription-services/','/directory/usa/transcription-services/alabama/','/directory/usa/transcription-services/alaska/','/directory/usa/transcription-services/arizona/','/directory/usa/transcription-services/arkansas/','/directory/usa/transcription-services/california/','/directory/usa/transcription-services/colorado/','/directory/usa/transcription-services/connecticut/','/directory/usa/transcription-services/delaware/','/directory/usa/transcription-services/florida/','/directory/usa/transcription-services/georgia/','/directory/usa/transcription-services/hawaii/','/directory/usa/transcription-services/idaho/','/directory/usa/transcription-services/illinois/','/directory/usa/transcription-services/indiana/','/directory/usa/transcription-services/iowa/','/directory/usa/transcription-services/kansas/','/directory/usa/transcription-services/kentucky/','/directory/usa/transcription-services/louisiana/','/directory/usa/transcription-services/maine/','/directory/usa/transcription-services/maryland/','/directory/usa/transcription-services/massachusetts/','/directory/usa/transcription-services/michigan/','/directory/usa/transcription-services/minnesota/','/directory/usa/transcription-services/mississippi/','/directory/usa/transcription-services/missouri/','/directory/usa/transcription-services/montana/','/directory/usa/transcription-services/nebraska/','/directory/usa/transcription-services/nevada/','/directory/usa/transcription-services/new-hampshire/','/directory/usa/transcription-services/new-jersey/','/directory/usa/transcription-services/new-mexico/','/directory/usa/transcription-services/new-york/','/directory/usa/transcription-services/north-carolina/','/directory/usa/transcription-services/north-dakota/','/directory/usa/transcription-services/ohio/','/directory/usa/transcription-services/oklahoma/','/directory/usa/transcription-services/oregon/','/directory/usa/transcription-services/pennsylvania/','/directory/usa/transcription-services/rhode-island/','/directory/usa/transcription-services/south-carolina/','/directory/usa/transcription-services/south-dakota/','/directory/usa/transcription-services/tennessee/','/directory/usa/transcription-services/texas/','/directory/usa/transcription-services/utah/','/directory/usa/transcription-services/vermont/','/directory/usa/transcription-services/virginia/','/directory/usa/transcription-services/washington/','/directory/usa/transcription-services/west-virginia/','/directory/usa/transcription-services/wisconsin/']

import psycopg2

connection = psycopg2.connect(database="postgres", user="LetsTranscriptDB", password="PayloadATA", host="letstranscriptdb.cjrmd3r1ge1r.us-east-2.rds.amazonaws.com", port=5432)

cur = connection.cursor()


# sqlite_insert_query = """INSERT INTO main_Sitemaps ("companyname","rating","reviewcount","industry","address","city","state","country","experience","website","reltype","phone","uniqueid","metatitle","metadescription","metakeywords","pagedescription","logourl")VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

sqlite_insert_query = """INSERT INTO main_Sitemaps ("sitemapurl","priority","changefrequency")VALUES(%s,%s,%s)"""



# cur.executemany(sqlite_insert_query,listoftuples)

for s in sitemaps:
    cur.execute(sqlite_insert_query,(s,"1.00","monthly"))

connection.commit()
connection.close()





















