#gradient_descent.m
#Gradient descent for Octave
#theta: column vector, X: matrix, alpha: real, Y: column vector
function [theta] = gradientDescent(X, y, alpha) #returns theta, a column vector

theta = theta - (alpha*(1/m)*sum(X.*(X*theta-y)))'
#result of sum(X.*(X*theta-y)) is a row vector of 1 row and n columns (where n = number of features)
