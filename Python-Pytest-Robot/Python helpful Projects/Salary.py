def get_float_input(prompt):
    """Helper function to get float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Collect user inputs
print("Enter your salary components (annual figures):")
basic = get_float_input("Basic: ")
hra = get_float_input("House Rental Allowance: ")
special_allowance = get_float_input("Special Allowance: ")
bonus = get_float_input("Advance Statutory Bonus: ")
conveyance = get_float_input("Conveyance Allowance: ")
pf_contribution = get_float_input("Company's Contribution to PF: ")
incentive = get_float_input("Incentive: ")
insurance = get_float_input("Company’s contribution to benefits (Medical, Accident, Life Insurance): ")

# Calculate the annual gross, CTC, and fixed pay
annual_gross = basic + hra + special_allowance + bonus + conveyance
ctc = annual_gross + pf_contribution + incentive + insurance
fixed_pay = basic + hra + special_allowance + conveyance
variable_pay = bonus + incentive
other_benefits = pf_contribution + insurance

# Ask for actual in-hand salary
actual_in_hand = get_float_input("Enter your actual in-hand salary (monthly): ")

# Monthly calculations
monthly_fixed_pay = fixed_pay / 12
monthly_variable_pay = variable_pay / 12
monthly_in_hand_calculated = (annual_gross / 12) - (pf_contribution / 12)


# Display results
print("\n### Results ###")
print(f"1. Current CTC: ₹{ctc:.2f}")
print(f"   In-hand Salary (Calculated): ₹{monthly_in_hand_calculated:.2f}")
print(f"   In-hand Salary (Actual): ₹{actual_in_hand:.2f}")
print(f"   Difference: ₹{actual_in_hand - monthly_in_hand_calculated:.2f}")
print()
print(f"2. Fixed Pay: ₹{fixed_pay / 1_00_000:.2f} Lakhs")
print(f"   Variable Pay: ₹{variable_pay / 1_00_000:.2f} Lakhs")
print(f"   Other Benefits: ₹{other_benefits / 1_00_000:.2f} Lakhs")

# Percentage-based raise calculations
print("\n### Percentage-based Raise ###")
print("Percentage | CTC After Raise (₹) | In-hand After Raise (₹/month)")
for percentage in [3, 4, 4.4, 5] + list(range(10, 101, 10)):
    raise_factor = 1 + (percentage / 100)
    new_ctc = ctc * raise_factor
    new_monthly_in_hand = (new_ctc / 12) - (pf_contribution / 12)
    difference = (new_ctc / 12) * (actual_in_hand / ctc)
    print(f"{percentage:>9}% | {new_ctc:>17.2f} | {new_monthly_in_hand:>26.2f}")

# Template for job portal
expected_min_ctc = ctc * 1.3
expected_max_ctc = ctc * 1.5
print("\n### Job Portal Template ###")
print(f"""
I am currently looking for opportunities where I can grow both professionally and financially. 
Given my experience, skills, and current compensation, I am seeking a raise of approximately 30% to 50% 
from my current CTC of ₹{ctc / 1_00_000:.2f} Lakhs annually.

My expected CTC range is between ₹{expected_min_ctc / 1_00_000:.2f} Lakhs to ₹{expected_max_ctc / 1_00_000:.2f} Lakhs annually. 
I am flexible based on the company's offerings and role specifics. I am eager to explore challenging roles that align 
with my career aspirations in automation testing and related fields.
""")
