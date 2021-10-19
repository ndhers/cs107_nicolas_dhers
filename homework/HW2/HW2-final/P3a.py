def make_withdrawal(balance):
	def inner(withdrawal):
		if withdrawal > balance:
			raise ValueError('Not enough funds in balance to withdraw this amount of money')
		if withdrawal < 0:
			raise ValueError('Please enter a positive amount to withdraw')
		return (balance - withdrawal)
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

comments = 'Anormal behavior here: we withdrew $1500 dollars from the bank account\
 even though we only had $1000 left, the program should have raised an error.\
 This is because we have not updated the balance amount in our inner function. \n'

print(comments)