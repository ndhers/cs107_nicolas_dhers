def my_pow(x,r):
	return (x**r,r*x**(r-1))

if __name__ == "__main__":
	f,f_prime = my_pow(3,4)
	print(f"For x=3, r=4, we obtain $f(x)$={f} and $f'(x)$={f_prime}.")