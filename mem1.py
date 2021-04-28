import requests

first_links = input()
r= requests.get(first_links)
zu = r.text
while zu[0] != 'W' and zu[1]!='e':
    r=requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+zu)
    print(zu)
    zu = r.text
print(zu)