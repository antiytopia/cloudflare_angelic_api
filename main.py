from session import set_token, get_token, set_selected_zones, get_selected_zones, clear_selected_zones
from client import invoke_cf
import dns_actions
from rich import print


def show_token_info():
    print("""
[bold red]To use this tool, you need a Cloudflare API Token with the following permissions:[/bold red]
[green]- Zone - Read
- Zone Settings - Read
- Zone Settings - Edit
- DNS - Read
- DNS - Edit[/green]
    """)
    print("[bold magenta]Paste your Cloudflare API Token:[/bold magenta]", end=" ")
    token = input().strip()
    set_token(token)

    print("[bold green]Token saved![/bold green]")

def get_all_zones():
    all_zones = []
    page = 1

    first_response = invoke_cf("GET", "zones?page=1&per_page=50")
    all_zones.extend(first_response["result"])

    total_pages = first_response.get("result_info", {}).get("total_pages", 1)

    for page in range(2, total_pages + 1):
        response = invoke_cf("GET", f"zones?page={page}&per_page=50")
        all_zones.extend(response["result"])

    return all_zones

def input_domains():
    print("[bold magenta]\nEnter your domains (one per line). Enter an empty line to finish:[/bold magenta]")
    domains = []
    while True:
        line = input().strip()
        if line == "":
            break
        domains.append(line)

    all_zones = get_all_zones()



    zone_dict = {}
    for domain in domains:
        match = next((z for z in all_zones if z["name"] == domain), None)
        if match:
            zone_dict[domain] = match["id"]
        else:
            print(f"[yellow]Domain not found in account: {domain}[/yellow]")
            print("\n[bold yellow]All zones available to your token:[/bold yellow]")
            for z in all_zones:
                print(f"- {z['name']}")

    set_selected_zones(zone_dict)
    print(f"[green]Added {len(zone_dict)} domain(s)[/green]")


def show_selected_zones():
    selected = get_selected_zones()
    if selected:
        print("\n[bold cyan]Selected Zones:[/bold cyan]")
        for domain, zone_id in selected.items():
            print(f"[green]{domain}[/green] → {zone_id}")
    else:
        print("[yellow]No zones selected.[/yellow]")


def clear_zones():
    print("[bold red]Are you sure you want to clear selected zones? (y/n):[/bold red]", end=" ")
    confirm = input().strip().lower()

    if confirm == "y":
        clear_selected_zones()
        print("[red]Zone selection cleared.[/red]")


def main_menu():
    while True:
        print("""
[bold magenta]Cloudflare API Menu:[/bold magenta]
[magenta]1.[/] Set API Token
[magenta]2.[/] Input Domains Manually
[magenta]3.[/] Show Selected Zones
[magenta]4.[/] Clear Selected Zones
[magenta]5.[/] Change A-record IPs
[magenta]6.[/] Enable Always Use HTTPS
[magenta]7.[/] Disable TLS 1.3
[magenta]8.[/] Change SSL Mode
[magenta]9.[/] Purge All DNS Records
[magenta]0.[/] Exit
""")
        print("[bold magenta]Select an option:[/bold magenta]", end=" ")
        choice = input().strip()

        if choice == "1":
            show_token_info()
        elif choice == "2":
            input_domains()
        elif choice == "3":
            show_selected_zones()
        elif choice == "4":
            clear_zones()
        elif choice == "5":
            dns_actions.change_a_records()
        elif choice == "6":
            dns_actions.toggle_https(True)
        elif choice == "7":
            dns_actions.toggle_tls13(False)
        elif choice == "8":
            dns_actions.change_ssl_mode()
        elif choice == "9":
            dns_actions.purge_all_dns_records()
        elif choice == "0":
            print("[bold red]Goodbye![/bold red]")
            break
        else:
            print("[red]Invalid option. Try again.[/red]")



if __name__ == "__main__":
    main_menu()