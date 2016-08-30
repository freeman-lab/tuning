# alex's version

from tuning import estimate_from_file
from tuning import estimate_from_array

b, r2 = estimate_from_file('file1.csv', 'file2.csv')

b, r2 = estimate_from_array(X, y)

# pandas version

from tuning import estimate

b, r2 = estimate('file1.csv', 'file2.csv')

# numpy version

from tuning import estimate
from pandas import read_csv

X = read_csv('file1.csv')
y = read_csv('file2.csv')

b, r2 = estimate(X, y)

# from numpy import loadtxt, corrcoef

# X = loadtxt('test/resources/X.csv', delimiter=',')
# y = loadtxt('test/resources/y.csv', delimiter=',')

#algorithm = LinearNonlinear(penalty='lasso', alpha=0, delay=0)

#model = algorithm.fit(X, y)

#model.predict(X)
