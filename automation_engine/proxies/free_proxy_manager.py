import requests
from bs4 import BeautifulSoup
import concurrent.futures
from config import settings

def scrape_proxies():
    proxy_sources = [
        "https://sslproxies.org/",
        "https://free-proxy-list.net/",
        "https://www.proxyscrape.com/free-proxy-list"
    ]
    
    proxies = []
    for url in proxy_sources:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            for row in soup.find_all('tr'):
                cols = row.find_all('td')
                if len(cols) >= 2:
                    ip = cols[0].text.strip()
                    port = cols[1].text.strip()
                    if ip and port and ip.count('.') == 3:
                        proxies.append(f"{ip}:{port}")
        except:
            continue
            
    return list(set(proxies))

def validate_proxy(proxy):
    try:
        response = requests.get(settings.PROXY_TEST_URL, proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=settings.PROXY_TIMEOUT)
        origin = response.json().get("origin", "")
        proxy_ip = proxy.split(":")[0]
        return origin == proxy_ip
    except:
        return False

def get_valid_proxies():
    all_proxies = scrape_proxies()
    valid_proxies = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_proxy = {executor.submit(validate_proxy, proxy): proxy for proxy in all_proxies}
        for future in concurrent.futures.as_completed(future_to_proxy):
            if future.result():
                valid_proxies.append(future_to_proxy[future])
    return valid_proxies