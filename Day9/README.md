# Silent Auction Program

This is a Python script for running a silent auction. It allows multiple users to place bids, stores their information, and determines the winner with the highest bid.

---

## Features

- Allows users to input their name and bid amount.
- Handles multiple bidders in a silent auction format.
- Determines the winner with the highest bid.
- Displays the winning bidder and the bid amount at the end of the auction.

---

## Prerequisites

- Python 3.x installed on your machine.
- The `art` Python package for displaying a decorative logo. Install it using:
  ```bash
  pip install art
  ```

---

## Usage

1. Clone this repository or copy the script to your local environment.
2. Ensure you have Python 3.x installed.
3. Run the script:
   ```bash
   python silent_auction.py
   ```
4. Follow the interactive prompts:
   - Enter your name and bid.
   - Indicate whether there are more bidders.

### Example Interaction

#### Input:
```
What is your name?: Alice
What is your bid?: $300
Are there any other bidders? Type 'yes or 'no'.
yes

What is your name?: Bob
What is your bid?: $400
Are there any other bidders? Type 'yes or 'no'.
no
```

#### Output:
```
The winner is Bob with a bid of $400
```