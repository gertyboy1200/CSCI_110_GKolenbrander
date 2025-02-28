my_dict = {}
import string


with open ("alice_in_wonderland.txt", 'r') as file:
    lines = {line.strip() for line in file}

for line in lines:
    for word in line.split():
        if word in my_dict:
            my_dict[word] += 1
            continue
        else:
            my_dict[word] = 1
            
            
my_dict=  {k.lower(): v for k, v in my_dict.items()}

keys = list(my_dict.keys())
keys = sorted(keys)
value = 0
for i in range(len(keys)):
    if keys[i] == 'a':
        value = i
        break

print(value)

for j in range(value):
    del my_dict[keys[j]]


print(sorted(my_dict))