import json
import time
from typing import Dict, List
import requests
from rich.console import Console
from rich.table import Table

console = Console()


# -------------------------------------------------------
# LOAD COOKIES
# -------------------------------------------------------

def load_cookies() -> Dict[str, str]:
    """
    Loads cookies from cookies.txt where the user pastes a Python dict like:
    cookies = {
        "name": "value",
        ...
    }
    """
    try:
        with open("cookies.txt", "r", encoding="utf-8") as f:
            content = f.read()

        # Local dictionary to capture executed variables
        local_vars = {}
        exec(content, {}, local_vars)

        if "cookies" not in local_vars:
            console.print("[bold red]cookies.txt is missing the variable 'cookies'[/]")
            return {}

        return local_vars["cookies"]

    except FileNotFoundError:
        console.print("[bold red]cookies.txt not found![/]")
        return {}
    except Exception as e:
        console.print(f"[bold red]Error reading cookies.txt: {e}[/]")
        return {}



# -------------------------------------------------------
# GLOBAL HEADERS
# -------------------------------------------------------

HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "text/plain",
    "Origin": "https://www.icloud.com",
    "Referer": "https://www.icloud.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Chromium";"Google Chrome";"Not A(Brand"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}


# -------------------------------------------------------
# UTIL: CLEAN API RESPONSE
# -------------------------------------------------------

def parse_response(res):
    """
    Converts Apple API response into readable status messages.
    """
    try:
        data = res.json()

        if data.get("success"):
            return True, "Success"

        if "error" in data:
            err = data["error"]
            reason = err.get("errorMessage", "Unknown error")
            return False, reason

        return False, "Unknown response format"

    except Exception:
        return False, "Invalid JSON response"


# -------------------------------------------------------
# FETCH HME LIST
# -------------------------------------------------------

def fetch_hme_list(cookies: Dict[str, str]) -> List[Dict]:
    dsid = cookies["X-APPLE-WEBAUTH-USER"].split("d=")[-1].replace('"', "")

    params = {
        "clientBuildNumber": "2542Build17",
        "clientMasteringNumber": "2542Build17",
        "clientId": "auto-script",
        "dsid": dsid
    }

    url = "https://p158-maildomainws.icloud.com/v2/hme/list"

    console.print("[bold cyan]Fetching Hide My Email list...[/]")

    res = requests.get(url, headers=HEADERS, cookies=cookies, params=params)

    try:
        return res.json()["result"]["hmeEmails"]
    except:
        console.print("[bold red]❌ Failed to parse response from Apple[/]")
        console.print(res.text)
        return []


# -------------------------------------------------------
# DEACTIVATE
# -------------------------------------------------------

def deactivate_hme(cookies: Dict[str, str], anon_id: str):
    dsid = cookies["X-APPLE-WEBAUTH-USER"].split("d=")[-1].replace('"', "")
    url = "https://p158-maildomainws.icloud.com/v1/hme/deactivate"
    payload = json.dumps({"anonymousId": anon_id})

    params = {
        "clientBuildNumber": "2542Build17",
        "clientMasteringNumber": "2542Build17",
        "clientId": "auto-script",
        "dsid": dsid
    }

    res = requests.post(url, headers=HEADERS, cookies=cookies, params=params, data=payload)
    return parse_response(res)


# -------------------------------------------------------
# DELETE
# -------------------------------------------------------

def delete_hme(cookies: Dict[str, str], anon_id: str):
    dsid = cookies["X-APPLE-WEBAUTH-USER"].split("d=")[-1].replace('"', "")
    url = "https://p158-maildomainws.icloud.com/v1/hme/delete"
    payload = json.dumps({"anonymousId": anon_id})

    params = {
        "clientBuildNumber": "2542Build17",
        "clientMasteringNumber": "2542Build17",
        "clientId": "auto-script",
        "dsid": dsid
    }

    res = requests.post(url, headers=HEADERS, cookies=cookies, params=params, data=payload)
    return parse_response(res)


# -------------------------------------------------------
# MAIN SCRIPT
# -------------------------------------------------------

def main():

    console.print("[bold green]🚀 Hide My Email Manager[/]")

    cookies = load_cookies()

    if not cookies:
        console.print("[red]No cookies loaded![/]")
        return

    hme_list = fetch_hme_list(cookies)

    if not hme_list:
        console.print("[yellow]No Hide My Email entries found.[/]")
        return

    # Save to file
    with open("emails.txt", "w", encoding="utf-8") as f:
        for h in hme_list:
            f.write(
                f"anonymousId: {h['anonymousId']} | email: {h['hme']} | active: {h['isActive']}\n"
            )

    console.print(f"[green]Saved {len(hme_list)} entries to emails.txt[/]\n")

    # Table
    table = Table(title="Hide My Email Entries")
    table.add_column("ID")
    table.add_column("Email")
    table.add_column("Active")

    for h in hme_list:
        table.add_row(h["anonymousId"], h["hme"], str(h["isActive"]))

    console.print(table)

    console.print("\n[bold red]Starting deactivation + deletion...[/]")

    for h in hme_list:

        anon = h["anonymousId"]
        email = h["hme"]

        console.print("\n[cyan]────────────────────────────────────────[/]")
        console.print(f"[white]📧 Email:[/] {email}")
        console.print(f"[white]🔑 ID:[/] {anon}")

        # Status
        if h["isActive"]:
            console.print("[yellow]🟡 Status: ACTIVE[/]")

            ok, msg = deactivate_hme(cookies, anon)
            icon = "✔" if ok else "✖"
            console.print(f" → Deactivating... {icon} {msg}")
            time.sleep(1)

        else:
            console.print("[blue]🔵 Status: INACTIVE (skipping deactivation)[/]")

        # Delete
        ok, msg = delete_hme(cookies, anon)
        icon = "✔" if ok else "✖"
        console.print(f" → Deleting....... {icon} {msg}")
        time.sleep(1)

        console.print("[cyan]────────────────────────────────────────[/]")

    console.print("\n[bold green]✔ All entries processed successfully![/]")


if __name__ == "__main__":
    main()
