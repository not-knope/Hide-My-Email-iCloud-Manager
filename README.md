# 🙈 Hide My Email Manager

> Manage your Apple iCloud **Hide My Email** addresses from the command line — list, deactivate, and delete entries in bulk, with a polished terminal interface.

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/not-knope/Hide-My-Email-iCloud-Manager?style=social)](https://github.com/not-knope/Hide-My-Email-iCloud-Manager/stargazers)

---

## 🎥 Video Tutorial

[![Full Tutorial](https://img.youtube.com/vi/I_if9q9gx6I/0.jpg)](https://youtu.be/I_if9q9gx6I)

*Click the thumbnail to watch the full setup and usage guide.*

---

## ✨ Features

| Feature | Description |
|---|---|
| 📋 **List** | Fetch your complete Hide My Email address list from iCloud |
| 🛑 **Deactivate** | Deactivate active aliases in bulk |
| 🗑️ **Delete** | Delete both active and inactive entries |
| 💾 **Export** | Save all entries to `emails.txt` |
| 🎨 **Rich UI** | Beautiful, color-coded terminal output via the [Rich](https://github.com/Textualize/rich) library |

---

## ⚠️ Security Warning

> **Your iCloud session cookies grant full access to your account.**
>
> - **Never share** your `cookies.txt` with anyone
> - **Never commit** it to version control — it is already in `.gitignore`
> - Cookies **expire periodically** — re-extract them when the script stops working
> - Use this script only on a machine you trust and own

---

## 📋 Prerequisites

- Python 3.7 or higher
- An Apple iCloud account with Hide My Email addresses
- A web browser with Developer Tools (to extract session cookies)

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/not-knope/Hide-My-Email-iCloud-Manager.git
cd Hide-My-Email-iCloud-Manager
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

This installs:
- [`requests`](https://requests.readthedocs.io/) — HTTP requests to the iCloud API
- [`rich`](https://github.com/Textualize/rich) — Beautiful terminal output

### 3. Extract and configure your iCloud cookies

```bash
cp cookies.txt.template cookies.txt
```

Then open `cookies.txt` and paste your cookies in this format:

```python
cookies = {
    'X-APPLE-WEBAUTH-USER': '"v=1:s=0:d=YOUR_DSID"',
    'X-APPLE-WEBAUTH-TOKEN': '"v=2:t=YOUR_TOKEN"',
    'X-APPLE-DS-WEB-SESSION-TOKEN': '"YOUR_SESSION_TOKEN"',
    # ... add all other X-APPLE-* cookies here
}
```

**How to extract your cookies:**

1. Log in to [icloud.com](https://www.icloud.com) in your browser
2. Open **Developer Tools** (`F12` / `Cmd+Option+I`)
3. Navigate to **Application** (Chrome) or **Storage** (Firefox) → **Cookies** → `https://www.icloud.com`
4. Copy all cookies whose names start with `X-APPLE-`
5. Paste them into `cookies.txt`

> 💡 Watch the [video tutorial](https://youtu.be/I_if9q9gx6I) for a step-by-step walkthrough.

### 4. Run the script

```bash
python main.py
```

---

## 🖥️ Screenshots

![Hide My Email Manager — email list](https://i.nuuls.com/dZfdo.png)
![Hide My Email Manager — in action](https://i.nuuls.com/zL-04.png)

---

## 📄 Output

When run, the script will:

1. Load your session from `cookies.txt`
2. Fetch all Hide My Email entries from iCloud
3. Display them in a formatted table in the terminal
4. Save the full list to `emails.txt`
5. Deactivate all active entries
6. Delete all entries (active and inactive)

### `emails.txt` format

```
anonymousId: abc123... | email: xyz@icloud.com | active: True
anonymousId: def456... | email: abc@icloud.com | active: False
```

---

## 🛠️ Error Handling

The script gracefully handles:

- 🔒 Authentication failures (invalid or expired cookies)
- 🌐 Network connectivity issues
- ⏱️ API timeouts
- 📁 File I/O errors
- 🔍 Malformed cookie format
- 📊 Empty or unexpected API responses

---

## 🔍 Troubleshooting

**Cookies not working?**
- Make sure you are actively logged in to iCloud.com when you extract them
- Cookies expire — try extracting fresh ones
- Ensure you copied **all** `X-APPLE-*` cookies, not just a few

**No entries found?**
- Confirm your iCloud account actually has Hide My Email addresses set up
- Verify the cookies are valid and not expired

**API errors?**
- Wait a few minutes and retry — iCloud may rate-limit requests
- Check your internet connection
- Visit [Apple's System Status](https://www.apple.com/support/systemstatus/) to rule out an outage

---

## 🤝 Contributing

Contributions are welcome!

- 🐛 [Report a bug](https://github.com/not-knope/Hide-My-Email-iCloud-Manager/issues/new)
- 💡 [Suggest a feature](https://github.com/not-knope/Hide-My-Email-iCloud-Manager/issues/new)
- 🔧 Open a pull request

---

## 📦 Star History

<a href="https://www.star-history.com/?repos=not-knope/Hide-My-Email-iCloud-Manager&type=date&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=not-knope/Hide-My-Email-iCloud-Manager&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=not-knope/Hide-My-Email-iCloud-Manager&type=date&legend=top-left" />
    <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=not-knope/Hide-My-Email-iCloud-Manager&type=date&legend=top-left" />
  </picture>
</a>

---

## 📜 License

Licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- [Rich](https://github.com/Textualize/rich) — Terminal formatting library
- [Requests](https://requests.readthedocs.io/) — HTTP library for Python
