from data_structures.hashtable import Hashtable
import re

def first_repeated_word(s):
    s = s.lower()
    
    words = re.findall(r'\b\w+\b', s)
    
    word_set = set()
    
    for word in words:
        if word in word_set:
            return word
        word_set.add(word)
    
    return None



