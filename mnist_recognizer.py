# -*- coding: utf-8 -*-
"""MNIST recognizer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OAQjVxomKqomrOpq151PnHLMgwCyaSnC
"""

from __future__ import absolute_import, division, print_function
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import mnist
(training_img, training_labels), (dev_img, dev_labels) = mnist.load_data()

#hyperparameters

learning_rate = 0.01
t_iteration = 30
batch_size = 100
disp_step = 2

#preprocessing, "normalize" inputs. Now each pixel is value from 0 to 1
training_img = training_img / 255
dev_img = dev_img / 255

print(training_labels)

training_img = training_img.reshape(training_img.shape[0], -1).T
training_labels = training_labels.reshape(training_labels.shape[0], -1).T
dev_img = dev_img.reshape(dev_img.shape[0], -1).T
dev_labels = dev_labels.reshape(dev_labels.shape[0], -1).T

n_x = 784 # 28 x 28 = 784 - size of single input 
n_y = 10 #no. of classes

X = tf_placeholder(tf.float32, [n_x, None], name = "X")
Y = tf_placeholder(tf.float32, [n_y, None], name = "Y")

#He / MRSA initialization
W1 = tf.get_variable("W1", [25, 12288], initializer = tf.contrib.layers.variance_scaling_initializer(dtype=tf.float32))
b1 = tf.get_variable("b1", [25, 1], initializer = tf.zeros_initializer())
W2 = tf.get_variable("W2", [12, 25], initializer = tf.contrib.layers.variance_scaling_initializer(dtype=tf.float32))
b2 = tf.get_variable("b2", [12, 1], initializer = tf.zeros_initializer())
W3 = tf.get_variable("W3", [6, 12], initializer = tf.contrib.layers.variance_scaling_initializer(dtype=tf.float32))
b3 = tf.get_variable("b3", [6, 1], initializer = tf.zeros_initializer())

def forwardProp():
  Z1 = tf.matmul(W1, X) + b1
  A1 = tf.nn.relu(Z1)
  Z2 = tf.matmul(W2, A1) + b2
  A2 = tf.nn.relu(Z2)
  Z3 = tf.matmul(W3, A2) + b3
  return Z3

