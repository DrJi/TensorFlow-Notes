"""
Simple linear regression example in TensorFlow
This program tries to predict the number of thefts from
the number of fire in the city of Chicago
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

DATA_FILE = './data/fire_theft.xls'

# Phase 1: Assemble the graph
# Step 1: read in data from the .xls file
book = xlrd.open_workbook(DATA_FILE, encoding_override='utf-8')
sheet = book.sheet_by_index(0)
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)])
n_samples = sheet.nrows - 1

# Step 2: create placeholders for input X (number of fire) and label Y (number of theft)

X = tf.placeholder(dtype=tf.float32, name='X')
Y = tf.placeholder(dtype=tf.float32, name='Y')

# Step 3: create weight and bias, initialized to 0
# name your variables w and b
w = tf.Variable(0.0, name='weights')
b = tf.Variable(0.0, name='bias')


# Step 4: predict Y (number of theft) from the number of fire
# name your variable Y_predicted
Y_pred = X * w + b

# Step 5: use the square error as the loss function
# name your variable loss
loss = tf.square(Y-Y_pred)
# Step 6: using gradient descent with learning rate of 0.01 to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

# Phase 2: Train our model
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./my_graph/linear_regression', sess.graph)
    for i in range(100):
        total_loss = 0
        for x, y in data:
            _, l = sess.run([optimizer, loss], feed_dict={X: x, Y:y})
            total_loss += l
        print("Epoch {0}: {1}".format(i, total_loss/n_samples))

# plot the results

# Each time when I try to run the plot
# there is an error:
# 'Tensor' object has no attribute 'ndim'

# X, Y = data.T[0], data.T[1]
# plt.plot(X, Y, 'bo', label='Real data')
# plt.plot(X, X * w + b, 'r', label='Predicted data')
# plt.legend()
# plt.show()
