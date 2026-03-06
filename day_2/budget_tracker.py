def budget_tracker():
    """Simple budget tracker that calculates remaining balance after expenses."""
    
    print("=" * 50)
    print("SIMPLE BUDGET TRACKER")
    print("=" * 50)
    print()
    
    # Get total monthly budget
    while True:
        try:
            total_budget = float(input("Enter your total monthly budget (LKR): "))
            if total_budget < 0:
                print("Budget cannot be negative. Please enter a valid amount.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print()
    print("Enter your 3 expenses:")
    print("-" * 50)
    
    # Get 3 expenses
    expenses = []
    for i in range(1, 4):
        while True:
            try:
                expense = float(input(f"Expense {i} (LKR): "))
                if expense < 0:
                    print("Expense cannot be negative. Please enter a valid amount.")
                    continue
                expenses.append(expense)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    # Calculate total expenses
    total_expenses = sum(expenses)
    
    # Calculate remaining balance
    remaining_balance = total_budget - total_expenses
    
    # Display results
    print()
    print("=" * 50)
    print("BUDGET SUMMARY")
    print("=" * 50)
    print(f"Total Monthly Budget:  LKR {total_budget:,.2f}")
    print("-" * 50)
    print("Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"  Expense {i}:         LKR {expense:,.2f}")
    print("-" * 50)
    print(f"Total Expenses:        LKR {total_expenses:,.2f}")
    print("=" * 50)
    
    # Display remaining balance with color coding
    if remaining_balance >= 0:
        print(f"Remaining Balance:     LKR {remaining_balance:,.2f} ✓")
    else:
        print(f"Remaining Balance:     LKR {remaining_balance:,.2f} (OVERSPENT)")
    
    print("=" * 50)


if __name__ == "__main__":
    budget_tracker()
