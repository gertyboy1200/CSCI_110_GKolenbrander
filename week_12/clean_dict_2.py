import re
import string

def clean_dict(my_dict):
    """Lowercases keys and removes entries before 'a'."""
    my_dict = {k.lower(): v for k, v in my_dict.items()}
    
    # Sort keys alphabetically
    sorted_keys = sorted(my_dict.keys())
    
    # Find index where 'a' starts
    start_idx = next((i for i, key in enumerate(sorted_keys) if key >= 'a'), None)
    
    if start_idx is None:
        return {}  # No valid words found

    # Create a new dictionary with words starting from 'a'
    return {k: my_dict[k] for k in sorted_keys[start_idx:]}

def clean_list(lines):
    """Extracts words, removes punctuation, and returns a cleaned list."""
    words = []
    for line in lines:
        clean_line = re.findall(r"\b[a-zA-Z']+\b", line)  # Keeps words, removes special characters
        words.extend(clean_line)
    return words
