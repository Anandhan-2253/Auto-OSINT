import requests
from bs4 import BeautifulSoup

# List of websites to check username presence
platforms = {
    "GitHub": "https://github.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "TikTok": "https://www.tiktok.com/@{}"
}

def username_lookup(username):
    found = {}
    for platform, url in platforms.items():
        full_url = url.format(username)
        response = requests.get(full_url)
        if response.status_code == 200:
            found[platform] = full_url
        else:
            found[platform] = None
    return found

# Example Usage
if __name__ == "__main__":
    username = "johndoe"
    results = username_lookup(username)
    for platform, url in results.items():
        if url:
            print(f"[+] Found on {platform}: {url}")
        else:
            print(f"[-] Not Found on {platform}")
