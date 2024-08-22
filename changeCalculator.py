#from word2number import w2n

def calculate_change(total_cost, amount_given):
    
    currency = {
        '50000 won': 50000,
        '10000 won': 10000,
        '5000 won': 5000,
        '1000 won': 1000,
        '500 won': 500,
        '100 won': 100,
        '50 won': 50,
        '10 won': 10,
        '5 won': 5,
        '1 won': 1,
    }
    
    change = amount_given - total_cost
    
    if change < 0:
        print("The amount given is less then total cost")
        return
    
    change_to_give = {}
    
    for denomination, value in currency.items():
        if change >= value:
            count = change // value  
            change_to_give[denomination] = count
            change -= count * value 
    
    if change_to_give:
        print(f"\nTotal change to give back: {amount_given - total_cost} won")
        print("\nChange to give back:")
        for denomination, count in change_to_give.items():
            print(f"{denomination}:{count} pieces")
    else:
        print("No change to give back!")
        
try:
    total_cost = int(input("Enter the total cost (in won): "))
    amount_given = int(input("Enter the amount given (in won): "))
    
    calculate_change(total_cost, amount_given)
    
except ValueError:
    print("Please enter valid amount")

    
    
 