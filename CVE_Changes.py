import requests
from bs4 import BeautifulSoup

cve_list = []
cve_format_list = []
print("Enter CVEs (Separated by New Line, ^D to End:")
while True:
    try:
        cve_input = input()
    except EOFError:
        break
    cve_list.append(cve_input)

print("\n\n---CVE List---\n")
for cve in cve_list:
    cve = "CVE-{}".format(cve)
    cve_format_list.append(cve)

for cve in cve_format_list:
    print(cve)

print("\n\n---CVE Description---")
for cve in cve_format_list:
    URL = "https://nvd.nist.gov/vuln/detail/{}".format(cve)
    request = requests.get(URL)
    web_page = request.content

    soup = BeautifulSoup(web_page, 'lxml')
    text = soup.find_all(text=True)
    cve_identifier = soup.select_one("span[data-testid=page-header-vuln-id]").text
    cve_description = soup.select_one("p[data-testid='vuln-description']").text
    print("\n"+cve_identifier, ":", cve_description)