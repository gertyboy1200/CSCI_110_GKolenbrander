import re
def clean_dict(my_dict):

    my_dict=  {k.lower(): v for k, v in my_dict.items()}

    keys = list(my_dict.keys())
    keys = sorted(keys)
    value = 0
    for i in range(len(keys)):
        if keys[i] == 'a':
            value = i
            break

    for j in range(value):
        del my_dict[keys[j]]

    return(my_dict)

def clean_list(lines):
    value = []
    for line in lines:
        words = re.findall(r"\b\S+\b", line) 
        for word in words:
            value.append(word)
    return value