
import itertools
import sys

if len(sys.argv) < 4:
    print("Usage: python3 generate_wordlist.py <name> <surname> <dob> [outfile]")
    sys.exit(1)

name, surname, dob = sys.argv[1], sys.argv[2], sys.argv[3]
outfile = sys.argv[4] if len(sys.argv) > 4 else "custom-passwords.txt"


parts = [name.capitalize(), name.lower(), surname.capitalize(), surname.lower(), dob]
extras = ['123', '1234', '12345', '!', '@', '2020', '2021', '01', '07']

candidates = set()


for p in parts:
    candidates.add(p)


for a, b in itertools.product(parts, extras):
    candidates.add(a + b)


for a, b in itertools.product(parts, parts):
    candidates.add(a + b)


with open(outfile, 'w') as f:
    for pwd in sorted(candidates):
        f.write(pwd + '\n')

print(f'Wrote {len(candidates)} passwords to {outfile}')
