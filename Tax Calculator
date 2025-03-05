#Tax Calculator Based on Gross Income

def calculate_tax(gross_income):
    if gross_income <= 12500:
        tax = 0
    elif gross_income <= 50000:
        tax = (gross_income - 12500) * 0.20
    elif gross_income <= 150000:
        tax = (37500 * 0.20) + (gross_income - 50000) * 0.40
    else:
        tax = (37500 * 0.20) + (100000 * 0.40) + (gross_income - 150000) * 0.45
    
    return tax

def main():
    gross_income = float(input("Enter your gross income (£): "))
    tax_owed = calculate_tax(gross_income)
    net_income = gross_income - tax_owed
    
    print(f"Tax Owed: £{tax_owed:,.2f}")
    print(f"Net Income: £{net_income:,.2f}")

if __name__ == "__main__":
    main()
