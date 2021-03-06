# reverse a string recursively


def str_reverse(string: str) -> str:
    ''' traverse to the end of the string,
        then add add the last string to the recursion
        chain and reverse the stack
    '''
    if not string:
        return string
    return str_reverse(string[1:]) + string[0]


# print(str_reverse('the weather'))


def anagram_test(string_1: str, string_2: str) -> bool:
    '''
    Possible solutions include sort and compare - O(n log n)
    Hash map - O(n)
    ASCII counter - count should be 0 for a-z
    assuming the letters are in small case only "a-z"
    '''
    MAX_SIZE = 26
    count = [0 for _ in range(MAX_SIZE)]
    for s1, s2 in zip(string_1, string_2):
        count[ord(s1) - ord('a')] += 1
        count[ord(s2) - ord('a')] -= 1
    result = any(count) == False
    return result


# print(f"Anagram Test(fat, atf): {anagram_test('fat', 'atf')}")
# print(f"Anagram Test(fat, atg): {anagram_test('fat', 'atg')}")


def anagram_test_in_array(str_arr: set) -> bool:
    '''
    Check for anagram in an array
    Use hash map to store the characters for any set
    if any other characters in the set does not match
    then not anagram
    O(n * m)
    n = len(str_arr)
    m = len(each element within the str_arr)
    '''
    ana_hist = {s for s in str_arr.pop()}
    for v in str_arr:
        print(all(val in ana_hist for val in list(v)))


def all_suffix(suffix, string):
    if len(string) == 0:
        print(suffix)
        return
    for i in range(len(string)):
        all_suffix(suffix + string[0], string[i + 1:])


# test_data = set(['fat', 'atf', 'tdf'])
# print(f'[{test_data}]:')
# anagram_test_in_array(test_data)
word = "ababc"
all_suffix(word[0], word[1:])
