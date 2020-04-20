cve_list = []
print("Enter CVEs (Separated by New Line, ^D to End:")
while True:
    try:
        cve_input = input()
    except EOFError:
        break
    cve_list.append(cve_input)

for cve in cve_list:
    print("CVE-{}".format(cve))