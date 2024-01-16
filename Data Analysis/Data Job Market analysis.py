### Import Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

### Read CSV file

df = pd.read_csv(r"C:\Users\Nicho\Desktop\jobs_in_data.csv")


### Descriptive Statistics

# Descriptive statistics for salary_in_usd
salary_stats = df['salary_in_usd'].describe()

# Count of each category in experience_level
experience_level_counts = df['experience_level'].value_counts()

# Count of each category in employment_type
employment_type_counts = df['employment_type'].value_counts()

# Count of each category in work_setting
work_setting_counts = df['work_setting'].value_counts()

# Count of each category in company_size
company_size_counts = df['company_size'].value_counts()

# Salary in USD Statistics
salary_stats_df = pd.DataFrame(salary_stats).reset_index()
salary_stats_df.columns = ['Statistic', 'Value']

# Experience Level Counts
experience_level_counts_df = pd.DataFrame(experience_level_counts).reset_index()
experience_level_counts_df.columns = ['Experience Level', 'Count']

# Employment Type Counts
employment_type_counts_df = pd.DataFrame(employment_type_counts).reset_index()
employment_type_counts_df.columns = ['Employment Type', 'Count']

# Work Setting Counts
work_setting_counts_df = pd.DataFrame(work_setting_counts).reset_index()
work_setting_counts_df.columns = ['Work Setting', 'Count']

# Company Size Counts
company_size_counts_df = pd.DataFrame(company_size_counts).reset_index()
company_size_counts_df.columns = ['Company Size', 'Count']

# Displaying the statistics
print("Salary in USD Statistics:\n", round(salary_stats_df,))
print("\nExperience Level Counts:\n", experience_level_counts_df)
print("\nEmployment Type Counts:\n", employment_type_counts_df)
print("\nWork Setting Counts:\n", work_setting_counts_df)
print("\nCompany Size Counts:\n", company_size_counts_df)



### Data Visualization

# 1. Frequency of each year
year_freq = df["work_year"].value_counts()
plt.figure(figsize=(6, 6))
ax = sns.barplot(x=year_freq.index, y=year_freq.values, palette="magma")
plt.title("Frequency of Each Year")
for i in ax.containers:
    ax.bar_label(i,)
plt.show()


# 2. Average Salaries for Each Year
avg_salaries_year = df.groupby("work_year")["salary_in_usd"].mean()
plt.figure(figsize=(6, 6))
ax = sns.lineplot(x=avg_salaries_year.index, y=avg_salaries_year.values, marker="o", color="r", linestyle="-")
plt.title("Average Salaries for Each Year")
plt.show()


# 3. Frequency of job titles
job_title_freq = df["job_title"].value_counts().head(10)
plt.figure(figsize=(6, 6))
ax = sns.barplot(y=job_title_freq.index, x=job_title_freq.values, palette="icefire")
plt.title("Top 10 most common data jobs")
for i in ax.containers:
    ax.bar_label(i,)
plt.show()

# 4. Visualize average salaries by job titles
avg_salaries_job_title = df.groupby("job_title")["salary_in_usd"].mean().sort_values()
plt.figure(figsize=(6, 6))
plt.pie(avg_salaries_job_title.head(5), labels=avg_salaries_job_title.head(5).index, autopct="%1.1f%%", startangle=140, colors=sns.color_palette("magma", 5))
plt.title("Top 5 Job titles")
plt.show()

# 5. Average salary by Job Category
avg_salaries_job_category = df.groupby('job_category')['salary_in_usd'].mean().sort_values()
plt.figure(figsize=(6, 6))
ax = sns.barplot(x=avg_salaries_job_category.values, y=avg_salaries_job_category.index, palette="crest")
plt.title("Average Salaries by Job Category")
for i in ax.containers:
    ax.bar_label(i, labels=[f"${int(value)}" for value in i.datavalues])
plt.show()

# 6. Average salary in USD based on currency
avg_salary_currency = df.groupby("salary_currency")["salary_in_usd"].mean().sort_values()
plt.figure(figsize=(6, 6))
ax = sns.barplot(x=avg_salary_currency.values, y=avg_salary_currency.index, palette="muted")
plt.title("Average Salary in USD by Currency")
for i in ax.containers:
    ax.bar_label(i, labels=[f"${int(value)}" for value in i.datavalues])
plt.show()

# 7. Salary based on experience level
salary_experience_level = df.groupby('experience_level')['salary_in_usd'].mean().sort_values()
plt.figure(figsize=(6, 6))
ax = sns.barplot(x=salary_experience_level.index, y=salary_experience_level.values, palette="coolwarm")
plt.title('Average Salary by Experience Level')
for i in ax.containers:
    ax.bar_label(i, labels=[f"${int(value)}" for value in i.datavalues])
plt.show()

# 8. Average salary based on employment type, work setting, and company size
avg_salary_employment_type = df.groupby('employment_type')['salary_in_usd'].mean().sort_values()
avg_salary_work_setting = df.groupby('work_setting')['salary_in_usd'].mean().sort_values()
avg_salary_company_size = df.groupby('company_size')['salary_in_usd'].mean().sort_values()


plt.figure(figsize=(6, 6))
ax = sns.barplot(x=avg_salary_employment_type.index, y=avg_salary_employment_type.values, palette="pastel")
plt.title('Average Salary by Employment Type')
plt.ylabel('Average Salary in USD')
plt.xticks(rotation=45)
for i in ax.containers:
    ax.bar_label(i, labels=[f"${int(value)}" for value in i.datavalues])
plt.show()


plt.figure(figsize=(6, 6))
ax = sns.barplot(x=avg_salary_work_setting.index, y=avg_salary_work_setting.values, palette="Set3")
plt.title('Average Salary by Work Setting')
plt.ylabel('Average Salary in USD')
plt.xticks(rotation=45)
for i in ax.containers:
    ax.bar_label(i, labels=[f"${int(value)}" for value in i.datavalues])
plt.show()


plt.figure(figsize=(6, 6))
ax = sns.barplot(x=avg_salary_company_size.index, y=avg_salary_company_size.values, palette="cool")
plt.title('Average Salary by Company Size')
plt.ylabel('Average Salary in USD')
plt.xticks(rotation=45)
for i in ax.containers:
    ax.bar_label(i, labels=[f"${int(value)}" for value in i.datavalues])
plt.show()


