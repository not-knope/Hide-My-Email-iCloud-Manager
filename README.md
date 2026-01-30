# Hide My Email Manager

A Python script that manages Apple iCloud Hide My Email addresses. List, deactivate, and delete Hide My Email entries with a beautiful console interface.

## 🎥 Video Tutorial

[![Full Tutorial](https://img.youtube.com/vi/I_if9q9gx6I/0.jpg)](https://youtu.be/I_if9q9gx6I)
[![Full Tutorial](https://img.youtube.com/vi/I_if9q9gx6I/0.jpg)](https://youtu.be/I_if9q9gx6I)



## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/not-knope/Hide-My-Email-iCloud-Manager.git
cd Hide-My-Email-iCloud-Manager
```

### 2. Install dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- `requests` - for making HTTP requests to iCloud API
- `rich` - for beautiful console output

### 3. Configure cookies

Copy the template and add your iCloud cookies:

```bash
cp cookies.txt.template cookies.txt
```

Then edit `cookies.txt` and paste your cookies in this format:

```python
cookies = {
    'X-APPLE-WEBAUTH-USER': '"v=1:s=0:d=YOUR_DSID"',
    'X-APPLE-WEBAUTH-TOKEN': '"v=2:t=YOUR_TOKEN"',
    'X-APPLE-DS-WEB-SESSION-TOKEN': '"YOUR_SESSION_TOKEN"',
    # ... add all other cookies here
}
```

**How to get cookies + FULL SCRIPT TUTORIAL:** See the [video tutorial](https://youtu.be/I_if9q9gx6I) above or follow these steps:
1. Log in to https://www.icloud.com
2. Open Developer Tools (F12)
3. Go to Application/Storage tab → Cookies → `https://www.icloud.com`
4. Copy all `X-APPLE-*` cookies
5. Paste them into `cookies.txt`

### 4. Run the script

```bash
python main.py
```

## Features

* 📧 Fetch complete Hide My Email list from iCloud
* 🛑 Deactivate active Hide My Email addresses
* 🗑️ Delete Hide My Email entries
* 💾 Export email list to `emails.txt`
* 🎨 Beautiful console interface with Rich library

## Screenshots

### Console Output

![Hide My Email Manager Emails List](https://i.nuuls.com/dZfdo.png)
![Hide My Email Manager in action](https://i.nuuls.com/zL-04.png)

## Output

The script will:

1. Load your cookies from `cookies.txt`
2. Fetch all Hide My Email entries from iCloud
3. Display them in a beautiful formatted table
4. Save the list to `emails.txt`
5. Automatically deactivate active entries
6. Delete all entries (both active and inactive)

### Output File Format

The `emails.txt` file contains one entry per line:

```
anonymousId: abc123... | email: xyz@icloud.com | active: True
anonymousId: def456... | email: abc@icloud.com | active: False
```

## Prerequisites

* Python 3.7 or higher
* Apple iCloud account
* Valid iCloud session cookies

## Error Handling

The script handles:

* 🔒 Authentication failures (invalid or expired cookies)
* 🌐 Network connectivity issues
* ⏱️ API timeouts
* 📁 File I/O errors
* 🔍 Invalid cookie format
* 📊 Empty response handling

## Troubleshooting

**Cookies not working?**
- Make sure you're logged into iCloud.com
- Cookies expire - extract fresh cookies
- Ensure all required cookies are in `cookies.txt`

**No entries found?**
- Verify you have Hide My Email addresses in your iCloud account
- Check that your cookies are valid and not expired

**API errors?**
- Wait a few minutes and try again (rate limiting)
- Verify your internet connection
- Check if iCloud services are operational

## Security Notes

⚠️ **Important:**
- Never share your cookies with anyone
- Cookies expire - you may need to refresh them periodically
- `cookies.txt` is already in `.gitignore` - never commit it

## Contributing

Contributions are welcome! Feel free to:

* Report bugs
* Suggest features
* Submit pull requests

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

Having issues or questions? Please open an issue on GitHub.

## Acknowledgments

* [Rich](https://github.com/Textualize/rich) - Beautiful terminal formatting
* [Requests](https://requests.readthedocs.io/) - HTTP library for Python



