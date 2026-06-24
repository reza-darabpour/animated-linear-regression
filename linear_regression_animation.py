import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


x_data = np.array([0.8, 1.5, 2.5, 3, 4, 5, 6])
y_data = np.array([1, 3, 4, 6.5, 7.3, 12, 11.5])

tolerance = 1e-6
b0_list = []
b1_list = []
loss_list = []
b0 = 8
b1 = 8
learning_rate = 0.02
epochs = 500
n = len(x_data)

for i in range(epochs):
    y_pred = b0 + b1 * x_data
    loss = np.mean((y_pred - y_data) ** 2)  #  MSE
    loss_list.append(loss)

    d_b0 = np.sum(y_pred - y_data) / n
    d_b1 = np.sum((y_pred - y_data) * x_data) / n
    temp0 = b0 - learning_rate * d_b0
    temp1 = b1 - learning_rate * d_b1
    b0=temp0
    b1=temp1
    b0_list.append(temp0)
    b1_list.append(temp1)

    if i > 0 and abs(loss_list[i] - loss_list[i - 1]) < tolerance:
        print(f"Converged at iteration {i+1} with loss = {loss:.6f}")
        break


print(f"Final coefficients: b0 = {b0}, b1 = {b1}")

X = np.linspace(0, 7, 100)

fig, ax = plt.subplots()
# fig.set_tight_layout(True)

ax.scatter(x_data, y_data, color='r',marker='+', label='Data points')
line, = ax.plot(X, b0 + b1 * X, 'b-', linewidth=2, label='Regression line')
ax.legend()

def update(frame):
    line.set_ydata(b0_list[frame] + b1_list[frame] * X)
    return line,

anim = FuncAnimation(fig, update, frames=len(b0_list), interval=50, repeat=False)

plt.show()
