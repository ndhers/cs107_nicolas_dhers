from enum import Enum


class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2


class BankAccount():
    
    def __init__(self, owner, accountType: AccountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Unable to withdraw more money than the current balance.')
        elif amount < 0:
            raise ValueError('Unable to withdraw a negative amount.')
        else:
            self.balance = self.balance - amount
        
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Unable to deposit a negative amount.')
        else:
            self.balance = self.balance + amount

    def __str__(self):
        return f'The account owner is {self.owner}; the account type is {self.accountType.name}.'

    def __len__(self):
        return self.balance


class BankUser():  

    def __init__(self, owner):
        self.owner = owner
        self.account_obj = {}
    
    def addAccount(self, accountType):    
        if accountType in self.account_obj.keys():
            raise ValueError('Only one savings and checking account per user.')
        else:    
        	self.account_obj[accountType] = BankAccount(self.owner, accountType)
        
    def getBalance(self, accountType):
    	if accountType not in self.account_obj.keys():
    		raise ValueError(f'{accountType.name} account has not been created.')
    	else:
        	return len(self.account_obj[accountType])
        
    def deposit(self, accountType, amount):
        if accountType not in self.account_obj.keys():
            raise ValueError(f'{accountType.name} account has not been created.')
        else:
        	self.account_obj[accountType].deposit(amount)

    def withdraw(self, accountType, amount):
        if accountType not in self.account_obj.keys():
            raise ValueError(f'{accountType.name} account has not been created.')
        else:
        	self.account_obj[accountType].withdraw(amount)

    def __str__(self):
    	account_summary = []
    	for key,value in self.account_obj.items():
    		if key.value == 1: # value is SAVINGS or CHECKING and key is accountType object
    			account_summary.append(('Savings', len(value)))
    		else:
    			account_summary.append(('Checking', len(value)))
    	return f"Summary of {self.owner}'s accounts (type and balance): {account_summary}"


def ATMSession(bankUser):
	assert type(bankUser) == BankUser, Exception('Must pass BankUser object to ATM function.')
	def Interface():
		while (True):
			try:
				if not bankUser.account_obj.keys(): # prompt only 1)exit and 2)create account
					in_put = int(input("Enter Option:\n1)Exit\n2)Create Account\n"))
					if in_put not in [1,2]:
						print('Invalid input, try again with integer in [1-2].')
						continue
					if in_put == 1:
						return -1
					elif in_put == 2:
						account = int(input("Enter Option:\n1)Savings\n2)Checking\n"))
						if account not in [1,2]:
							print('Invalid input, try again with integer in [1-2].')
							continue
						account_type = AccountType(account)
						bankUser.addAccount(account_type)
						print(f"{account_type.name} account was just created.")
					continue
				else: # normal prompt
					in_put = int(input("Enter Option:\n1)Exit\n2)Create Account\
						\n3)Check Balance\n4)Deposit\n5)Withdraw\n"))
					if in_put == 1:
						return -1
					elif in_put in [2,3,4,5]:
						account = int(input("Enter Option:\n1)Savings\n2)Checking\n"))
						if account not in [1,2]:
							print('Invalid input, try again with integer in [1-2].')
							continue
						account_type = AccountType(account)
						if in_put == 2:
							bankUser.addAccount(account_type)
							print(f"{account_type.name} account was just created.")
						elif in_put == 3:
							print(f"{account_type.name} balance is: ${bankUser.getBalance(account_type)}")
						elif in_put == 4:
							deposit_amount = int(input("Please enter deposit amount (positive number required):"))
							bankUser.deposit(account_type, deposit_amount)
							print(f"${deposit_amount} deposit in {account_type.name} completed.")
						else:
							withdrawal_amount = int(input("Please enter withdrawal amount (positive number less than current balance required):"))
							bankUser.withdraw(account_type, withdrawal_amount)
							print(f"${withdrawal_amount} withdrawal from {account_type.name} completed.")
					else:
						print('Invalid input, try again with integer in [1-5].')
			except Exception as e:
				print(e)
	return Interface

# if __name__ == '__main__':
#     bankUser = BankUser('Nicolas')
#     new_session = ATMSession(bankUser)
#     new_session()    