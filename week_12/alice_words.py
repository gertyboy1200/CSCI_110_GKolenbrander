import string
import re
import clean_dict_2

my_dict = {}

with open ("alice_in_wonderland.txt", 'r') as file:
    lines = file.readlines()


lines = clean_dict_2.clean_list(lines)

    
 
for word in lines:
    if word in my_dict:
        my_dict[word] += 1
        continue
    else:
        my_dict[word] = 1
            

         
my_dict = clean_dict_2.clean_dict(my_dict)

for key in sorted(my_dict):
    print(f"{key} : {my_dict[key]}")