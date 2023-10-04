# Description:      This program calculates employee payroll at Widgets Inc.
# Author:           Ellen Dalton
# Date Started:     May 8, 2023
# Date Completed:   May 8, 2023

# Constants are as follows:
HOURLY_RATE = 19.50
WIDGET_RATE = 0.35
UNION_DUES = 18.00

# Input the following:
employee_name = input("Employee name: ")
hours_worked = float(input("Hours worked: "))
num_wid_prod_mon = int(input("Number of widgets produced on Monday: "))
num_wid_prod_tues = int(input("Number of widgets produced on Tuesday: "))
num_wid_prod_wed = int(input("Number of widgets produced on Wednesday: "))
num_wid_prod_thus = int(input("Number of widgets produced on Thursday: "))
num_wid_prod_fri = int(input("Number of widgets produced on Friday: "))

# Calculate the following:
reg_pay = hours_worked * HOURLY_RATE  # Regular Pay
tot_num_widgets = num_wid_prod_mon + num_wid_prod_tues + num_wid_prod_wed + \
                  num_wid_prod_thus + num_wid_prod_fri  # Total number of widgets produced
com = WIDGET_RATE * tot_num_widgets  # Commission
gross_pay = reg_pay + com  # Gross pay
income_tax = 0.21*gross_pay  # Income Tax
cpp = 0.0495*gross_pay  # CPP
ei = 0.016*gross_pay  # EI
tot_deductions = income_tax + cpp + ei + UNION_DUES  # Total deductions
net_pay = gross_pay - tot_deductions  # Net pay

# Display the following:
print()
print("Employee name:                 ", employee_name)
print("Total # of widgets produced:   ", tot_num_widgets)
print()
print(f"Regular Pay:                    ${reg_pay:>9.2f}")
print(f"Commission:                     ${com:>9.2f}")
print(f"Gross Pay:                      ${gross_pay:>9.2f}")
print()
print(f"Income Tax:                     ${income_tax:>9.2f}")
print(f"CPP:                            ${cpp:>9.2f}")
print(f"EI:                             ${ei:>9.2f}")
print(f"Union Dues:                     ${UNION_DUES:>9.2f}")
print(f"Total Deductions:               ${tot_deductions:>9.2f}")
print()
print(f"Net Pay:                        ${net_pay:>9.2f}")
