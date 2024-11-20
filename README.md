# Currency Change Calculator

The **Currency Change Calculator** is a simple Python script designed to calculate and display the breakdown of change to be returned when a customer makes a payment in Korean won (₩). The script determines the number of currency denominations (notes and coins) needed to give back the exact change.

## Features

- **Change Breakdown**: Calculates the exact number of each denomination (notes and coins) needed to return the change.
- **User Input Validation**: Ensures that inputs are valid integers.
- **Custom Error Handling**: Notifies users if the amount given is insufficient or inputs are invalid.
- **Supports Korean Currency**: Handles standard Korean currency denominations, including notes and coins.

## How to Run

1. **Clone or Download the Script**:
   - Clone the repository or copy the script to your local machine.

2. **Run the Script**:
   - Use Python to run the script in your terminal:
     ```bash
     python currency_change_calculator.py
     ```

3. **Provide Inputs**:
   - Enter the total cost of the purchase.
   - Enter the amount given by the customer.
   - The script will calculate the change and display a breakdown of denominations.

## Example

**Input:**
```plaintext
Enter the total cost (in won): 7800
Enter the amount given (in won): 10000
