def to_be_paid(amount, bill):
    due = amount - bill
    return max(due, 0)
bill = float(input("Enter the bill amount: "))
amount = float(input("Enter the amount paid: "))
due = to_be_paid(amount, bill)
print(f"The amount due is: {due}")