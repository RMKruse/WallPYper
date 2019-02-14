# Dependencies laden:
import os
import tqdm
import time
import urllib 
import getpass
import bs4
import re
import requests

# Ordner erschaffen:
os.makedirs('wallpaper_wallhaven', exist_ok=True)

# Log-In fuer versaute Sachen:
def login():
    print('Einige Auflösungen brauchen einen login:')
    username = input('Benutzername eingeben: ')
    password = getpass.getpass('Password eingeben: ')
    req = requests.post('https://alpha.wallhaven.cc/auth/login', 
                   data={'username':username, 'password':password})
    return req.cookies

# 
