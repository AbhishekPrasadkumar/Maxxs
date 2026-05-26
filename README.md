# MA-xss
# XSS Vulnerability Scanner

This is a Python-based tool that scans websites for **Cross-Site Scripting (XSS)** vulnerabilities. It identifies potential XSS vulnerabilities by submitting common XSS payloads to forms and analyzing responses.

## Features

- **XSS Payload Injection:** Uses common XSS payloads to test if input fields are vulnerable to script injection.
- **Form Scanning:** Automatically detects forms on webpages and tests them for XSS vulnerabilities.
- **Website Crawling:** Crawls through the links of a given website and scans all reachable pages for XSS vulnerabilities.
- **Scan Reports:** Generates a detailed report of all discovered vulnerabilities with payloads used.

---

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

To install the necessary dependencies, run:

```bash
pip install requests beautifulsoup4
```

---

## Usage

### 1. Clone this repository:

```bash
git clone https://github.com/AbhishekPrasadkumar/xss-scanner.git
cd xss-scanner
```

### 2. Run the script:

```bash
python xss_scanner.py
```

### 3. Enter the URL of the website you wish to scan when prompted.

Example:

```
Enter the URL to scan: https://example.com
```

### 4. The tool will:

- Crawl the target website
- Scan webpages and detect forms
- Submit XSS payloads
- Analyze responses for vulnerabilities
- Generate a scan report

### 5. The report will be saved as:

```
xss_scan_report.txt
```

---

## Example Output

```
Enter the URL to scan: https://example.com

🔍 Crawling website to find pages...
 - Found page: https://example.com/contact
 - Found page: https://example.com/search

🔍 Scanning https://example.com/contact (contact) for XSS vulnerabilities...

✅ Potential XSS vulnerability detected:
   URL     : https://example.com/contact
   Form    : contact
   Payload : <script>alert('XSS')</script>

🔍 Scanning https://example.com/search (search) for XSS vulnerabilities...

✅ Potential XSS vulnerability detected:
   URL     : https://example.com/search
   Form    : search
   Payload : <img src=x onerror=alert(1)>

📄 Scan report saved as xss_scan_report.txt
✅ Scan complete. 2 vulnerabilities found across 2 pages.
```

---

## Report Format

The generated report contains a list of found XSS vulnerabilities, including:

- Vulnerability location
- URL affected
- Payload used
- Detection details

Example:

```text
XSS Vulnerability Scan Report
Target : https://example.com
Date   : 2026-05-26
==================================================

Vulnerability Location : Contact Form
URL                    : https://example.com/contact
Payload                :
<script>alert('XSS')</script>

--------------------------------------------------

Vulnerability Location : Search Form
URL                    : https://example.com/search
Payload                :
<img src=x onerror=alert(1)>

--------------------------------------------------

Total Vulnerabilities Found : 2
Pages Scanned               : 2
```

---

## Project Structure

```
xss-scanner/
│
├── xss_scanner.py        # Main scanner script
├── payloads.txt          # XSS payload wordlist (optional override)
├── xss_scan_report.txt   # Auto-generated scan output
└── README.md             # This file
```

---

## Disclaimer

⚠️ This tool is intended for **educational purposes and authorized security testing only**. Use this scanner only on systems that you own or have **explicit written permission** to test.

Unauthorized scanning of systems may violate laws and regulations. The author assumes **no liability** for any misuse of this tool.

---

## Contributing

Feel free to open issues or submit pull requests if you'd like to contribute to this project.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add: your feature'`
4. Push to your branch: `git push origin feature/your-feature`
5. Open a Pull Request with a clear description of your changes
