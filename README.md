# MA-xss
A Python-based security tool designed to detect potential Cross-Site Scripting (XSS) vulnerabilities in web applications. The scanner automatically crawls websites, discovers forms, injects common XSS payloads, and analyzes responses to identify possible vulnerabilities.

Features
XSS Payload Testing
Injects commonly used XSS payloads into input fields to detect script injection vulnerabilities.
Automated Form Detection
Identifies forms across webpages and tests input fields for potential XSS flaws.
Website Crawling
Crawls and explores website links to scan all reachable pages.
Vulnerability Reporting
Generates a detailed report containing discovered vulnerabilities, affected URLs, and payloads used during testing.
Requirements
Python 3.x
requests
beautifulsoup4

Install dependencies using:

pip install requests beautifulsoup4
Installation

Clone the repository:

git clone https://github.com/yourusername/xss-scanner.git
cd xss-scanner
Usage

Run the scanner:

python xss_scanner.py

Enter the target website URL when prompted:

Enter the URL to scan: https://example.com

The tool will:

Crawl the target website
Discover forms and input fields
Inject XSS payloads
Analyze responses for vulnerabilities
Generate a scan report
Example Output
Enter the URL to scan: https://example.com

🔍 Crawling website to find pages...
 - Found page: https://example.com/contact

🔍 Scanning https://example.com/contact (contact) for XSS vulnerabilities...

✅ Potential XSS vulnerability detected:
URL: https://example.com/contact
Payload: <script>alert('XSS')</script>

📄 Scan report saved as xss_scan_report.txt
Report Format

The generated report (xss_scan_report.txt) contains:

Vulnerable page or form location
Target URL
Successful payload used
Details of detected vulnerabilities

Example:

XSS Vulnerability Scan Report
==================================================

Vulnerability Location: Contact Form
URL: https://example.com/contact

Payload:
<script>alert('XSS')</script>
Disclaimer

This tool is intended for educational purposes and authorized security testing only. Use it only on systems and applications you own or have explicit permission to test. Unauthorized scanning of third-party systems may violate laws or terms of service.

Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.
