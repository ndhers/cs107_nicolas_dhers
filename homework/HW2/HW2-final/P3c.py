def make_withdrawal(balance):
	def inner(withdrawal):
		nonlocal balance
		if withdrawal > balance:
			raise ValueError('Not enough funds in balance to withdraw this amount of money')
		if withdrawal < 0:
			raise ValueError('Please enter a positive amount to withdraw')
		balance = balance - withdrawal
		return (balance)
	return inner

### Demo:

init_balance = 5000 # initial balance equal to $5000
wd = make_withdrawal(init_balance)

withdrawal_amount = 4000 # withdrawing $4000
wd_1 = wd(withdrawal_amount)
print(wd_1)

new_withdrawal_amount = 1500 # withdrawing another $1500
wd_2 = wd(new_withdrawal_amount)
print(wd_2)

comments = 'Having set balance to a nonlocal variable, we have solved our problem. The above \
code now returns an error because we are trying to withdraw too much money from our bank account\
in the second step.\n'

print(comments)