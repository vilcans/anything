"""
Defines the `Anything` constant that compares true with any other object.

>>> Anything == 42
True
>>> 'hello' == Anything
True

You can use it to check that specific values in a data structure
have a value, but it doesn't matter what they are,
for example in a unit test:

>>> [1, 2, 3] == [1, Anything, 3]
True
>>> {'x': 10, 'y': -3} == {'x': 10, 'y': Anything}
True
>>> {'x': 10} == {'x': 10, 'y': Anything}
False

Inequality behaves consistently with equality:

>>> 'hello' != Anything
False

Even None is considered equal to Anything:

>>> Anything == None
True

And of course:

>>> Anything == Anything
True
"""

__all__ = ['Anything']


class AnythingType(object):
    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return False

    def __repr__(self):
        return 'Anything'

Anything = AnythingType()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
