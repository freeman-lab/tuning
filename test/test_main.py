from tuning import estimate_from_array

def test_b():
  X = 1
  y = 2
  b, r2 = estimate_from_array(X, y)
  assert b == 3

def test_r2():
  X = 1
  y = 2
  b, r2 = estimate_from_array(X, y)
  assert r2 == -1