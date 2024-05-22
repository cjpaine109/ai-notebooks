# Linear Regression from Scratch

This repository contains basic implementations of Linear Regression models from scratch using Python. The models are built without relying on any machine learning libraries, showcasing the underlying mathematics and algorithms.

## Description

In this project, we compute the parameters of the Linear Regression model using a closed-form solution known as the Normal Equation. This method is best suited for small to medium-sized datasets due to its time complexity of \(O(n^3)\).

## Files

- `Linear_Regression.ipynb`: Jupyter Notebook demonstrating the implementation and usage of the Linear Regression model.
- `Linear_Regression_class.ipynb`: Jupyter Notebook containing a class-based implementation of Linear Regression.
- `housing.csv`: Dataset used for training and testing the model (class).
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
    cd Simple Linear Regression
    ```

2. **Open the Jupyter Notebooks**:
    Open `Linear_Regression.ipynb` or `Linear_Regression_class.ipynb` in Jupyter Notebook to run and explore the code.

3. **Ensure the dataset is in the correct folder**:
    Place the `housing.csv` file in the `Dataset` folder. This is important for the notebooks to read the data correctly.

## Explanation of the Normal Equation

The Normal Equation is used to find the optimal parameters (theta) that minimize the cost function in Linear Regression. The closed-form solution is given by:

\[
theta = (X^T X)^{-1} X^T y
\]

where:
- \(X\) is the matrix of input features.
- \(y\) is the vector of output values.
- \(theta\) is the vector of parameters to be computed.

This method directly computes the best-fit parameters without requiring iterative optimization techniques like Gradient Descent.

## Note

- This implementation is intended for educational purposes and may not be suitable for large datasets due to its \(O(n^3)\) time complexity.
- Ensure that the dataset is correctly formatted and located in the `Dataset` folder before running the notebooks.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For any questions: cjpaine109@gmail.com.
