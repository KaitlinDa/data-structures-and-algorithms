from data_structures.hashtable import Hashtable


def left_join(synonyms, antonyms):
    result = []
    
    for key, value in synonyms.items():
        if key in antonyms:
            antonym = antonyms[key]
        else:
            antonym = "NONE"
        
        result.append([key, value, antonym])
    
    return result

