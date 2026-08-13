# Matplotlib Assignment 11

This project demonstrates various data visualization techniques using the pure `matplotlib` API and `pandas` (strictly for data manipulation), based on the Walmart Sales dataset.

## Files Overview

### `matplotlib_assignment.ipynb` - Master Notebook
This notebook is the main submission file that contains all 7 tasks executed sequentially:
- **Task 1: Line Chart** - Visualizes the Walmart sales trend over months using `plt.plot()`.
- **Task 2: Scatter Plot** - Displays the relationship between Store Number and Weekly Sales using `plt.scatter()`.
- **Task 3: Bar Charts** - Shows vertical and horizontal bar charts for Average Weekly Sales by Store using `plt.bar()` and `plt.barh()`.
- **Task 4: Multiple Bar Chart** - A multiple bar chart comparing sales across different years and quarters side-by-side using calculated offsets and `plt.bar()`.
- **Task 5: Stacked Bar Chart** - Displays total weekly sales by store and year as a stacked bar chart using `plt.bar()` with the `bottom` parameter.
- **Task 6: Histogram** - Analyzes the distribution of Weekly Sales using `plt.hist()`.
- **Task 7: Pie Chart** - Depicts the share of Holiday vs. Non-Holiday sales records using `plt.pie()`.

## Requirements

You must have the following libraries installed:
- `pandas`
- `matplotlib`
- `numpy`
- `jupyter` (to run the notebook)

You can install them using pip:

```bash
pip install pandas matplotlib numpy jupyter
```

## How to Run

1. Ensure that the dataset file `Walmart_Sales.csv` is located in the same directory as the notebook.
2. Open your terminal or command prompt and navigate to this project directory (`Assignment11`).
3. Start the Jupyter Notebook server by running:

```bash
jupyter notebook matplotlib_assignment.ipynb
```

4. Once the notebook opens in your web browser, click on **Cell > Run All** to execute all the tasks sequentially and view the generated plots directly below each cell.
