import requests
import json

def main():
    content = requests.get("https://cve.circl.lu/api/last")
    json = content.json()

    for entry in json:
        print("{} \033[91m{}\033[0m".format("Vuln No:", entry['id'] ))
        #print("{} \033[91m{}\033[0m".format("Vuln Name:", entry['name'] ))        
        print("{} \033[92m{}\033[0m \n".format("Description:", entry['summary']))
        #print("{} {} ".format("Remediation:", entry['solutions']))

main()