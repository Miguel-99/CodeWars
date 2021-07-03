"""
Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
"""

def first_non_repeating_letter(string):
    a = string.lower()
    for i, _ in enumerate(a):
        if a.count(a[i])==1:
            return string[i]
    return ""


print(first_non_repeating_letter("a")) # "a"
print(first_non_repeating_letter("stress")) # "t"
print(first_non_repeating_letter("moonmen")) # "a"
print(first_non_repeating_letter("")) # ""
print(first_non_repeating_letter("abba")) # ""
print(first_non_repeating_letter("aa")) # ""
print(first_non_repeating_letter("~><#~><")) # "a"
print(first_non_repeating_letter("go hang a salami, i\'m a lasagna hog!")) # ","
print(first_non_repeating_letter("sTreSS")) # "T"
"""
test.assert_equals(first_non_repeating_letter('a'), 'a')
test.assert_equals(first_non_repeating_letter('stress'), 't')
test.assert_equals(first_non_repeating_letter('moonmen'), 'e')

test.it('should handle empty strings')
test.assert_equals(first_non_repeating_letter(''), '')

test.it('should handle all repeating strings') 
test.assert_equals(first_non_repeating_letter('abba'), '')
test.assert_equals(first_non_repeating_letter('aa'), '')

test.it('should handle odd characters')
test.assert_equals(first_non_repeating_letter('~><#~><'), '#')
test.assert_equals(first_non_repeating_letter('hello world, eh?'), 'w')

test.it('should handle letter cases')
test.assert_equals(first_non_repeating_letter('sTreSS'), 'T')
test.assert_equals(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')
"""
