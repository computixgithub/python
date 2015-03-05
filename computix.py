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

def collect_vowels(s):
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

def up_to_vowel(s):
    '''(str) -> str

    Return a substring of s. The substring starts from
    the beginning of s and includes the last consonant
    before the first vowel is reached.
    
    >>> up_to_vowel('Hello')
    'H'
    >>> up_to_vowel('My name is COMPUTIX')
    'My n'
    >>> up_to_vowel('Xyz')
    'Xyz'
    >>> up_to_vowel('I like bread.')
    ''
    '''

    i = 0
    string = ''
    
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        string = string + s[i]
        i = i + 1

    return string
