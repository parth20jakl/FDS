def deposit(balance, amount):
    """Function to deposit an amount into the account."""
    return balance + amount

def withdraw(balance, amount):
    """Function to withdraw an amount from the account, ensuring no negative balance."""
    if balance >= amount:
        return balance - amount
    else:
        print("Withdrawal denied: Insufficient funds.")
        return balance

def main():
    balance = 0  # Initial balance

    # Input transaction log
    transaction_log = input("Enter transactions (e.g., 'D 300, W 200'): ")
    transactions = transaction_log.split(", ")

    for transaction in transactions:
        action, amount = transaction.split()
        amount = int(amount)

        if action == 'D':
            balance = deposit(balance, amount)
        elif action == 'W':
            balance = withdraw(balance, amount)
        else:
            print(f"Invalid transaction type: {action}")

    print(f"Net balance: {balance}")

if __name__ == "__main__":
    main()