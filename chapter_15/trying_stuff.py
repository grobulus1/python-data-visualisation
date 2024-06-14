import math
import matplotlib.pyplot as plt


def calculate_1(size):
    i = 0
    result = []
    while i < size:
        result.append(math.sin(i * 0.01))  # Use smaller steps
        i += 1
    return result


y = calculate_1(1000)
x = [i * 0.01 for i in range(1000)]  # Match the x values with the steps
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(x, y)  # Use plot instead of scatter for a smooth line
plt.show()
