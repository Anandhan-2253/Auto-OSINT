import requests

# 1. Email Breach Check using HaveIBeenPwned API
def hibp_breach_check(email, api_key):
    headers = {
        'hibp-api-key': api_key,
        'user-agent': 'AutoOSINT-Tool'
    }
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return []
    else:
        return {"error": f"Error Code: {response.status_code}"}

# 2. Email Validation (Simple SMTP Check Simulation)
def email_validation(email):
    api = f"https://api.eva.pingutil.com/email?email={email}"
    response = requests.get(api).json()
    return response

# Example Usage
if __name__ == "__main__":
    email = "test@example.com"
    hibp_api_key = "YOUR_HIBP_API_KEY"
    print("[+] HIBP Breach Check:", hibp_breach_check(email, hibp_api_key))
    print("[+] Email Validation:", email_validation(email))
