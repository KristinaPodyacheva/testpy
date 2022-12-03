import pytest
def reverse(s):
    if type(s) != str:
        raise TypeError('jj'.format(type(s)))
    return s [::-1]
