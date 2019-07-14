import time
badip = []
usedip = []

def changeIP(usedip=[]):
    from bs4 import BeautifulSoup
    import requests
    url = 'https://free-proxy-list.net/'
    r = requests.get(url).content
    soup = BeautifulSoup(r)
    rows = soup.select('tr')[1:]
    ips = [r.select('td')[0].text+':'+r.select('td')[1].text for r in rows]
    url = 'https://httpbin.org/ip'
    for ip in ips:
        if ip in usedip and ip not in badip:
            try:
                response = requests.get(url,proxies={"http": ip, "https": ip})
                if response.json():
                    print(ip)
                    return ip
            except:
                print('skip :',ip)
                badip.append(ip)
                continue

t0 = time.time()
for i in range(10):
    # do something
    time.sleep(3)
    t1 = time.time()
    if t1-t0>10:
        newip = changeIP(usedip)
        print('ipchanged to :', newip)
        if len(usedip)>9:
            usedip = []
        usedip.append(newip)
        t0=t1
    
