# Linear Regression from Scratch with Batch Gradient Descent

This repository contains basic implementations of Linear Regression models from scratch using Python. The models are built without relying on any machine learning libraries, showcasing the underlying mathematics and algorithms.

## Description

In this project, we compute the parameters of the Linear Regression model using Batch Gradient Descent.

## Files

- `batch_gradient_descent.ipynb`: Jupyter Notebook demonstrating the implementation and usage of the Linear Regression model with Batch Gradient Descent.
- `batch_gradient_descent_class.ipynb`: Jupyter Notebook containing a class-based implementation of Linear Regression using Batch Gradient Descent.
- `Equations`: A folder containing some of the basic equations used.
- `README.md`: Documentation of the project.

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Basic knowledge of Linear Regression and Python programming

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/cjpaine109/ai-notebooks.git
    cd ai-notebooks
    ```

2. **Install necessary packages**:
    Make sure you have the required Python packages installed. You can use `pip` to install them:
    ```bash
    pip install numpy pandas matplotlib
    ```

3. **Open Jupyter Notebook**:
    ```bash
    jupyter notebook
    ```

### Usage

1. **Navigate to the project directory**:
    ```bash
    cd Batch_Gradient_Descent_Linear_Regression
    ```

2. **Open the Jupyter Notebooks**:
    Open `batch_gradient_descent.ipynb` or `batch_gradient_descent_class.ipynb` in Jupyter Notebook to run and explore the code.

## Explanation of Batch Gradient Descent

Batch Gradient Descent is used to find the optimal parameters (theta) that minimize the cost function in Linear Regression. The iterative optimization algorithm updates the parameters using the following update rule:

$\theta := \theta - \alpha \frac{1}{m} X^T (X \theta - y)$

where:
- \(theta) is the vector of parameters.
- \(alpha) is the learning rate.
- \(X\) is the matrix of input features.
- \(y\) is the vector of output values.
- \(m\) is the number of training examples.

This method iteratively updates the parameters to minimize the cost function.

## Note

- This implementation is intended for educational purposes and provides a clear understanding of how Batch Gradient Descent works.
- This is not intented to be used for any kind of investing or financial strategy.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For any questions: cjpaine109@gmail.com.
