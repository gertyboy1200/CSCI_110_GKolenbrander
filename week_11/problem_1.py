with open ("problem_1.txt", 'r') as file:
    lines = [line.strip() for line in file]  #removes newline character


for line in lines:  #prints the original text
    print(line)

i = len(lines) - 1  #finds the length of the  list

while(i >= 0):  #starts at the end of the list
    print(lines[i])
    i -= 1  #incrments backwards to the begginning of the list
