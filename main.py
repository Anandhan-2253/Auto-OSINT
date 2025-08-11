import argparse
from modules import ip_lookup, email_lookup, username_lookup
from rich.console import Console
from rich.table import Table
import os
import json
from datetime import datetime


def print_banner():
    # ANSI Colors
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    print(f"""
{RED}▄▄▄       █    ██ ▄▄▄█████▓ ▒█████      ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓
▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒   ▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒   ▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░   ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
 ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░   ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░    ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░      ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒     ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
      ░  ░   ░                  ░ ░         ░ ░        ░   ░           ░          
                                                                                  
{YELLOW}                              v1.0.0
{CYAN}                      Developed by: {MAGENTA}R00tGh0sT
{GREEN}             GitHub: https://github.com/Anandhan-2253
{RESET}
""")


def save_report(data, folder="reports"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/osint_report_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    console.print(f"[green]Report saved to {filename}[/green]")

def display_table(title, data_dict):
    table = Table(title=title)
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="magenta")
    for key, value in data_dict.items():
        table.add_row(str(key), str(value))
    console.print(table)

def main():
    print_banner()  # Display banner at start

    parser = argparse.ArgumentParser(description="Auto OSINT Toolkit")
    parser.add_argument("--ip", help="Target IP Address")
    parser.add_argument("--email", help="Target Email Address")
    parser.add_argument("--username", help="Target Username")
    parser.add_argument("--shodan", help="Shodan API Key")
    parser.add_argument("--hibp", help="HaveIBeenPwned API Key")
    args = parser.parse_args()

    final_report = {}

    if args.ip:
        console.print(f"[bold yellow]Performing IP OSINT on {args.ip}...[/bold yellow]")
        geo = ip_lookup.ip_geolocation(args.ip)
        whois_data = ip_lookup.ip_whois(args.ip)
        reverse_dns = ip_lookup.reverse_dns(args.ip)
        shodan_data = ip_lookup.shodan_lookup(args.ip, args.shodan) if args.shodan else {"error": "Shodan API Key not provided"}

        display_table("IP Geolocation", geo)
        final_report['IP Geolocation'] = geo

        console.print(f"[blue]WHOIS Data fetched[/blue]")
        final_report['WHOIS'] = whois_data

        console.print(f"[blue]Reverse DNS Result:[/blue] {reverse_dns}")
        final_report['Reverse DNS'] = reverse_dns

        final_report['Shodan'] = shodan_data

    if args.email:
        console.print(f"[bold yellow]Performing Email OSINT on {args.email}...[/bold yellow]")
        hibp = email_lookup.hibp_breach_check(args.email, args.hibp)
        validation = email_lookup.email_validation(args.email)

        if isinstance(hibp, list) and len(hibp) > 0:
            console.print(f"[red]Breached in {len(hibp)} data breaches:[/red]")
            for breach in hibp:
                console.print(f" - {breach['Name']}")
        else:
            console.print("[green]No breaches found[/green]")

        final_report['Email Breaches'] = hibp
        display_table("Email Validation", validation)
        final_report['Email Validation'] = validation

    if args.username:
        console.print(f"[bold yellow]Performing Username OSINT on {args.username}...[/bold yellow]")
        usernames = username_lookup.username_lookup(args.username)
        for platform, url in usernames.items():
            if url:
                console.print(f"[green][+] Found on {platform}[/green]: {url}")
            else:
                console.print(f"[red][-] Not Found on {platform}[/red]")
        final_report['Username Search'] = usernames

    save_report(final_report)

if __name__ == "__main__":
    main()
