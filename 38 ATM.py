def check_balance(account_number, accounts):
    if account_number in accounts:
        return f"Your current balance is ₹{accounts[account_number]['balance']:.2f}"
    else:
        return "Account not found."
accounts = {
    '123456': {
        'name': 'John Doe',
        'pin': '4321',
        'balance': 10000.0
    },
    '987654': {
        'name': 'Jane Smith',
        'pin': '1234',
        'balance': 8000.0
    }
}
def withdraw(account_number, pin, amount, accounts):
    if account_number not in accounts:
        return "Account not found."

    user = accounts[account_number]
    if user['pin'] != pin:
        return "Invalid PIN."

    if user['balance'] < amount:
        return "Insufficient funds."

    user['balance'] -= amount
    return f"Withdrawal successful. New balance: ₹{user['balance']:.2f}"
