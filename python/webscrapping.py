#!/usr/bin/python3

import requests # http requests

from bs4 import BeautifulSoup # for web scrapping

import smtplib #sending emails

#email body
from email.mime.multpart import MIMEMultpart
from email.mime.text import MIMEText

#system date and time
import datetime
now = datetime.datetime.now()

#email content
content = ''
def scrap_news(url):
    print("scrapping news......")
    cnt = ''
    cnt+ = ('<b> Top Stories</b>\n'+'<br>'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')


