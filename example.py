from tuning import estimate

b, r2 = estimate(X, y)

# from numpy import loadtxt, corrcoef

# X = loadtxt('test/resources/X.csv', delimiter=',')
# y = loadtxt('test/resources/y.csv', delimiter=',')

#algorithm = LinearNonlinear(penalty='lasso', alpha=0, delay=0)

#model = algorithm.fit(X, y)

#model.predict(X)
