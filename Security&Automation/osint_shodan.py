import shodan
import requests

SHODAN_API_KEY =  "INSERT_API_KEY_HERE"

api = shodan.Shodan(SHODAN_API_KEY)

target = 'www.reddit.com'

dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + target + '&key=' + SHODAN_API_KEY

try:
    resolved = requests.get(dnsResolve)
    hostAddr = resolved.json()[target]
    host = api.host(hostAddr)
    print("IP: %s" %host['ip_str'])
    print("Organization: %s" %host.get('org', 'n/a'))
    print("OS: %s" %host.get('os', 'n/a'))

    for item in host['data']:
        print("Port: %s" %item['port'])
        print("Banner: %s" %item['data'])
    for item in host['vulns']:
        CVE = item.replace('!','')
        print("Vulns: %s" %item)
        exploits = api.exploits.search(CVE)
        for item in exploits['matches']:
            if item.get('cve')[0] == CVE:
                print(item.get('description'))
except:
    'An error occured!'
