import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("clean_student.csv")

# numeric columns 
numeric_cols = df.select_dtypes(include='number').columns

# plot histogram with kde
for col in numeric_cols:
    plt.figure(figsize=(8, 5))
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()


# categorical columns
categorical_cols = df.select_dtypes(include=['string', "object"]).columns

# Count Plot
for col in categorical_cols:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x=col)
    plt.title(f'Count Plot of {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()


# boxplot for detecting outliers
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.xlabel(col)
    plt.show()


'''
1. Most of the numerical variables exhibit a reasonably balanced distribution where hours of studying and attendance are clustered at moderate levels. 
2. Examination marks are clustered towards the low to middle range and exhibit right-skewness with a few extremely high values. 
3. Tutoring is also skewed right suggesting that many students have relatively few tutoring sessions while a smaller number of students has many.
4. The plots for categorical variables indicate that **Medium** parental involvement and **Yes** extracurricular activity belong to the common categories.
5. Boxplots can be used to find outliers especially in examination marks and tutoring sessions.
'''

