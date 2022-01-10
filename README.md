# Module Challenge 2: Qualifying Loans Application: Find Out If You're Clients Are Eligible!

The dream of homeownership in 2022 America seems bleak for many, however, many Americans do not realize that they can qualify for a loan to live out their "American Dream." To help with this
issue, I have developed the Qualifying Loans Application, an app that allows those within BizOps to collect a client's credit score, monthly debt, montly income, desired loan amount, and home value.

Through the app's modularization and code design, a client's credentials can be quickly filtered and calculated for factors including the credit score, debt-to-income-ratio, loan-to-value-ratio, and maximum loan size, to then match the client's information with qualifying loans from BizOps' Daily Rate Sheet of available loans. 

The app then will prompt to have a list of qualifying loans based on the client's info saved, followed by a prompt asking the user what name they would like to save the new .csv file as. The app will then retrun a new .csv file with the prompted name within the loan_qualifier_app folder, for direct use of the client and/or user. 



Just after the title, introduce your project by describing attractively what the project is about and what is the main problem that inspires you to create this project or what is the main contribution for the potential user of your project.

---

# Technologies

This application was coded within Python using Anaconda, running within its own "loanqualifierapp" environment in version 3.7.11. Imported source files include sys, fire, questionary, and csv; sys provides various functions and variables to run the environment, fire turns Python components into command line interfaces, questionary for building direct command line features, and csv to
parse tabular-like data structures.

As a modularized application, the app is able to call functions (groups of related statements used to execute a specifc task and defined with "def") from the internal .py files using "from___import__," with the in question .py file location and name entered first (ex. qualifier.filters.max_loan_size) followed by the needed function within the .py file.

The application also uniquely uses csv-related functions (.writer(), .writerow(), .reader(), .append()), which in context help to read and extract information from the provided Daily Rate Sheet, and then create a new .csv file of qualifying loans based on the client data input. 



Describe the technologies required to use your project such as programming languages, libraries, frameworks, and operating systems. Be sure to include the specific versions of any critical dependencies that you have used in the stable version of your project.

---

#  Installation Guide

To complete the installation of our application, we first evaluated the starter code to see what was provided. Within the utils folder, we checked the fileio.py and calculators.py to understand each modularized function; the fieio.py defines the loan_csv function after an import csv statement. The load_csv function reads the CSV file from the provided path (to be covered in app.py file) and then returns "data" which is a list of lists with the rows of CSV file data, as can be seen in the image below:



The calculators.py file contains two functions, calculate_monthly_debt_ratio and calculate_loan_to_value ratio, which will use the client's monthly debt and monthly income and loan amount and home value, respectively, to calculate the two functions with basic math, as shown below:



Once the functions in the utils .py files were determined as ok, a similar process was used to evaluate the credit_score.py, debt_to_income.py, loan_to_value.py, and max_loan_size.py files from the filter folder. These functions utilize for loops to take the client's entered credit score, and loan amount along with the monthly_debt_ratio and loan_to_value ratio that are returned in the calculators.py file and creates lists of the qualifying compnents within each loop. The list is then returned at the end of each function, as can be seen in the images below:




After evaluating the utlis and filters .py files and their associated functions, work began on the main app.py file. The starter code provided the majority of imports needed and proper "from__import__" statements for the relevant functions we will need from the utils and filters folders as seen below:




The first function created within the app.py file directly was the save_csv function, with the parameter qualifying_loans. Within the function a variable "location" was made and assigned using questionary.text().ask to ask the user what they would like to save their new csv of qualifying loans as, followed by a "header" varaible of the column labels. The location variable is then assigned with +=".csv" which is the same as saying location = location + .csv, adding .csv to the entered file name. Below is a "with open() as __" with open parameters of location (our new file name) and "w" for write, as we are wrting a new csv. This is opened as csvfile. Now, unlike in fileio.py where we're reading a csv file, we are writing a csv file and will need the csv.writer and .writerow functions. This is first used to add the string from the "header variable." To rotate through all of the qualifying loans, a for loop is added at the end with parameters "loan" and "qualifying_loans" of the function, and then returned:




Now that we have the save_csv function, we need to establish the file path through the loan_bank_data function. We need the information from the daily_rate_sheet.csv file, so a path to that file was directly set with the variable csvpath (*Note: starter code asks to prompt user for file location, but does not specify this in the grading rubric. I asked in Saturday office hours and setting the path directly was deemed ok). Even though we are setting the path directly, if someone were to change where the daily_rate_sheet file was, an if statement is present to state that the path does not exist, as shown below:



The next two functions in the app.py file, get_applicant_info and find_qualifying_loans, were provided with the starter code. get_applicant_info will prompt the client for the necessary information (credit score, monthly debt, monthly income, loan amount, home value) using the proper classes (float for everything except credit score which must be an int) to return said information, as below:




The find_qualifying_loans function takes the returned parameters from get_applicant_info as function parameters to determine the monthly_debt_ratio and loan_to_value ratio based on the function parameters. bank_data_filtered variables are then created and assigned to the associated filters functions to print the total number of qualifying loans using the len function and returning bank_data_filtered.




At this point, we wrote our save_qualifying_loans function, with qualifying_loans as the parameter. Using variable save_prompt, we use questionary.confirm().ask to prompt the user if they would like to save the qualifying loans in a .csv file. A for loop would then run the save_csv function with qualifying_loans parameter, as below:





At the bottom, our run function from the starter code was unedited, containing the load_bank_data, get_applicant_info, save_qualifying_loans, and save_qualifiying loans functions. The code is ended with a fire.Fire() to turn components into command line interfaces (Note: even with Fire, I would like the client to have ease-of-use and enter each data component needed at a time.)


## Usage

Using this app is fairly easy. After downloading the loan_qualifier_app, we want to open up or GitBash terminal and cd to the folder. Once in the folder, and already having the proper versions of python, questionary, fire, and pytest installed, we will simply type "python app.py" in the terminal. The first prompts you'll see will ask for your credit score, monthly debt, monthly income, desired loan amount and home value. For the purpose of this example, I entered 770, 2000, 4500, 300000, and 425000, respectively. The terminal will then output the monthly debt_to_income ratio and loan_to_value ratio on screen, followed by the number of loans found (in this case 4). The user is the prompted to save the qualifying loans .csv with [Y/n] and if yes, the user is prompted to name the file. After the file is named and entered, the new .csv file of qualifying loans will be saved back in the loan_qualifier_app folder:






---

## Contributors

Those who contributed to this application include Columbia Engineering Fintech Bootcamp for providing the starter code, .csv file and directional instructions for the app, and Lance Arena, a software engineer for Northwestern Mutual for providing clarifiation on creating a save-csv function.


The main writer and contributer of this appliation is Gabriel Ferreri, and can be contacted at:

Gabriel M. Ferreri
(516)-660-5266
gabeferreri49@gmail.com

---

## License

I am really not sure what to put in this section, so I am doing to leave it.
