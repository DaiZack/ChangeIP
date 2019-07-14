badip = []

def changeIP(ipnow=''):
    from bs4 import BeautifulSoup
    import requests
    url = 'https://free-proxy-list.net/'
    r = requests.get(url).content
    soup = BeautifulSoup(r)
    rows = soup.select('tr')[1:20]
    ips = [r.select('td')[0].text+':'+r.select('td')[1].text for r in rows]
    url = 'https://httpbin.org/ip'
    for ip in ips:
        if ip != ipnow and ip not in badip:
            try:
                response = requests.get(url,proxies={"http": ip, "https": ip})
                print(response.json())
                print(ip)
                return ip
            except:
                print('skip :',ip)
                badip.append(ip)
                continue

newip = changeIP('165.22.114.11:8080')
print('ipchanged to :', newip)
