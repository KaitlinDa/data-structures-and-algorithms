# Code Challenge 01 - Class 401d24

## Author
Kaitlin Davis | January 2024

## Challenge Title
Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process
![Code Challenge 2 Whiteboard Image]()

## Approach & Efficiency
My approach was to create a new array and manually copy elements from the original array, inserting the new element at the middle index. This approach does not use any built-in methods, as per the specifications.

## Solution
def insert_shift_array(arr, value):
    new_length = len(arr) + 1
    middle = new_length // 2
    new_arr = [None] * new_length
    inserted = False

    for i in range(len(arr) + 1):
        if i == middle and not inserted:
            new_arr[i] = value
            inserted = True
        elif inserted:
            new_arr[i] = arr[i - 1]
        else:
            new_arr[i] = arr[i]

    return new_arr

## Example 1
result1 = insert_shift_array([2, 4, 6, -8], 5)
print(result1)  # Output: [2, 4, 5, 6, -8]

## Example 2
result2 = insert_shift_array([42, 8, 15, 23, 42], 16)
print(result2)  # Output: [42, 8, 15, 16, 23, 42]


## Resources
I used the help of ChatGPT for this assignment.