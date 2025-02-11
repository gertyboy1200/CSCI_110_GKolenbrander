with open('war_and_peace.txt', 'r') as file:
    text = [line.strip() for line in file]

words = []

for line in text:
    lines = line.split()
    words.append(lines)

total_words_with_e = 0
total_words = 0

for line in words:
    for word in line:
        total_words += 1
        for letter in word:
            if letter == 'e' or letter == 'E':
                total_words_with_e += 1
                continue

print("your text contains", total_words, "of which", total_words_with_e, "(", int((total_words_with_e/total_words) * 1000) /10, "%) contain and 'e' ")