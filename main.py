#!/usr/bin/env python3
# main.py — Auto OSINT Toolkit with Help & Examples

import argparse
from modules import ip_lookup, email_lookup, username_lookup
from rich.console import Console
from rich.table import Table
import os
import json
from datetime import datetime
import sys

console = Console()

# --------------------------
# Save Report
# --------------------------
def save_report(data, folder="reports"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/osint_report_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    console.print(f"[green]Report saved to {filename}[/green]")

# --------------------------
# Display Table
# --------------------------
def display_table(title, data_dict):
    table = Table(title=title)
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="magenta")
    for key, value in data_dict.items():
        table.add_row(str(key), str(value))
    console.print(table)

# --------------------------
# Print Examples & Exit
# --------------------------
def print_examples():
    console.print("\n[bold cyan]Auto OSINT Toolkit - Usage Examples[/bold cyan]\n")
    console.print("1️⃣ [yellow]IP Lookup with Shodan API Key[/yellow]")
    console.print("   python main.py --ip 8.8.8.8 --shodan YOUR_SHODAN_KEY\n")
    
    console.print("2️⃣ [yellow]Email Breach Check (HaveIBeenPwned API)[/yellow]")
    console.print("   python main.py --email target@example.com --hibp YOUR_HIBP_KEY\n")
    
    console.print("3️⃣ [yellow]Username Search Across Platforms[/yellow]")
    console.print("   python main.py --username johndoe\n")
    
    console.print("4️⃣ [yellow]Combine Multiple Lookups[/yellow]")
    console.print("   python main.py --ip 1.1.1.1 --email test@mail.com --username alice --shodan KEY --hibp KEY\n")
    
    console.print("Reports are automatically saved in the [green]'reports/'[/green] folder.\n")
    sys.exit(0)

# --------------------------
# Main Function
# --------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Auto OSINT Toolkit — Gather public intelligence on IPs, Emails, and Usernames."
    )
    parser.add_argument("--ip", help="Target IP Address")
    parser.add_argument("--email", help="Target Email Address")
    parser.add_argument("--username", help="Target Username")
    parser.add_argument("--shodan", help="Shodan API Key (for IP scanning)")
    parser.add_argument("--hibp", help="HaveIBeenPwned API Key (for email breach checks)")
    parser.add_argument("--examples", action="store_true", help="Show usage examples and exit")
    
    args = parser.parse_args()

    if args.examples:
        print_examples()

    final_report = {}

    # IP OSINT
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

    # Email OSINT
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

    # Username OSINT
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
