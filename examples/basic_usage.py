import numpy as np
from pydaggerjl import daggerjl

# Create a Dagger DTask to sum the elements of an array
task = daggerjl.spawn(np.sum, np.array([1, 2, 3]))

# Wait on task to finish
# This is purely educational, as fetch will wait for the task to finish
daggerjl.wait(task)

# Fetch the result
result = daggerjl.fetch(task)

print(f"The sum is: {result}")

# Create two numpy arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise sum of the two arrays
task = daggerjl.spawn(np.add, a, b)

# Fetch the result
result = daggerjl.fetch(task)

print(f"The element-wise sum is: {result}")

# Element-wise sum of last result with itself
task2 = daggerjl.spawn(np.add, task, task)

# Fetch the result
result2 = daggerjl.fetch(task2)

print(f"The element-wise sum of the last result with itself is: {result2}")
