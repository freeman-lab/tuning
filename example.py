from tuning import test

test()

from numpy import loadtxt, corrcoef

X = loadtxt('test/resources/X.csv', delimiter=',')
y = loadtxt('test/resources/y.csv', delimiter=',')

#algorithm = LinearNonlinear(penalty='lasso', alpha=0, delay=0)

#model = algorithm.fit(X, y)

#model.predict(X)

import matplotlib.pyplot as plt

fig = plt.figure(figsize=[15,5])
plt.plot(X,'r')
plt.plot(y,'k')
plt.ylabel('df/f')
plt.xlabel('time (s)');
plt.show()