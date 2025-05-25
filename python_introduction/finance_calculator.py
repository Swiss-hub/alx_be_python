monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: ${monthly_savings:.2f}")
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)  # Assuming a 5% annual interest rate
print(f"Your projected savings after one year, including interest, will be: ${projected_savings:.2f}")