<h1 align="center">🕵️‍♂️ Auto-OSINT Toolkit</h1>
<p align="center">
  Automated Open-Source Intelligence gathering tool built with Python.<br>
  Investigate IPs, Emails, and Usernames with integrated APIs and visual graphs.
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
  <a href="https://github.com/Anandhan-2253/Auto-OSINT">
    <img src="https://img.shields.io/badge/GitHub-Anandhan--2253%2FAuto--OSINT-black?logo=github" alt="GitHub Repo">
  </a>
</p>

<hr>

<h2>✨ Features</h2>
<ul>
  <li>🌍 <b>IP Intelligence</b> – GeoIP, WHOIS, Reverse DNS, Shodan lookup</li>
  <li>📧 <b>Email OSINT</b> – Breach check &amp; validation</li>
  <li>👤 <b>Username OSINT</b> – Cross-platform search</li>
  <li>📁 <b>Export Reports</b> – JSON with timestamps</li>
  <li>🎨 <b>Rich CLI Output</b> – Colorful and interactive tables</li>
</ul>

<hr>

<h2>📦 Installation</h2>
<pre>
# Clone the repository
git clone https://github.com/Anandhan-2253/Auto-OSINT.git
cd Auto-OSINT

# Create a virtual environment (optional)
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
</pre>

<hr>

<h2>🚀 Usage</h2>
<pre>
# IP OSINT
python main.py --ip &lt;IP_ADDRESS&gt;

# Email OSINT
python main.py --email &lt;EMAIL_ADDRESS&gt;

# Username OSINT
python main.py --username &lt;USERNAME&gt;

# With API keys
python main.py --ip &lt;IP&gt; --shodan &lt;SHODAN_API_KEY&gt;
python main.py --email &lt;EMAIL&gt; --hibp &lt;HIBP_API_KEY&gt;
</pre>

<hr>

<h2>🖥 Example Output</h2>
<p><b>IP Lookup</b></p>
<pre>
Performing IP OSINT on 8.8.8.8...
[Table with geolocation, WHOIS, reverse DNS]
</pre>

<p><b>Email Breach Check</b></p>
<pre>
Breached in 3 data breaches:
 - Adobe
 - Dropbox
 - LinkedIn
</pre>

<p><b>Username Search</b></p>
<pre>
[+] Found on GitHub: https://github.com/johndoe
[-] Not Found on Twitter
</pre>

<p>📁 <b>Report saved to:</b> reports/osint_report_YYYYMMDD_HHMMSS.json</p>

<hr>

<h2>🔑 API Keys</h2>
<ul>
  <li><a href="https://account.shodan.io/register">Shodan API</a> (Free tier available)</li>
  <li><a href="https://haveibeenpwned.com/API/Key">HaveIBeenPwned API</a> (Paid)</li>
  <li><b>Alternative:</b> <a href="https://dehashed.com/">Dehashed API</a> (Limited free usage)</li>
</ul>

<hr>

<h2>⚠️ Disclaimer</h2>
<blockquote>
This tool is for <b>educational and ethical security testing purposes only</b>.<br>
Do <b>NOT</b> use for illegal activities.<br>
The author assumes <b>no responsibility</b> for misuse.
</blockquote>

<hr>

<h2>📜 License</h2>
<p>Licensed under the <a href="LICENSE">MIT License</a>.</p>
