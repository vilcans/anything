anything
========

Defines the `Anything` and `Something` constants.

`Anything` compares true with any other object::

    >>> Anything == 42
    True
    >>> 'hello' == Anything
    True

You can use it to check that specific values in a data structure
have a value, but it doesn't matter what they are,
for example in a unit test::

    >>> [1, 2, 3] == [1, Anything, 3]
    True
    >>> {'x': 10, 'y': -3} == {'x': 10, 'y': Anything}
    True
    >>> {'x': 10} == {'x': 10, 'y': Anything}
    False

Inequality behaves consistently with equality::

    >>> 'hello' != Anything
    False

Even None is considered equal to Anything::

    >>> Anything == None
    True

If you want to make sure that a value is not None, use `Something`
instead::

    >>> Something == None
    False
    >>> Something == 1
    True
    >>> 1 == Something
    True
    >>> Something != None
    True
    >>> Something != 'foo'
    False

`Something` only checks for None specifically, i.e. it does not accept any
falsy value::

    >>> Something == False
    True
    >>> Something != False
    False

Equality between the two constants works as you probably expect::

    >>> Anything == Anything
    True
    >>> Something == Something
    True
    >>> Anything == Something
    True
    >>> Something == Anything
    True

Usage in Tests
--------------

Example: Creating a user and making sure its data is returned.
As the generated ID can be anything, we can't check it's value,
but this makes sure it is returned::

    import unittest

    class MyTest(unittest.TestCase):
        def test_create_user(self):
            data = create_user(name='Mary')
            self.assertEqual({
                'name': 'Mary',
                'id': Anything
            }, data)
