def withdraw(account_number, pin, amount, accounts):
    user = accounts.get(account_number)
    if not user:
        return "Account not found."
    if user['pin'] != pin:
        return "Invalid PIN."
    if user['balance'] < amount:
        return "❌ Transaction declined: Insufficient funds."
    
    user['balance'] -= amount
    return f"✅ ₹{amount:.2f} withdrawn. New balance: ₹{user['balance']:.2f}"
