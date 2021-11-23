# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels (but not y).
# The input string will only consist of lower case letters and/or spaces.
# Input = "hello world"
# Output = 3

def num_of_vowels(str):
    count = 0
    vowel = "aeiou"
    for a in helloworld:
        if a in vowel:
            count += 1
        return count

helloworld = "hello world"
print(num_of_vowels(helloworld))

#or 
def num_of_vowels(str):
    vowels = "aeiou"
    ans = len([x for x in str if x in vowels])
    return ans
    
#or
def count_vowels(string):
    return sum(l in 'aeiou' for l in string)
