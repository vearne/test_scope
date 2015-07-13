from base import value
from b import hello

print dir()
print 'scope base', value, id(value)
value = 20
print dir()
print 'scope local', value, id(value)
hello()
