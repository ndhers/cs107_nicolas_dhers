def make_withdrawal(balance):
	def inner(withdrawal):
		if withdrawal > balance:
			raise ValueError('Not enough funds in balance to withdraw this amount of money')
		if withdrawal < 0:
			raise ValueError('Please enter a positive amount to withdraw')
		balance = balance - withdrawal
		return (balance)
	return inner

comments = 'Error raised: local variable "balance" referenced before assignment \
This is due to data encapsulation; once the init_balance intially passed to make_withdrawal\
is captured by the inner function, it cannot be changed anymore. "balance" is bound to the parent\
block of the inner function.\n'

print(comments)

### Demo:

init_balance = 5000 # initial balance equal to $5000
wd = make_withdrawal(init_balance)

withdrawal_amount = 4000 # withdrawing $4000
wd_1 = wd(withdrawal_amount)
print(wd_1)

new_withdrawal_amount = 1500 # withdrawing another $1500
wd_2 = wd(new_withdrawal_amount)
print(wd_2)