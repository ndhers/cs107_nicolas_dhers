import numpy as np
import matplotlib.pyplot as plt

def numerical_diff(f,h):
	def inner(x):
		return (f(x+h)-f(x))/h
	return inner

def ln_func(x):
	return np.log(x)

x_space = np.linspace(0.2,0.4,100)
f_prime_list_1 = [numerical_diff(ln_func,0.1)(x) for x in x_space]
f_prime_list_2 = [numerical_diff(ln_func,10**(-7))(x) for x in x_space]
f_prime_list_3 = [numerical_diff(ln_func,10**(-15))(x) for x in x_space]

plt.figure(figsize = (8,6))
plt.plot(x_space, 1/x_space, 'kx--', markersize = 4, label = 'exact derivative')
plt.plot(x_space, f_prime_list_1, label = 'h=1e-1')
plt.plot(x_space, f_prime_list_2, label = 'h=1e-7')
plt.plot(x_space, f_prime_list_3, label = 'h=1e-15')
plt.xlabel('$x$', fontsize = 15)
plt.ylabel("$f'(x)$", fontsize = 15)
plt.title('Comparison of finite differences and exact derivative for $ln(x)$')
plt.legend()
# plt.savefig('P1_fig.png')

print("Answer to Q-a: the value of 1e-7 most closely approximates the true derivative.\
	When h is too small, rounding error occurs when we take the difference of two very similar\
	numbers f(x+h) and f(x). This error is also known as subtractive cancellation error,\
	and is due to finite computer arithmetics. It is shown here with the h=1e-15 case.\
	When h is too large, our step size is not small enough to capture close to the\
	slope of the curve at the point. This error is attributed to truncation error.\
	This is shown in our plot for h=1e-1.")

print("Answer to Q-b: In AD, we break down the original function into child functions\
	which are analytically computed and combined through simple arithmetic operations.\
	By taking individual analytical derivatives of these composite functions and using\
	chain rule, we can reconstruct the original function's derivative without having induced\
	any truncation or substantial round-off errors like in the case of finite differences.\
	We therefore end up with an exact derivative evaluation through correct use of AD.")
# plt.show()


