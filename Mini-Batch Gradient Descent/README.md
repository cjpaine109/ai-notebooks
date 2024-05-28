# Linear Regression from Scratch

This repository contains basic implementations of Linear Regression models from scratch using Python. The models are built without relying on any machine learning libraries, showcasing the underlying mathematics and algorithms.

## Description

In this project, we compute the parameters for a Linear Regression model using Mini-Batch Gradient Descent. This algorithm works great for large datasets!

## Files

- `mini_batch_gradient_descent.ipynb`:
- `mini_batch_gradient_descent_class.ipynb`:
- `Dataset`: Folder containing dataset from Kaggle.
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
    cd Mini-Batch Gradient Descent
    ```

2. **Open the Jupyter Notebooks**:
    Open `mini_batch_gradient_descent.ipynb` in Jupyter Notebook to run and explore the code or
    open `mini_batch_gradient_descent_class.ipynb` in Jupyter Notebook to run and explore the code.

## Explanation of the Mini-Batch Gradient Descent Algorithm:

Note: very similar to SGD. Some slight differences in implementation (computing gradients + random sample size)

$w := w - \eta \cdot \frac{1}{m} \sum_{i \in \mathcal{B}} \nabla Q_{i}(w)$

Where:
- $w$ represents the weights or parameters of the model.
- $\eta$ (eta) is the learning rate, a scalar that controls the step size.
- $\nabla Q_{i}(w)$ is the gradient of the loss function $Q$ with respect to the weights $w$, computed using the $i$-th training example in the mini-batch.
- $m$ is the mini-batch size.
- $\mathcal{B}$ is the set of indices of the training examples in the current mini-batch.

## Note

- This implementation is intended for educational purposes.
- Dataset: https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For any questions: cjpaine109@gmail.com.
