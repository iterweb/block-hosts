#!/usr/bin/python 3.7.8
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

get_hosts_list = requests.get('https://github.com/StevenBlack/hosts/blob/master/data/StevenBlack/hosts', headers=headers)

html = BeautifulSoup(get_hosts_list.content, 'html.parser')
table = html.find('table', class_='highlight tab-size js-file-line-container')

with open('C:\Windows\System32\drivers\etc\hosts') as hosts:
    file_read = hosts.read()

for row in table.find_all('tr'):
    col = row.find_all('td', class_='blob-code blob-code-inner js-file-line')
    print(col[0].text)
    link = col[0].text
    if link not in file_read:       
        f=open('C:\Windows\System32\drivers\etc\hosts', 'a')
        f.write(link + '\n')
        f.close
