from pandas import read_csv

def estimate_from_file(file1, file2):
  X = read_csv(file1)
  y = read_csv(file2)
  b, r2 = estimate_from_array(X, y)
  return b, r2

def estimate_from_array(X, y):
  b = X + y
  r2 = X + y
  return b, r2