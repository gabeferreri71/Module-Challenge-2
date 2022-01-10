# calculates basic monthly debt ratio formula with parameters monthly_debt_payment and monthly_income, where the parameters must be integers.

def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
    
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio

# calculates basic loan-to-value ratio with parameters loan_amount and home_value, where the parameters must also be integers.

def calculate_loan_to_value_ratio(loan_amount, home_value):
    
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio
