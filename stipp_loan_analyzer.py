import csv
from pathlib import Path
# Part One
loan_costs = [500, 600, 200, 1000, 450]
number_loans = len(loan_costs)
print(f"The total number of loans: {number_loans}")

total_value = sum(loan_costs)
print(f"The total value of all loans: ${total_value}")

average_loan_amount = total_value/number_loans
print(f"The average loan amount is ${average_loan_amount:.2f}.")

# Part Two
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
print(loan.get("future_value"))
print(loan.get("remaining_months"))

Discount_Rate = 0.20
fair_value = loan["future_value"] / (1 + Discount_Rate/12) ** loan["remaining_months"]
print (f"The fair value of the loan is: $ {fair_value:.2f}.")

if loan["future_value"] >= fair_value:
    print("The loan is worth at least the cost to buy it!")
else:
    print("The loan is too expensive and not worth the price.")

# Part Three
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
annual_discount_rate = 0.20

def present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months
    print(f"The present value of the loan is: ${present_value:.2f}")
cost_of_a_new_loan = present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)

#Part 4
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]
inexpensive_loans = []

for loan_data in loans:
    if loan_data["loan_price"] <= 500:
        inexpensive_loans.append(loan_data)

# Struggling to take all keys of filtered dictionary to list - 
# only returning "loan_price", deleted other code that was working but
# didn't match header for csv file 

print(inexpensive_loans)

#Part 5
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
output_path = Path("inexpensive_loans.csv")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for loan_data in inexpensive_loans:
        csvwriter.writerow(loan_data.values())

