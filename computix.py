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
    >>> kjup_to_vowel('I like bread.')
    ''
    '''

    i = 0
    string = ''
    
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        string = string + s[i]
        i = i + 1

    return string

def ask_user(prompt):
    '''(str) -> str

    Use prompt to ask the user for a "yes" or "no"
    answer and continue asking until the user gives
    a valid response. Return the answer.
    '''
    
    answer = input(prompt)

    while not (answer == 'yes' or answer == 'Yes' or answer  == 'no' or answer == 'No'):
        answer = input(prompt)

    return answer

def find_neighbour(s):
    '''(str) -> str

    Return the equal neighbouring elements of string s.
    
    >>> find_neighbour('abbccdeffg')
    'bcf'
    >>> find_neighbour('abc')
    ''
     '''

    # Define the accumulator.
    string = ''
    
    for i in range(len(s) - 1):
        if s[i + 1] == s[i]:
            string = string + s[i + 1]

    return string
        
def shift_left(L):
    '''(list) -> NoneType

    Shift each item in list L one position to the left
    and shift the first item to the last position.

    Precondition: len(L) >= 1
    '''

##    first_item = L[0]
##
##    for i in range(len(L) - 1):
##        L[i] = L[i + 1]
##
##    L[-1] = first_item
##
##    print(L)

    # With methods.
    first_item = L.pop(0)
    L.append(first_item)
    print(L)

def sum_numbers(list1, list2):
    '''(list of number, list of number) -> list of number

    Return a new list in which each item is the sum of the
    numbers at the corresponding position of list1 and list2.

    Precondition: len(list1) == len(list2)

    >>> sum_numbers([1, 4, 9], [5, 10, 20])
    [6, 14, 29]
    >>> sum_numbers([1.3, 7, 9.4], [2.4, 3.9, 6.2])
    [3.7, 10.9, 15.6]
    '''

    new_list = []

    for i in range(len(list1)):
        summe = list1[i] + list2[i]
        new_list.append(summe)

    return new_list

def count_matches(s1, s2):
    '''(str, str) -> int

    Return the number of positions in s1 that contain
    the same character at the corresponding position of s2.

    Precondition: len(s1) == len(s2)

    >>> count_matches('ate', 'ape')
    2
    >>> count_matches('head', 'hard')
    2
    >>> count_matches('nope', 'pope')
    3
    >>> count_matches('Hello', 'Going')
    0
    '''

    num_matches = 0

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1

    return num_matches
