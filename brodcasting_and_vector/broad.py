import numpy as np

discount = 10
prices = np.array([100, 200, 300])

final_prices = prices - (prices * discount / 100)

print(final_prices)

