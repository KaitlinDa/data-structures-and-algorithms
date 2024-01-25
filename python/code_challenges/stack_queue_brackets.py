from data_structures.queue import Queue


def multi_bracket_validation(input_string):
    bracket_map = {")": "(", "}": "{", "]": "["}
    open_brackets = set(["(", "{", "["])
    stack = []

    for char in input_string:
        if char in open_brackets:
            stack.append(char)
        elif char in bracket_map:
            if not stack or bracket_map[char] != stack.pop():
                return False

    return not stack  
