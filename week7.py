from datetime import datetime

FILE_NAME = "employees.txt"


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%m/%d/%Y")
        return True
    except ValueError:
        return False


def get_date(prompt):
    while True:
        date_input = input(prompt)
        if validate_date(date_input):
            return date_input
        print("Invalid date format. Use mm/dd/yyyy.")


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



def save_record(from_date, to_date, name, hours, rate, tax_rate):
    with open(FILE_NAME, "a") as file:
        file.write(
            f"{from_date}|{to_date}|{name}|{hours}|{rate}|{tax_rate}\n"
        )


def get_report_date():
    while True:
        report_date = input("\nEnter FROM date for report (mm/dd/yyyy) or All: ")
        if report_date.lower() == "all":
            return "All"
        if validate_date(report_date):
            return report_date
        print("Invalid date format.")


def process_file(report_date):
    totals = {"employees": 0, "hours": 0, "tax": 0, "net": 0}

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                record = line.strip().split("|")

                if len(record) != 6:
                    continue

                from_date, to_date, name, hours, rate, tax_rate = record
                hours = float(hours)
                rate = float(rate)
                tax_rate = float(tax_rate)

                if report_date == "All" or from_date == report_date:
                    gross, tax, net = calculate_pay(hours, rate, tax_rate)

                    print("\nEmployee Payroll")
                    print("From Date:", from_date)
                    print("To Date:", to_date)
                    print("Name:", name)
                    print("Hours Worked:", round(hours, 2))
                    print("Hourly Rate:", round(rate, 2))
                    print("Gross Pay:", gross)
                    print("Income Tax Rate:", tax_rate)
                    print("Income Tax:", tax)
                    print("Net Pay:", net)

                    totals["employees"] += 1
                    totals["hours"] += hours
                    totals["tax"] += tax
                    totals["net"] += net

    except FileNotFoundError:
        print("No employee file found.")
        return totals

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

while True:
    from_date = get_date("\nEnter FROM date (mm/dd/yyyy): ")
    to_date = get_date("Enter TO date (mm/dd/yyyy): ")

    name = get_name()
    if name == "End":
        break

    hours = get_float("Enter hours worked: ")
    rate = get_float("Enter hourly rate: ")
    tax_rate = get_tax_rate()

    save_record(from_date, to_date, name, hours, rate, tax_rate)

print("\nData entry complete.")

report_date = get_report_date()
totals = process_file(report_date)
display_totals(totals)