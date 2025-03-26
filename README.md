# HealthDatamat

HealthDatamat is a repository that contains samples of my worked projects in Data Science. It includes examples of data manipulation and visualization using **NumPy** and **Matplotlib**. In this repository, you'll find various coding exercises that demonstrate how to handle arrays, perform mathematical operations, and create visualizations.

## Projects Included

- **NumPy Array Operations**: Manipulating 1D and 2D arrays, performing mathematical operations like addition, multiplication, and slicing.
- **Matplotlib Visualizations**: Creating various types of plots, such as line plots and bar charts, to visualize data.
- **Data Science Simulations**: A demonstration of handling data with various scenarios, such as healthcare data analysis and impact visualizations.

## How to Get Started with Jupyter in VS Code

1. **Install Visual Studio Code (VS Code)**:
   - Download and install VS Code from the official site: [Visual Studio Code](https://code.visualstudio.com/).

2. **Install Python and Jupyter**:
   - Install Python if it's not installed: [Download Python](https://www.python.org/downloads/).
   - Install Jupyter by running the following in your terminal:
     ```bash
     pip install notebook
     ```

3. **Install the Python Extension for VS Code**:
   - Open VS Code, go to the Extensions tab (or press `Ctrl+Shift+X`), and search for `Python`.
   - Install the extension by Microsoft.

4. **Create a New Jupyter Notebook**:
   - Open VS Code, and click on the "View" tab and select "Command Palette" (`Ctrl+Shift+P`).
   - Search for and select "Jupyter: Create New Notebook".
   - Choose the Python environment you want to use (ensure Jupyter is installed).

5. **Start Coding**:
   - Copy the code from the repository or write your own within the Jupyter Notebook.
   - Use the **Run** button to execute your code and see the output.

## Example Code

```python
import numpy as np
import matplotlib.pyplot as plt

# Example 1: NumPy array operations
arr = np.array([1, 2, 3, 4, 5])
total_multiply = arr * 5
print(total_multiply)

# Example 2: Creating a plot
x = np.arange(0, 2 * np.pi, 0.5)
y = np.sin(x)

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title("Sine Wave")
plt.xlabel("x (radians)")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()

