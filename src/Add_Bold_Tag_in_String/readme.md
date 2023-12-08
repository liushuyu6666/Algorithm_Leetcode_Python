# types
## string
### find index of substring
### string rearrangement

# caveats
## string
### find index of substring
To find multiple indices of a substring, instead of slicing the original string, we should update the start index of the `find` function. Here's the corrected approach in Python:
```python
s, word = "abceeabc", "abc"
find_index = s.find(word, 0)

while find_index != -1:
    find_index = s.find(word, find_index + 1)  # Update the start index
    # find_index = s[find_index + 1: ].find(word) # wrong. Explanation: After finding the first occurrence of the substring, the expression becomes "bceeabc".find("abc"), which may lead to incorrect results.
```
In the corrected code, we increment the start index for each iteration to find all occurrences of the substring within the string.