# tuning

compute linear and nonlinear tuning curves

## install

use pip

## example

from tuning import estimate_from_array

X = 1
y = 2

b, r2 = estimate_from_array(X, y)

print('b:%s' % b)
print('r2:%s' % r2)


## describe