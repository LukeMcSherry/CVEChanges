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

print("\n---CVE List---\n")
for cve in cve_list:
    cve = "CVE-{}".format(cve)
    cve_format_list.append(cve)

for cve in cve_format_list:
    print(cve)

print("\n---CVE Descriptions---")
for cve in cve_format_list:
    URL = "https://nvd.nist.gov/vuln/detail/{}".format(cve)
    request = requests.get(URL)
    web_page = request.content

    soup = BeautifulSoup(web_page, 'lxml')
    text = soup.find_all(text=True)

    cve_identifier = soup.select_one("span[data-testid=page-header-vuln-id]").text
    cve_description = soup.select_one("p[data-testid='vuln-description']").text
    cpe_configuration_clean = []

    try:
        cpe_configuration1 = soup.select("b[data-testid=vuln-software-cpe-1-0-0]")
        cpe_configuration1_2 = soup.select("b[data-testid=vuln-software-cpe-1-0-1]")
        cpe_configuration = cpe_configuration1 + cpe_configuration1_2
        cpe_configuration = str(cpe_configuration)
        strip_text = ['[', ']', '<b data-testid="vuln-software-cpe-1-0-0">cpe:2.3:',
                      '<b data-testid="vuln-software-cpe-1'
                      '-0-1">cpe:2.3:', ':*', '</b>']
        for i in strip_text:
            for item in cpe_configuration:
                cpe_configuration = cpe_configuration.replace(i, "")

        cpe_configuration = cpe_configuration.split(",")

        for i in cpe_configuration:
            cpe_configuration_clean.append(i.split(":")[2])

    except IndexError:
        cpe_configuration_clean.append("No CPE Configuration Found")

    print("\n" + cve_identifier, ":", cve_description)
    print("Affects: ", end="")
    print(*cpe_configuration_clean, sep=", ", end="")
