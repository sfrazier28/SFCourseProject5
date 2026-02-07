def get_dates():
    from_date = input("Enter FROM date (mm/dd/yyyy): ")
    to_date = input("Enter TO date (mm/dd/yyyy): ")
    return from_date, to_date


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


def display_employee_list(employee_list):
    print("\nEmployee List")
    for emp in employee_list:
        print(emp)


def process_employees(employee_list, employees, from_date, to_date):
    totals = {
        "employees": 0,
        "hours": 0.0,
        "tax": 0.0,
        "net": 0.0
    }

    for name in employee_list:
        data = employees[name]

        gross, tax, net = calculate_pay(
            data["hours"],
            data["rate"],
            data["tax_rate"]
        )

        print("\nEmployee Payroll")
        print("From Date:", from_date)
        print("To Date:", to_date)
        print("Name:", name)
        print("Hours Worked:", round(data["hours"], 2))
        print("Hourly Rate:", round(data["rate"], 2))
        print("Gross Pay:", gross)
        print("Income Tax Rate:", data["tax_rate"])
        print("Income Tax:", tax)
        print("Net Pay:", net)

        totals["employees"] += 1
        totals["hours"] += data["hours"]
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

employee_list = []
employees = {}

while True:
    name = get_name()
    if name == "End":
        break

    employee_list.append(name)

    employees[name] = {
        "hours": get_float("Enter hours worked: "),
        "rate": get_float("Enter hourly rate: "),
        "tax_rate": get_tax_rate()
    }

if employee_list:
    display_employee_list(employee_list)
    totals_dict = process_employees(employee_list, employees, from_date, to_date)
    display_totals(totals_dict)
else:
    print("\nNo employee data entered.")
