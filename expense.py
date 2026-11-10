import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("expense.csv")

# Data Understand:

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

# Data Cleaning:

print(df.isnull().sum())
print(df.duplicated().sum())
df = df.drop_duplicates()
df['Category'] = df['Category'].str.strip().str.title()
df['Type'] = df['Type'].str.strip().str.title()

# Pandas:

df["Date"] = pd.to_datetime(df['Date'])

expense_df = df[df['Type']=='Expense']
total_expense = expense_df['Amount'].sum()
print(total_expense)

expense_df = df[df['Type'] == 'Income']
total_income = expense_df['Amount'].sum()
print(total_income)

savings = total_income - total_expense
print(savings)

category_expense = (
    expense_df
    .groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)
print(category_expense)

# Numpy :

df["expense_level"] = np.where(df["Amount"] >= 1000,"High","Normal")

expense_df = df[df["Type"] == "Expense"]
total_expense = expense_df["Amount"].sum()
print(total_expense)

income_df = df[df["Type"] == "Income"]
total_income = income_df["Amount"].sum()
print(total_income)

category_expense = (
    expense_df
    .groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print(category_expense)

# Matplotlib :

ax = category_expense.plot(kind="bar")
plt.title("Expense by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation =45)
for container in ax.containers:
    ax.bar_label(container)
plt.tight_layout()
plt.show()

# seaborn :

sns.barplot(
    data = expense_df,
    x = "Category",
    y = "Amount",
    errorbar = None
)

plt.title("Expense Distribution by category")
plt.xticks(rotation = 45)
plt.show()

# Expense by category Pie Chart :

category_expense.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(7,7)
)
plt.title("Expense Percentage  by Category")
plt.show()

# Payment Mode Analysis:

payment_expense = expense_df.groupby("Payment_mode")["Amount"].sum()

print("Expense By Payment Mode:")
print(payment_expense)

# Bar Chart :
payment_expense.plot(kind="bar")
plt.title("Expense by Payment Mode")
plt.ylabel("Amount")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Monthly Expense :

monthly_expense = expense_df.groupby(
    expense_df['Date'].dt.to_period('M')
)["Amount"].sum()

print("Montly Expense Alanysis")
print(monthly_expense)
monthly_expense.plot(kind="bar")
plt.title("Monthly Expense Anlaysis")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation = 0)

plt.tight_layout()
plt.show()

# Savings Analysis :

total_income = df.loc[df["Type"] == "Income","Amount"].sum()
total_expense = df.loc[df["Type"] == "Expense", "Amount"].sum()
savings = total_income - total_expense 
print("Total Income:",total_income)
print("Total Expense:",total_expense)
print("Total Savings:",savings)

# Savings Percentage Analysis:

savings_percentage = (savings/total_income)*100
print("Savings Percentage:",round(savings_percentage,2),"%")

# Highest Expense Category :

highest_category = category_expense.idxmax()
highest_amount = category_expense.max()
print("Highest Expense Category:", highest_category)
print("Highest Expense Amount:", highest_amount)

# Lowest Expense Category :

lowest_category = category_expense.idxmin()
lowest_amount = category_expense.min()
print("Lowest Expense Category:",lowest_category)
print("Lowest Expense Category:",lowest_amount)

# Expense Percentage by Category :

category_percentage = (category_expense / total_expense) *100
print("Expense Percentage by Category:")
print(category_percentage.round(2))

# Payment Percentage by Category :

payment_expense = (payment_expense / total_expense) *100
print("Payment Mode Percentage:")
print(payment_expense.round(2))

# Financial Status Summery in Python :

total_savings = total_income - total_expense
if total_savings > 0:
    print("Your saving money:")
elif total_savings == 0:
    print("Your income equals your expense:")
else:
    print("Your expense exceed your income:")

# Clean data to CSV :

df.to_csv("cleaned_expense.csv",index=False)
print("Cleaned data saved successfully!")

# Save the Category :

category_expense.to_csv("cateory_expense_summay .csv")
print("Category expense summary saved successfuly!")

# Pyhton Monthly Expense :

df["Date"] = pd.to_datetime(df["Date"])
expense_df = df[df["Type"] == "Expense"].copy()
expense_df["Month"] = expense_df["Date"].dt.strftime("%B")
monthly_expense = expense_df.groupby ("Month")["Amount"].sum()
print("\nMonthly Expense Summary:")
print(monthly_expense)
monthly_expense.to_csv("Monthly_expense_summary.csv")
print("Monthly expense summary saved sucessfully!")

# Savings Percentage Analysis :

savings_percentage = (total_savings / total_income) * 100
print("Savings Percentage:",round(savings_percentage, 2),"%")