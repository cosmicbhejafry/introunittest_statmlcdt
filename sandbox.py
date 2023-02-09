from inflammation.models import daily_mean, daily_max
import numpy as np

# print(daily_max(np.array([[1, 2], [3, 4], [5, 6]])))
# print(daily_max(np.array([[1, 2], [2, 1], [5, 6]])))

# assert np.array_equal(np.array([0, 0]), daily_mean(np.array([[0, 0], [0, 0]])))
# assert np.array_equal(np.array([3, 4]), daily_mean(np.array([[1, 2], [3, 4], [5, 6]])))
# assert np.array_equal(np.array([2, 4]), daily_mean(np.array([[1, 2], [3, 4], [5, 6]])))