import requests
from bs4 import BeautifulSoup

url_list = []
print("Enter Feed (^D to End):")
while True:
    try:
        packetstorm_input = input()
    except EOFError:
        break
    url_list.append(packetstorm_input)

url_list = ','.join(map(str, url_list))
strip_text = ['TITLE : Comments (0),', ',', ]

for i in strip_text:
    for item in url_list:
        url_list = url_list.replace(i, "")

url_list = url_list.split('URL :')
del url_list[0]

print("\n---Packetstorm Descriptions---")
for url in url_list:
    URL = url
    request = requests.get(URL)
    web_page = request.content

    soup = BeautifulSoup(web_page, 'lxml')
    text = soup.find_all(text=True)

    packetstorm_details = soup.select_one("dd[class=detail]").text

    try:
        related_cves = soup.select_one("dd[class=cve]").text
        related_cves = related_cves.strip('advisories | ')
    except AttributeError:
        related_cves = "No Related CVE(s)"

    print(url + "\n" + packetstorm_details + "\n" + related_cves + "\n")

'''    
TITLE : Comments (0)
URL :
http://packetstormsecurity.org/files/157404/Docker
-Credential-Wincred.exe-Privilege-Escalation.html

TITLE : Comments (0)
URL :
http://packetstormsecurity.org/files/157402/Geeklo
g-2.2.1-SQL-Injection.html
'''
