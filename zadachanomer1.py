import json
import os
import numpy as np
import matplotlib.pyplot as plt


def f(x):
     return 100*np.sqrt(np.abs(1-0.001*x**2))+0.01*np.abs(x+10)


x = np.linspace(-15, 5, 400)
y = f(x)
data = [{"x": x, "y": y} for x, y in zip(x, y)]

if not os.path.exists('results'):
     os.makedirs('results')

with open('results/values.json', 'w') as file:
json.dump(data, file)
plt.figure(figsize=(16, 9))
plt.plot(x, y, label='f(x)', color='k')
plt.title('График')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()