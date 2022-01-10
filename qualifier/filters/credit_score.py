
def filter_credit_score(credit_score, bank_list):

# list filled with the min. credit score of the user using the credit_score and bank_list parameters
    credit_score_approval_list = []
    for bank in bank_list:
# "4" refers to the position of the credit score within the bank list
        if credit_score >= int(bank[4]):
            credit_score_approval_list.append(bank)
    return credit_score_approval_list
