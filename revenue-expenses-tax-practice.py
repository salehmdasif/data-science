"""
Scenario: You are a Data Scientist working for a consulting firm. One of your
colleagues from the Auditing department has asked you to help them assess the
financial statement of organization X.
You have been supplied with two vectors of data: monthly revenue and monthly expenses
for the financial year in question. Your task is to calculate the following

financial metrics:
- profit for each month
- profit after tax for each month (the tax rate is 30%)
- profit margin for each month - equals to profit after tax divided by revenue
- good months - where the profit after tax was greater than the mean for the year
- bad months - where the profit after tax was less than the mean for the year
- the best month - where the profit after tax was max for the year
- the worst month - where the profit after tax was min for the year

Results for dollar values need to be calculated with $0.01 precision, but need to be
presented in Units of $1,000 (i.e. 1k) with no decimal points.
Results for the profit margin ratio need to be presented in units of % with no
decimal points.
Note: Your colleague has warned you that it is okay for tax for any given month to be
negative (in accounting terms, negative tax translates into a deferred tax asset).
"""

# ---------------- SOLUTION ----------------
from builtins import list

revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28,
           9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73,
            5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

"""
profit = list([])
for i in range(0, len(revenue)):
    profit.append(revenue[i] - expenses[i])
"""

profit = [round(revenue[i] - expenses[i], 2) for i in range(0, len(revenue))]
print(profit)

tax = [round(i * 0.3, 2) for i in profit]
print(tax)

profit_after_tex = [round(profit[i] - tax[i], 2) for i in range(0, len(profit))]
print(profit_after_tex)

"""
profit_margin = list([])
for i in range(0, len(profit)):
    profit_margin.append(profit_after_tex[i]/revenue[i])
profit_margin = [round((i*100), 2) for i in profit_margin]
"""

profit_margin = [round((profit_after_tex[i] / revenue[i]) * 100, 2) for i in range(0, len(profit))]
print(profit_margin)

profit_after_tex_mean = sum(profit_after_tex) / len(profit_after_tex)
print(round(profit_after_tex_mean, 2))

good_months = list([])
for i in range(0, len(profit)):
    good_months.append(profit_after_tex[i] > profit_after_tex_mean)
print(good_months)

bad_months = list([])
for i in range(0, len(profit)):
    bad_months.append(profit_after_tex[i] < profit_after_tex_mean)
print(bad_months)

best_month = list([])
for i in range(0, len(profit)):
    best_month.append(profit_after_tex[i] == max(profit_after_tex))
print(best_month)

worst_month = list([])
for i in range(0, len(profit)):
    worst_month.append(profit_after_tex[i] == min(profit_after_tex))
print(worst_month)

# Convert All Calculations To Units Of One Thousand Dollars
revenue_1000 = [round(i / 1000, 2) for i in revenue]
expenses_1000 = [round(i / 1000, 2) for i in profit]
profit_1000 = [round(i / 1000, 2) for i in profit]
profit_after_tax_1000 = [round(i / 1000, 2) for i in profit_after_tex]

revenue_1000 = [int(i) for i in revenue_1000]
expenses_1000 = [int(i) for i in profit_1000]
profit_1000 = [int(i) for i in profit_1000]
profit_after_tax_1000 = [int(i) for i in profit_after_tax_1000]


print(revenue_1000)
print(expenses_1000)
print(profit_1000)
print(profit_after_tax_1000)

