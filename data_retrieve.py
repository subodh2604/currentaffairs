from telethon.sync import TelegramClient,events
import configparser
from telethon import utils

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

config = configparser.ConfigParser()
config.read("config-sample.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

with TelegramClient(username,api_id,api_hash) as client:
    messages=client.get_messages('https://t.me/UPSC_Prelims_Mains_PDF_Materials',limit=2)
    for msg in messages:
        try:
            pdf_name=msg.media.document.attributes[0].file_name
        except:
            continue
        ans=input("Do you want to download pdf: "+msg.media.document.attributes[0].file_name +" ? [Y/N]"+"\n"+"Answer: ")
        print()
        if ans=='Y' or ans=='y':
            print("download--> : ",msg.media.document.attributes[0].file_name)
            client.download_media(msg,"files/")
            print()
            print()
        else:
            continue

import os

directory=r'C:\Users\User\Desktop\telegram-data-retrieve/files/'

gauth=GoogleAuth()
gauth.LocalWebserverAuth()
drive=GoogleDrive(gauth)

for x in os.listdir(directory): 
    f = drive.CreateFile({'title': x}) 
    f.SetContentFile(os.path.join(directory, x)) 
    f.Upload() 
    print("Uploading to google drive....")

    

