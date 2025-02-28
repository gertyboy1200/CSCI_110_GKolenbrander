import re

with open ("alice_in_wonderland.txt", 'r') as file:
    lines = {line.strip() for line in file}
for text in lines:
    words = re.findall(r"\b\w+\b", text)

    print(words)
