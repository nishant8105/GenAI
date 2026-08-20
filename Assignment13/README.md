# Data Analysis & Preprocessing Assignment

A step-by-step exploratory data analysis (EDA), data cleaning, database integration, API handling, and preprocessing project using Python, Pandas, Matplotlib, and Seaborn.

---

## 🚀 How to Run

### Step 1: Prerequisites
Ensure you have Python (version 3.9 or higher) installed on your system.

### Step 2: Install Required Libraries
Open your terminal (PowerShell, Command Prompt, or Bash) in the project folder and run:

```bash
pip install pandas numpy requests python-dotenv scikit-learn matplotlib seaborn 
```

### Step 3: Configure Environment Variables (For Task 4 API)
Create a `.env` file in the project folder (if not already present) and add your TMDb API Read Access Token:
```env
TMDBKEY=your_tmdb_bearer_token_here
```

---

## 📖 Methodology & Approach (Simple Breakdown)

### 🔹 Task 1: Basic Data Loading & Summary
- **Method:** Used `pd.read_csv()` to load `student.csv`.
- **Purpose:** Checked `.head()`, `.shape`, `.info()`, and `.describe()` to quickly understand data dimensions, column types, and statistical spread (mean, min, max, quartiles).

### 🔹 Task 2: Working with JSON Data
- **Method:** Exported the dataset using `.to_json()` and read it back with `pd.read_json()`.
- **Purpose:** Validated seamless conversion between tabular DataFrames and JSON format used in web services and APIs.

### 🔹 Task 3: SQLite Database Integration
- **Method:** Connected to a local database (`sample.db`) using Python's built-in `sqlite3`. Created an `employee` table, inserted sample records, and retrieved them into a Pandas DataFrame using `pd.read_sql_query()`.
- **Purpose:** Demonstrated how to bridge relational SQL databases with Pandas for analysis.

### 🔹 Task 4: Fetching Data from External APIs
- **Method:** Sent authenticated HTTP GET requests via `requests` library to TMDb endpoints for popular and top-rated movies.
- **Purpose:** Extracted JSON responses, structured relevant fields into DataFrames, and exported them to `tmdb_movies.csv` and `tmdb_top_rated_movies.csv`.

### 🔹 Task 5: Data Profiling
- **Method:** Separated numerical and categorical columns using `select_dtypes()`. Checked null value counts with `.isnull().sum()`.
- **Purpose:** Identified missing data patterns and mapped out what cleaning steps were necessary.

### 🔹 Task 6: Data Cleaning, Standardization & Type Casting
- **Method:**
  - Filled missing values in `Teacher_Quality` and `Parental_Education_Level` using their **mode** (most frequent value).
  - Filled missing values in `Distance_from_Home` with `"Unknown"`.
  - Removed duplicate rows using `.drop_duplicates()`.
  - Converted column names to lower `snake_case` (e.g., `Hours_Studied` → `hours_studied`) using regex for consistent coding.
  - **Explicit Type Casting:** Checked initial data types with `df.dtypes` and explicitly converted numerical columns to `int64` via `pd.to_numeric(errors='coerce')` and categorical columns to `string`.
- **Purpose:** Prepared a clean, reliable, and strictly typed dataset free of null errors, type mismatches, and inconsistent naming.

### 🔹 Task 7: Encoding & Train-Test Preparation
- **Method:** Applied `LabelEncoder` to transform text/categorical labels into numbers. Separated independent features into `X` and target variable (`exam_score`) into `y`.
- **Purpose:** Transformed raw data into a machine-learning-ready format.

### 🔹 Task 8: Univariate Analysis (Single Variable Study)
- **Method:**
  - **Histograms + KDE:** Observed the distribution shapes of numerical columns.
  - **Count Plots:** Counted frequency distributions across categorical classes.
  - **Box Plots:** Checked for skewness and detected potential outliers.
- **Purpose:** Understood the baseline behavior of each feature independently.

### 🔹 Task 9: Bivariate Analysis (Two-Variable Relationships)
- **Method:**
  - **Scatter Plots (`sns.regplot`):** Plotted numerical features (e.g., `hours_studied`, `attendance`) against `exam_score` with trendlines.
  - **Correlation Heatmap (`sns.heatmap`):** Calculated linear correlation coefficients across all numeric columns.
  - **Bar Plots & Box Plots:** Compared average `exam_score` and score distributions across categorical groups (e.g., `teacher_quality`, `internet_access`, `peer_influence`).
  - **Cross-tabulation Heatmap:** Evaluated relationships between categorical pairs (`parental_involvement` vs `motivation_level`).
- **Purpose:** Identified key drivers and dependencies influencing student exam performance.


## 🔍 Key Findings & Insights
- **Attendance ($\approx 0.58$) & Study Hours ($\approx 0.45$):** Strongest positive predictors of student exam performance.
- **Resources & Environment:** High access to resources, quality teaching, and positive peer influence consistently elevate performance.
- **Gender Balance:** Shows no statistically meaningful disparity in exam scores between male and female students.

---
