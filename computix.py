def is_even(num):
    '''(num) -> bool

    Return whether num is even.
    
    >>> is_even(4)
    True
    >>> is_even(7)
    False
    >>> is_even(17.63)
    False
    >>> is_even(12.0)
    True
    >>> is_even(0)
    True
    '''

    return num % 2 == 0
def num_vowels(s):   
    '''(str) -> int

    Return the number of vowels in s.
    
    >>> num_vowels('Hello')
    2
    >>> num_vowels('MKV')
    0
    >>> num_vowels('Aeiou')
    5
    '''

    num_vowels = 0
    
    for char in s:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1

    return num_vowels

def collecht_vowels(s):
    '''(str) -> str

    Return the vowels of s.
    
    >>> collect_vowels('Hello')
    'eo'
    >>> collect_vowels('MKV')
    ''
    >>> collect_vowels('My name is Earl!')
    'aeiEa'
    >>> collect_vowels("It's raining again, but the sun will come back :-)")
    'Iaiiaaiueuioea'
    '''

    string = ''

    for char in s:
        if char in 'aeiouAEIOU':
            string = string + char

    return string
