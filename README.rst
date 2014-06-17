anything
========

A Python constant that considers itself equal to everything else. Useful for unit testing and more.

::

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

And of course::

    >>> Anything == Anything
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
