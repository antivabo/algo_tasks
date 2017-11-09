
def is_palindrome(word):
    """ Complexity O(n), without usage of extra memory"""
    left_position = 0
    right_position = len(word) - 1

    while left_position <= right_position:
        while not word[left_position].isalnum():
            left_position += 1
        while not word[right_position].isalnum():
            right_position -= 1
        if not word[left_position].lower() == word[right_position].lower():
            return False
        else:
            left_position += 1
            right_position -= 1
    return True


positive_test_cases = ['_!E#@y#e',
                       'MaDaM!!',
                       'RaCEC@A@R',
                       'A@@@$1ds1sd1A']
negative_test_cases = ['aA$$$d$^^5a',
                       'A$B%$%%$c%',
                       'any%%other^^']


def test_is_palindrome():
    for test in positive_test_cases:
        try:
            assert is_palindrome(test)
        except AssertionError:
            print 'Error in positive case: %s' % test
    for test in negative_test_cases:
        try:
            assert not is_palindrome(test)
        except AssertionError:
            print 'Error in negative case: %s' % test


if __name__ == '__main__':
    test_is_palindrome()

