
def filter_loan_to_value(loan_to_value_ratio, bank_list):

#list filled with max loan-to-value ratio with parameters laon_to_value_ratio and bank_list
   
    loan_to_value_approval_list = []

# "2" refers to the position of the credit score within the bank list
    for bank in bank_list:
        if loan_to_value_ratio <= float(bank[2]):
            loan_to_value_approval_list.append(bank)
    return loan_to_value_approval_list
