#gradient_descent.m
#Gradient descent for Octave

function [theta] = gradientDescent(X, y, alpha)

theta = theta - (alpha*(1/m)*sum(X.*(X*theta-y)))'
