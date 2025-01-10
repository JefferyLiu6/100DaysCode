# Tip Calculator

A simple Python script to calculate the tip and evenly split the total bill among a group of people.

---

## How It Works

1. The script prompts the user to input:
   - The total bill amount.
   - The tip percentage they want to give (e.g., 10%, 12%, or 15%).
   - The number of people to split the bill.
2. It calculates:
   - The total tip amount.
   - The total bill (including the tip).
   - The amount each person should pay, rounded to 2 decimal places.
3. The result is displayed, showing how much each person should pay.

---

## Code Example

```python
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_per = tip/100  # tip in percent
total_tip = bill*tip_per
tot_bill = bill + total_tip

bill_per_person = tot_bill/people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
```
