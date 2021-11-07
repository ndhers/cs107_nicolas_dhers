class AutoDiffToy():
    def __init__(self, val, der=1.0):
        self.val = val
        self.der = der

    def __add__(self, other):
        try:
            new_val = other.val + self.val
            new_der = other.der + self.der
        except AttributeError:
            new_val = other + self.val
            new_der = self.der
        return AutoDiffToy(new_val, new_der)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        try:
            new_val = self.val * other.val
            new_der = self.der * other.val + self.val * other.der
        except AttributeError:
            new_val = self.val * other
            new_der = self.der * other
        return AutoDiffToy(new_val, new_der)

    def __rmul__(self, other):
        return self.__mul__(other)


if __name__ == '__main__':
    a = 2.0
    x = AutoDiffToy(a)
    alpha = 2.0
    beta = 3.0

    f_strings = ["alpha*x + beta", "x*alpha + beta",
             "beta + alpha*x", "beta + x*alpha"]
    fs = [alpha * x + beta, x * alpha + beta, beta + alpha * x, beta + x * alpha]
    print(f"Using parameters and x as: alpha {alpha}, beta {beta}, x {x.val}")
    for i,f in enumerate(fs):
        print(f"For f = {f_strings[i]}, we obtain a function value of {f.val} and derivative\
 of {f.der}.")


    ## Testing mul
    # b = 3.0
    # y = AutoDiffToy(b)
    # print(f"for y*2*3*x, we get a value of {(y*alpha*beta*x).val} and a derivative of {(y*alpha*beta*x).der}")

'''
Demo output:
Using parameters and x as: alpha 2.0, beta 3.0, x 2.0
For f = alpha*x + beta, we obtain a function value of 7.0 and derivative of 2.0.
For f = x*alpha + beta, we obtain a function value of 7.0 and derivative of 2.0.
For f = beta + alpha*x, we obtain a function value of 7.0 and derivative of 2.0.
For f = beta + x*alpha, we obtain a function value of 7.0 and derivative of 2.0.
'''
