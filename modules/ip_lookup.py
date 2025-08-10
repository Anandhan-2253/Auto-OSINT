# modules/ip_lookup.py

import requests
import whois

def ip_geolocation(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url).json()
    return response

def ip_whois(ip):
    w = whois.whois(ip)
    return w.text

def shodan_lookup(ip, api_key):
    url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
    response = requests.get(url).json()
    return response

def reverse_dns(ip):
    try:
        result = requests.get(f"https://api.hackertarget.com/reversedns/?q={ip}")
        return result.text
    except:
        return "Reverse DNS lookup failed"

# Example Usage
if __name__ == "__main__":
    ip = "1.1.1.1"
    shodan_api_key = "YOUR_SHODAN_API_KEY"
    print("[+] Geolocation:", ip_geolocation(ip))
    print("[+] WHOIS:", ip_whois(ip))
    print("[+] Shodan:", shodan_lookup(ip, shodan_api_key))
    print("[+] Reverse DNS:", reverse_dns(ip))
