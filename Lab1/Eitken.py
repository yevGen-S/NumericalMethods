
from functions import fun_poly, fun_trans, fun_poly_d, fun_trans_d, phi_fun_poly, phi_fun_trans, phi_fun_poly_d, \
    phi_fun_trans_d

eps = 10e-10
a1 = 0.75
b1 = 2
a2 = 0
b2 = 1
q1 = 0.3085
q2 = 3.0025



def fixedPointIterations_Eitken(phi_fun, phi_fun_d, e, x_first_approx, q = 0.308):
    n = 0
    x0 = x_first_approx
    x1 = phi_fun(x0)
    x2 = phi_fun(x1)
    while True:
        x2_t = (x1 * x1 - x2 * x0) / (2 * x1 - x2 - x0)
        x3 = phi_fun(x2_t)
        if abs(phi_fun_d(x0)) > 1:
            break
        if abs(x3 - x2_t) > ((1 - q) / q) * e:
            # if((phiFun(x3-e)*phiFun(x3+e))>0){
            x0 = x2_t
            x1 = x3
            x2 = phi_fun(x1)
        else:
            break
        print("res = ", x3)
        n += 1
    return x3, n



print(fixedPointIterations_Eitken(phi_fun_trans,phi_fun_trans_d,eps,0.5,q1))