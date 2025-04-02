from client import invoke_cf
from session import get_selected_zones
from rich import print


def change_a_records():
    zones = get_selected_zones()
    if not zones:
        print("[red]No zones selected.[/red]")
        return

    print("[magenta]Enter the OLD IP:[/magenta]", end=" ")
    old_ip = input().strip()

    print("[magenta]Enter the NEW IP:[/magenta]", end=" ")
    new_ip = input().strip()

    updated_total = 0

    for domain, zone_id in zones.items():
        print(f"\n[bold cyan]Processing zone: {domain}[/bold cyan]")

        records = invoke_cf("GET", f"zones/{zone_id}/dns_records?type=A")["result"]
        zone_updated = 0

        for record in records:
            if record["content"] == old_ip:
                updated = {
                    "type": "A",
                    "name": record["name"],
                    "content": new_ip,
                    "ttl": record["ttl"],
                    "proxied": record["proxied"]
                }
                invoke_cf("PUT", f"zones/{zone_id}/dns_records/{record['id']}", data=updated)
                print(f"[green] Updated:[/green] {record['name']} → {new_ip}")
                zone_updated += 1

        if zone_updated == 0:
            print("[yellow]No matching A-records found.[/yellow]")

        updated_total += zone_updated

    print(f"\n[bold green]Done. {updated_total} record(s) updated in total.[/bold green]")



def toggle_https(enable: bool):
    value = "on" if enable else "off"
    for zone_id in get_selected_zones().values():
        invoke_cf("PATCH", f"zones/{zone_id}/settings/always_use_https", data={"value": value})
        print(f"[cyan]Always Use HTTPS set to {value.upper()} for zone {zone_id}[/cyan]")


def toggle_tls13(enable: bool):
    value = "on" if enable else "off"
    for zone_id in get_selected_zones().values():
        invoke_cf("PATCH", f"zones/{zone_id}/settings/tls_1_3", data={"value": value})
        print(f"[cyan]TLS 1.3 set to {value.upper()} for zone {zone_id}[/cyan]")


def change_ssl_mode():
    print("\nChoose SSL mode:")
    print("1. Flexible")
    print("2. Full")
    print("3. Strict")
    choice = input("Select an option (1-3): ").strip()

    mode_map = {"1": "flexible", "2": "full", "3": "strict"}
    mode = mode_map.get(choice)

    if not mode:
        print("[red]Invalid SSL mode selection.[/red]")
        return

    for zone_id in get_selected_zones().values():
        invoke_cf("PATCH", f"zones/{zone_id}/settings/ssl", data={"value": mode})
        print(f"[green]SSL mode set to {mode.upper()} for zone {zone_id}[/green]")

def purge_all_dns_records():
    confirm = input("Are you sure you want to DELETE ALL DNS records in selected zones? (y/n): ").strip().lower()
    if confirm != "y":
        print("[yellow]Aborted.[/yellow]")
        return

    for domain, zone_id in get_selected_zones().items():
        print(f"\n[bold red]Purging DNS for: {domain}[/bold red]")
        records = invoke_cf("GET", f"zones/{zone_id}/dns_records")["result"]
        deleted_count = 0

        for record in records:
            if record["type"] in ["A", "AAAA", "CNAME", "TXT", "MX", "SRV", "NS", "PTR", "SPF"]:
                invoke_cf("DELETE", f"zones/{zone_id}/dns_records/{record['id']}")
                print(f"[red]Deleted:[/red] {record['type']} {record['name']}")
                deleted_count += 1

        print(f"[green]Done. {deleted_count} record(s) deleted.[/green]")

def add_a_record():
    zones = get_selected_zones()
    if not zones:
        print("[red]No zones selected.[/red]")
        return

    print("[magenta]Enter the subdomain (e.g. 'api'). Use '@' for root domain:[/magenta]", end=" ")
    subdomain = input().strip()

    if subdomain == "@":
        for domain in zones.keys():
            name = domain  # заменяем @ на корневой домен
            break
    else:
        name = f"{subdomain}"

    print("[magenta]Enter the IP address:[/magenta]", end=" ")
    ip = input().strip()

    print("[magenta]Enter TTL (default is 1, press Enter to use default):[/magenta]", end=" ")
    ttl = input().strip()
    ttl = int(ttl) if ttl else 1  # Преобразуем TTL в целое число

    print("[magenta]Should the record be proxied? (y/n):[/magenta]", end=" ")
    proxied_input = input().strip().lower()
    proxied = True if proxied_input == "y" else False

    for domain, zone_id in zones.items():
        print(f"\n[bold cyan]Adding A-record to zone: {domain}[/bold cyan]")

        data = {
            "type": "A",
            "name": name,
            "content": ip,
            "ttl": ttl,  # передаем как число
            "proxied": proxied
        }

        response = invoke_cf("POST", f"zones/{zone_id}/dns_records", data=data)
        
        if response["success"]:
            print(f"[green]A-record added for {name} → {ip}[/green]")
        else:
            print(f"[red]Failed to add A-record for {name}[/red]")
