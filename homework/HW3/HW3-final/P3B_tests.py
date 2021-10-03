from Bank import BankAccount, BankUser, AccountType

# Running tests:
def test_over_withdrawal():
    print("Checking implementation of error messages:")
    user = BankUser("Nicolas")
    user.addAccount(AccountType.SAVINGS)
    user.deposit(AccountType.SAVINGS, 10000)

    # test with negative value deposit
    try:
        user.deposit(AccountType.SAVINGS, -100)
    except Exception as e:
        print(e)

    # test with negative value withdrawal
    try:
        user.withdraw(AccountType.SAVINGS, -100)
    except Exception as e:
        print(e)    

    # test withdrawing more than available balance
    try:
        user.withdraw(AccountType.SAVINGS, 11000)
    except Exception as e:
        print(e)

    # test withdrawing in non-existing account
    try:
        user.withdraw(AccountType.CHECKING, 10000)
    except Exception as e:
        print(e)

    # test deposit in non-existing account
    try:
        user.deposit(AccountType.CHECKING, 10000)
    except Exception as e:
        print(e)       

    # test more than 1 savings account
    try:
        user.addAccount(AccountType.SAVINGS)
    except Exception as e:
        print(e)

    # Test get balance from non-existing account
    try:
        user.getBalance(AccountType.CHECKING)
    except Exception as e:
        print(e)

    # Test to see if methods and classes work properly:
    print("\nChecking if methods work properly:")
    user.deposit(AccountType.SAVINGS, 1000) # total should be 10000+1000 = 11000
    user.withdraw(AccountType.SAVINGS, 5000) # total should be 11000 - 5000 = 6000
    print(f"Current balance in account is {user.getBalance(AccountType.SAVINGS)}")
    print(user)
    user.addAccount(AccountType.CHECKING) # adding CHECKING account
    user.deposit(AccountType.CHECKING, 1100)
    user.withdraw(AccountType.CHECKING, 500) # Total in Checking should now be 600
    print(f"Current balance in account is {user.getBalance(AccountType.CHECKING)}")
    print(user)


test_over_withdrawal()


'''
Outputs:
****************************************************************************
Checking implementation of error messages:
Unable to deposit a negative amount.
Unable to withdraw a negative amount.
Unable to withdraw more money than the current balance.
CHECKING account has not been created.
CHECKING account has not been created.
Only one savings and checking account per user.
CHECKING account has not been created.

Checking if methods work properly:
Current balance in account is 6000
Summary of Nicolas's accounts (type and balance): [('Savings', 6000)]
Current balance in account is 600
Summary of Nicolas's accounts (type and balance): [('Savings', 6000), ('Checking', 600)]
'''