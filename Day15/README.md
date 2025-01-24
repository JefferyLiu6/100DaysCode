# Coffee Machine Program

This is a Python implementation of a **Coffee Machine Program** that simulates the functioning of a coffee vending machine. Users can select their desired drink, pay for it using virtual coins, and the program ensures sufficient resources are available to prepare the drink.

---

## Features

- **Drink Options**:
  - Espresso
  - Latte
  - Cappuccino
- **Reports**:
  - Displays current resource levels (water, milk, coffee, and profit).
- **Resource Management**:
  - Checks if enough ingredients are available to prepare the selected drink.
  - Deducts resources when a drink is prepared.
- **Coin Handling**:
  - Accepts virtual coins (quarters, dimes, nickels, pennies).
  - Calculates and provides change if the payment exceeds the drink cost.
  - Refunds money if the payment is insufficient.
- **Shutdown Command**:
  - `off`: Stops the program.

---

## Usage

1. Clone this repository or copy the script to your local environment.
2. Run the script:
   ```bash
   python coffee_machine.py
   ```
3. Follow the interactive prompts to:
   - Select a drink.
   - Insert coins.
   - Check resource reports.
   - Enjoy your coffee!