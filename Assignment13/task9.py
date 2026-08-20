import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("clean_student.csv")

numeric_cols = df.select_dtypes(include='number')


# Key numerical features vs Exam Score
num_features = ['hours_studied', 'attendance', 'previous_scores', 'sleep_hours']

plt.figure(figsize=(14, 10))
for i, col in enumerate(num_features, 1):
    plt.subplot(2, 2, i)
    sns.regplot(data=df, x=col, y='exam_score', scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
    plt.title(f'{col.replace("_", " ").title()} vs Exam Score')
    plt.xlabel(col.replace("_", " ").title())
    plt.ylabel('Exam Score')

plt.tight_layout()
plt.show()

# Correlation matrix among numerical variables
plt.figure(figsize=(10, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap (Numerical Features)')
plt.show()


cat_features = ['parental_involvement', 'access_to_resources', 'motivation_level', 'teacher_quality']

plt.figure(figsize=(14, 10))
for i, col in enumerate(cat_features, 1):
    plt.subplot(2, 2, i)
    sns.barplot(data=df, x=col, y='exam_score', estimator='mean', errorbar=None, palette='Blues_d')
    plt.title(f'Mean Exam Score by {col.replace("_", " ").title()}')
    plt.xlabel(col.replace("_", " ").title())
    plt.ylabel('Average Exam Score')
    plt.xticks(rotation=30)

plt.tight_layout()
plt.show()


box_features = ['internet_access', 'school_type', 'peer_influence', 'learning_disabilities']

plt.figure(figsize=(14, 10))
for i, col in enumerate(box_features, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(data=df, x=col, y='exam_score', palette='Set2')
    plt.title(f'Exam Score Distribution by {col.replace("_", " ").title()}')
    plt.xlabel(col.replace("_", " ").title())
    plt.ylabel('Exam Score')

plt.tight_layout()
plt.show()


# Relationship between Parental Involvement and Motivation Level
cross_tab = pd.crosstab(df['parental_involvement'], df['motivation_level'], normalize='index') * 100

plt.figure(figsize=(8, 5))
sns.heatmap(cross_tab, annot=True, fmt='.1f', cmap='YlGnBu')
plt.title('Parental Involvement vs Motivation Level (%)')
plt.xlabel('Motivation Level')
plt.ylabel('Parental Involvement')
plt.show()


'''
1. Exam grades can be analyzed in terms of their comparison to the hours spent studying, attendance, previous grades achieved, and sleep duration. 
2. The correlations heatmap enables you to find out whether the numerical variables have a strong positive or negative association with exam grades.
3. Average exam grades can be analyzed in terms of parental involvement, access to resources, levels of motivation, and teacher quality.
4. Boxplots can be used to analyze the distribution of exam grades depending on the quality of internet access, type of school, peer influence, and learning disabilities.
5. The heatmap clarifies whether different types of parental involvement are distributed within students' level of motivation.

'''