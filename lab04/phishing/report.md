# Lab04(Additional material) — Phishing Simulation (Banking page)

## What I built
- A local simulated banking login page `bank_login.html` served by `server.py` (Flask).
- The page collects username/password/CVV and writes to `login_data.txt` (simulation only).

## How to run 
1. Create virtualenv and install deps:
   $ python3 -m venv venv
   $ source venv/bin/activate
   $ pip install -r requirements.txt
2. Run the server:
   $ python3 server.py
3. Open browser on the lab machine to:
   http://127.0.0.1:8080

## Detection indicators (what would alert defenders)
- Unexpected email or link prompting login.
- Domain mismatch (hover link shows different host).
- SSL certificate problems (self-signed).
- Content asking for payment/CVV when not needed.
- Unusual network connections to external or unknown hosts.

## Defense strategies
- Multi-factor authentication (MFA) to reduce credential reuse risk.
- Email filtering and secure email gateways with link rewriting.
- SPF/DKIM/DMARC to protect sending domains.
- Employee awareness training and phishing tests.
- Browser-based protections and domain blacklists.

## Safety
All data in `login_data.txt` are test values only and the lab is local.

