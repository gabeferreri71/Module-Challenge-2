# In this first section, we import everything we may need (sys, fire, questionary, csv) into our app. The "from __ import ___" is used to call the necessary functions already defined 
# within the modules for filters

import sys
import fire
import questionary 
import csv
from pathlib import Path

from qualifier.utils.fileio import load_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value


# in this section, we create our save_csv function with the qualifying_loans parameter, by which we ask the user to name their new .csv file when it is produced 

def save_csv(qualifying_loans):

    location = questionary.text("What name would you like to give to the newly-saved .csv file?").ask()
    header = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]
    location += ".csv"

 # with open() as statement to write the qualifying loans in the newly-named .csv file to be produced.

    with open(location, "w") as csvfile:
        
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(header)
        for loan in qualifying_loans:
            csvwriter.writerow(loan)
    return 
 
     
#In this section, we are setting the file path to the location of the original .csv file and checking if it exists.

def load_bank_data():
    csvpath = Path("./data/daily_rate_sheet.csv")
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

# here we return the load_csv function from the fileio.py using the parameter csvpath

    return load_csv(csvpath)

# Here we are prompting the user to enter the necessary information to calculate the qualifying loans and returning the values.

def get_applicant_info():

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value

# We are defining the find_qualifying_loans function, which utilizes the two functions provided in the calculators.py file. Once calculating and printing the results (will be seen in the terminal window),
# variables are set to the functions within the filters folder .py files, using each "bank_data_filtered" variable to solve the next function. The result will print the len() or length function to determine 
# the number of objects (in this case loans) in bank_data_filtered, followed by a return satement.

def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")
    
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")
    
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered

# In this function, we use the parameter qualifying_loans within the save_qualifying_loans function to prompt the user with [Y/N] as to if they want to save the qualifying loan data, and with Y,
# run an if loop to run the save_csv function with the parameter qualifying_loans.

def save_qualifying_loans(qualifying_loans):

    save_prompt = questionary.confirm("Would you like to save the qualifying loans csv?").ask() 
    if save_prompt:
        save_csv(qualifying_loans) 
    return 

# This last run function is what executes our code, containing the previously-defined load_bank_data, get_applicant_info, find_qualifying_loans, and save_qualifying_loans functions with associated variables.

def run():
    
    bank_data = load_bank_data()

    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    save_qualifying_loans(qualifying_loans)

# turns python components into command line interfaces

if __name__ == "__main__":
    fire.Fire(run)
