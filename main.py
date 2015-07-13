from base import value
from b import hello
print 'scope base', value, id(value)
value = 20
print 'scope local', value, id(value)
hello()
