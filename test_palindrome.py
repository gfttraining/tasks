from palindrome import isPalindrome

def test_palindrome():

    '''
        >>> isPalindrome('')
        True
        >>> isPalindrome('a')
        True
        >>> isPalindrome('_!E#@y#e')
        True
        >>> isPalindrome('baa')
        False
        >>> isPalindrome('RMaDaM!!')
        True
        >>> isPalindrome('baaRb')
        False
        >>> isPalindrome('RaCEC@A@R')
        True
        >>> isPalindrome('!!eY#%@e!@!')
        True
        >>> isPalindrome('noon')
        True
        >>> isPalindrome('ab'*2)
        False
        >>> x = 'ab' *2**20
        >>> len(x)
        2097152
        >>> xreversed = x[::-1]
        >>> isPalindrome(x+xreversed)
        True
        >>>
    '''

def _test():
    import doctest
    doctest.testmod()
    doctest.testmod(verbose=True)

if __name__ == "__main__":
    _test()

