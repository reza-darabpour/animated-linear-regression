# Linear Regression Animation using Gradient Descent

This repository contains a Python implementation of **Linear Regression** trained using **Gradient Descent**. The project visualizes how the regression line gradually fits the data points through an animation.

The main goal of this project is to demonstrate the learning process of a simple linear regression model in an intuitive and visual way.

## Overview

Linear regression is a basic machine learning method used to model the relationship between an independent variable and a dependent variable. In this project, the model tries to find the best-fitting straight line for a given set of data points.

The line equation is:

```text
y = b0 + b1x
```

where:

* `b0` is the intercept
* `b1` is the slope
* `x` is the input variable
* `y` is the predicted output

The model updates `b0` and `b1` using gradient descent in order to minimize the Mean Squared Error (MSE).

## Objective

The objective of this project is to show how gradient descent changes the regression line step by step until it fits the data points better.

## Features

* Python implementation of simple linear regression
* Gradient descent optimization
* Mean Squared Error calculation
* Iterative update of slope and intercept
* Animation of the regression line fitting process
* Visualization of data points and fitted line
* Convergence check using tolerance

## Project Structure

```text
linear-regression-gradient-descent-animation/
│
├── linear_regression_animation.py
├── requirements.txt
└── README.md
```

## File Description

* `linear_regression_animation.py`: Main Python script that performs linear regression using gradient descent and displays the fitting process as an animation.
* `requirements.txt`: List of required Python packages.
* `README.md`: Project description and usage instructions.

## Requirements

This project requires Python 3.

Required Python packages:

```text
numpy
matplotlib
```

You can install the required packages using:

```bash
pip install -r requirements.txt
```

## How to Run

After downloading or cloning the repository, run the Python script:

```bash
python linear_regression_animation.py
```

On Windows, you can also run:

```bash
py linear_regression_animation.py
```

## How It Works

The program starts with initial values for the regression parameters:

```text
b0 = 8
b1 = 8
```

Then, for each iteration:

1. The predicted values are calculated.
2. The Mean Squared Error is computed.
3. The gradients for `b0` and `b1` are calculated.
4. The parameters are updated using gradient descent.
5. The updated regression line is stored.
6. The animation shows how the line changes over time.

The algorithm stops when either the maximum number of epochs is reached or the change in loss becomes smaller than the defined tolerance.

## Output

The program displays:

* The final values of the regression coefficients
* The convergence information, if convergence is reached
* An animated plot showing how the regression line fits the data points

Example output:

```text
Converged at iteration 243 with loss = 1.234567
Final coefficients: b0 = 0.85, b1 = 1.95
```

The exact output may vary depending on the learning rate, initial values, and stopping conditions.

## Visualization

The animation shows the regression line moving gradually toward the best-fitting position. The red markers represent the original data points, and the blue line represents the regression line being updated during training.

This visualization helps explain how gradient descent improves the model step by step.

## Applications

This project can be useful for:

* Learning linear regression
* Understanding gradient descent
* Visualizing model training
* Educational machine learning demonstrations
* Python plotting and animation practice

## Author

Reza Darabpour

## License

This project is provided for educational and learning purposes.
