import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['figure.figsize'] = 5, 4

data = {1: 8, 2: 4, 3: 5, 4: 9}
x_val = [x for x in data.values()]
y_val = [y for y in data.keys()]
plt.bar(y_val, x_val)
plt.show()
