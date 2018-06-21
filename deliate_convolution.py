from keras.layers import Conv2D, Convolution2D
import math
import matplotlib.pyplot as plt


def changeable_learningrate(iter_, max_iter, base_lr, power):
    return math.pow((1-float(iter_/max_iter)), power)*base_lr


learning_rate_list = []
for iter_ in range(150*1000):
    learning_rate = changeable_learningrate(iter_, max_iter=150*1000, base_lr=0.01, power=0.9)
    learning_rate_list.append(learning_rate)

plt.plot(range(150*1000), learning_rate_list, 'g-')
plt.show()
print(learning_rate_list[-1])
