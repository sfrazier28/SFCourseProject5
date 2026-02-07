def get_dates():
    while True:
        from_date = input("Enter FROM date (mm/dd/yyyy): ")
        to_date = input("Enter TO date (mm/dd/yyyy): ")
        if from_date and to_date:
            return from_date, to_date
        print("Dates cannot be empty.")


def get_name():
    return input("Enter employee name (or type End): ")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def get_tax_rate():
    return get_float("Enter income tax rate (example: 20 for 20%): ") / 100


def calculate_pay(hours, rate, tax_rate):
    gross = round(hours * rate, 2)
    tax = round(gross * tax_rate, 2)
    net = round(gross - tax, 2)
    return gross, tax, net


def process_employees(names, hours, rates, tax_rates, from_date, to_date):
    totals = {
        "employees": 0,
        "hours": 0.0,
        "tax": 0.0,
        "net": 0.0
    }

    for i in range(len(names)):
        gross, tax, net = calculate_pay(hours[i], rates[i], tax_rates[i])

        print("\nEmployee Payroll")
        print("From Date:", from_date)
        print("To Date:", to_date)
        print("Name:", names[i])
        print("Hours Worked:", round(hours[i], 2))
        print("Hourly Rate:", round(rates[i], 2))
        print("Gross Pay:", gross)
        print("Income Tax Rate:", tax_rates[i])
        print("Income Tax:", tax)
        print("Net Pay:", net)

        totals["employees"] += 1
        totals["hours"] += hours[i]
        totals["tax"] += tax
        totals["net"] += net

    totals["hours"] = round(totals["hours"], 2)
    totals["tax"] = round(totals["tax"], 2)
    totals["net"] = round(totals["net"], 2)

    return totals


def display_totals(totals):
    print("\nPayroll Totals")
    print("Total Employees:", totals["employees"])
    print("Total Hours:", totals["hours"])
    print("Total Income Tax:", totals["tax"])
    print("Total Net Pay:", totals["net"])


# ---------------- MAIN PROGRAM ---------------- #

from_date, to_date = get_dates()

employee_names = []
hours_worked = []
hourly_rates = []
tax_rates = []

while True:
    name = get_name()
    if name == "End":
        break

    employee_names.append(name)
    hours_worked.append(get_float("Enter hours worked: "))
    hourly_rates.append(get_float("Enter hourly rate: "))
    tax_rates.append(get_tax_rate())

if employee_names:
    totals_dict = process_employees(
        employee_names,
        hours_worked,
        hourly_rates,
        tax_rates,
        from_date,
        to_date
    )
    display_totals(totals_dict)
else:
    print("\nNo employee data entered.")
