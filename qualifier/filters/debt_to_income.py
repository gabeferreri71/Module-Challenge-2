
def filter_debt_to_income(monthly_debt_ratio, bank_list):

#list filled with max. monthly debt ratio with the parameters monthly_debt_ratio and bank_list    
    
    debit_to_income_approval_list = []

# "3" refers to the position of the credit score within the bank list
    for bank in bank_list:
        if monthly_debt_ratio <= float(bank[3]):
            debit_to_income_approval_list.append(bank)
    return debit_to_income_approval_list
