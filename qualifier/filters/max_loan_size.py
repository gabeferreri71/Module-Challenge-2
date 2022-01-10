
def filter_max_loan_size(loan_amount, bank_list):

# list filled with the max loan size of the client with parameters loan_amount and bank_list
    
    loan_size_approval_list = []

# "1" refers to the position of the credit score within the bank list

    for bank in bank_list:
        if loan_amount <= int(bank[1]):
            loan_size_approval_list.append(bank)
    return loan_size_approval_list
