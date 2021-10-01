import matplotlib.pyplot as plt
from scipy.special import lambertw
import numpy as np
from sympy.solvers import solve
from sympy import Symbol
from functions import fun_poly, fun_trans, fun_poly_d, fun_trans_d, phi_fun_poly, phi_fun_trans, phi_fun_poly_d, \
    phi_fun_trans_d

eps1 = 10e-16
eps2 = 10e-10

a1 = 0.3
b1 = 2

a2 = 0
b2 = 0.5

q1 = 0.41  # Найдено исходя из графика производной фи функции трансцендентной функции
q2 = 0.46  # Аналогично первому случаю

x_absolute_poly = 2 - np.sqrt(3)
x_absolute_trans = 1.4776700622632155647870412477287370083390362290530360333937355564



print("poly(0) = ", fun_poly(a2), "poly(0.5) = ", fun_poly(b2), "poly(0) * poly(0.5) = ", fun_poly(a2) * fun_poly(b2))
print("trans(0.3) = ", fun_trans(a1), "trans(2) = ", fun_trans(b1), "trans(0.3) * trans(2) = ", fun_trans(a1) * fun_trans(b1))
print("phi_fun_trans(0.3) = ", phi_fun_trans(a1), "  phi_fun_trans(2) = ", phi_fun_trans(b1))
print("phi_fun_poly(0) = ", phi_fun_poly(a2), "  phi_fun_poly(0.5) = ", phi_fun_poly(b2) ,  "  phi_fun_poly(0.075) = ", phi_fun_poly(0.075))
print("phi_fun_poly_d(0) = ", phi_fun_poly_d(a2), "  phi_fun_poly_d(0.5) = ", phi_fun_poly_d(b2))
print("phi_fun_trans_d(0.3)   =    ", phi_fun_trans_d(0.3))




def machineEpsilon(value):
    while (1 + value) != 1:
        value /= 2
    return value


def bisection(fun, a, b, e, x_absolute):
    n = 0
    list_absolute_err = []
    list_iter = []
    if fun(a) * fun(b) >= 0:
        return None
    while (b - a) > e:
        c = (a + b) / 2
        list_absolute_err.append(abs(c - x_absolute))
        list_iter.append(n)
        n += 1
        if fun(a) * fun(c) < 0:
            b = c
        else:
            a = c
    x = (a + b) / 2
    # print("result = ", x, "iterations: ", n)
    return x, n, list_absolute_err, list_iter


def fixedPointIterations(phi_fun, e, x_first_approx, q, x_absolute):
    x_last = x_first_approx
    n = 0
    list_absolute_err = []
    list_iter = []
    while True:
        x = phi_fun(x_last)
        list_absolute_err.append(abs(x - x_absolute))
        list_iter.append(n)
        if abs(x - x_last) < ((1 - q) / q) * e:
            break
        x_last = x
        n += 1
    return x, n, list_absolute_err, list_iter


def fixedPointIterations_Aitken(phi_fun, phi_fun_d, e, x_first_approx, q, x_absolute):
    n = 0
    x0 = x_first_approx
    x1 = phi_fun(x0)
    x2 = phi_fun(x1)
    list_absolute_err = []
    list_iter = []
    while True:
        x2_t = (x1 * x1 - x2 * x0) / (2 * x1 - x2 - x0)
        x3 = phi_fun(x2_t)
        list_absolute_err.append(abs(x3 - x_absolute))
        list_iter.append(n)
        if abs(phi_fun_d(x0)) > 1:
            break
        if abs(x3 - x2_t) > ((1 - q) / q) * e:
            # if((phiFun(x3-e)*phiFun(x3+e))>0){
            x0 = x2_t
            x1 = x3
            x2 = phi_fun(x1)
        else:
            break
        n += 1
    # print("res = ", x3, "iterations: ", n)
    return x3, n, list_absolute_err, list_iter


def iter_from_epsilon_graph(read_file):
    read_file()
    plt.figure(1)
    plt.title("График зависимости количества итераций от эпсилон")
    plt.xlabel('точность epsilon')
    plt.ylabel('количество итераций')
    plt.xscale('log')
    plt.plot(read_file()[1], read_file()[0], label='Bisection for transcendental function')
    plt.legend()
    plt.grid()
    plt.show()


# Графики функций
_x1 = np.arange(a1, b1, 0.001)
_x2 = np.arange(a2, b2, 0.001)

# 1)График трансцендентной функции и полинома
plt.figure(1)
plt.title("Графики функций")
plt.ylabel('Y')
plt.xlabel('X')
plt.plot(_x1, fun_trans(_x1), label='(x - 1) ^ 2 - exp(-x)')
plt.plot(_x2, fun_poly(_x2), label='x ^ 4 - 10 * x ^ 2 - 16 * x + 5')
plt.legend()
plt.grid()

print(
    "-----------------------------------------------------------------------Bisection--------------------------------------------------------------------------------------------------------------")
print(
    "                                                                   (x - 1) ^ 2 - exp(-x)                                                                                                      ")
bisec1 = bisection(fun_trans, a1, b1, eps1, x_absolute_trans)
print("result: ", bisec1[0], "iterations: ", bisec1[1])
print(
    "                                                                x ^ 4 - 10 * x ^ 2 - 16 * x + 5                                                                                               ")
bisec2 = bisection(fun_poly, a2, b2, eps1, x_absolute_poly)
print("result: ", bisec2[0], "iterations: ", bisec2[1])

print(
    "------------------------------------------------------------------Fixed Point Iterations------------------------------------------------------------------------------------------------------")
print(
    "                                                     --            (x - 1) ^ 2 - exp(-x)                                                                                                      ")
fixed_p_i_1 = fixedPointIterations(phi_fun_trans, eps1, a1 + (b1 - a1) / 3, q1, x_absolute_trans)
print("result: ", fixed_p_i_1[0], "iterations: ", fixed_p_i_1[1])
print(
    "                                                                x ^ 4 - 10 * x ^ 2 - 16 * x + 5                                                                                               ")
fixed_p_i_2 = fixedPointIterations(phi_fun_poly, eps1, a1 + (b1 - a1) / 3, q2, x_absolute_poly)
print("result: ", fixed_p_i_2[0], "iterations: ", fixed_p_i_2[1])

print(
    "----------------------------------------------------------------------Eitken------------------------------------------------------------------------------------------------------------------")
print(
    "                                                                 (x - 1) ^ 2 - exp(-x)                                                                                                        ")
aitken1 = fixedPointIterations_Aitken(phi_fun_trans, phi_fun_trans_d, eps2, a1 + (b1 - a1) / 3, q1, x_absolute_trans)
print("result: ", aitken1[0], "iterations: ", aitken1[1])
print(
    "                                                                x ^ 4 - 10 * x ^ 2 - 16 * x + 5                                                                                               ")
aitken2 = fixedPointIterations_Aitken(phi_fun_poly, phi_fun_poly_d, eps2, a2 + (b2 - a2) / 3, q2, x_absolute_poly)
print("result: ", aitken2[0], "iterations: ", aitken2[1])


# Функция для получения данных и отрисовки графика зависимости количества итераций от точности
def iter_of_eps_bisec(method1, fun1, fun2, eps):
    e = eps
    list_eps = []
    list_iter1 = []
    list_iter2 = []
    for i in range(15):
        list_iter1.append(method1(fun1, a1, b1, e, x_absolute_trans)[1])
        list_iter2.append(method1(fun2, a2, b2, e, x_absolute_poly)[1])
        list_eps.append(e)
        e *= 10
    plt.figure(2)
    plt.title("График зависимости количества итераций от эпсилон")
    plt.xscale('log')
    plt.xlabel('epsilon')
    plt.ylabel('iterations')
    plt.plot(list_eps, list_iter1, label='Bisection transcendental function')
    plt.plot(list_eps, list_iter2, label='Bisection polynome')
    plt.legend()


def iter_of_eps_fixed_point(method2_1, fun1, fun2, x_first_approx1, x_first_approx2, q1, q2):
    e = eps1
    list_eps = []
    list_iter1 = []
    list_iter2 = []
    for i in range(15):
        list_iter1.append(method2_1(fun1, e, x_first_approx1, q1, x_absolute_trans)[1])
        list_iter2.append(method2_1(fun2, e, x_first_approx2, q2, x_absolute_poly)[1])
        list_eps.append(e)
        e *= 10
    plt.figure(2)
    plt.title("График зависимости количества итераций от эпсилон")
    plt.xscale('log')
    plt.xlabel('epsilon')
    plt.ylabel('iterations')
    plt.plot(list_eps, list_iter1, label='Fixed Point Iterations transcendental function')
    plt.plot(list_eps, list_iter2, label='Fixed Point Iterations polynome')
    plt.legend()


def iter_of_eps_aitken(method2_2, phi_fun1, phi_fun_d1, phi_fun2, phi_fun_d2, x_first_approx1, x_first_approx2, q1, q2):
    e = eps2
    list_eps = []
    list_iter1 = []
    list_iter2 = []
    for i in range(9):
        list_iter1.append(method2_2(phi_fun1, phi_fun_d1, e, x_first_approx1, q1, x_absolute_trans)[1])
        list_iter2.append(method2_2(phi_fun2, phi_fun_d2, e, x_first_approx2, q2, x_absolute_poly)[1])
        list_eps.append(e)
        e *= 10

    plt.figure(2)
    plt.title("График зависимости количества итераций от эпсилон")
    plt.xscale('log')
    plt.xlabel('epsilon')
    plt.ylabel('iterations')
    plt.plot(list_eps, list_iter1, label='Eitken transcendental function')
    plt.plot(list_eps, list_iter2, label='Eitken polynome')
    plt.legend()


iter_of_eps_bisec(bisection, fun_trans, fun_poly, eps1)
iter_of_eps_fixed_point(fixedPointIterations, phi_fun_trans, phi_fun_poly, a1 + (b1 - a1) / 3, a2 + (b2 - a2) / 3, q1,
                        q2)
iter_of_eps_aitken(fixedPointIterations_Aitken, phi_fun_trans, phi_fun_trans_d, phi_fun_poly, phi_fun_poly_d,
                   a1 + (b1 - a1) / 3, a2 + (b2 - a2) / 3, q1, q2)
plt.grid()


# # Функция для получения данных и отображения графиков зависимости погрешности от заданной точности
# def absolute_error_of_number_iter_bisec(method1, fun1, fun2, eps, x_absolute1, x_absolute2):
#     e = eps
#     list_absolute_err1 = []
#     list_absolute_err2 = []
#     list_eps = []
#     for i in range(10):
#         list_absolute_err1.append(abs(method1(fun1, a1, b1, e)[0] - x_absolute1))
#         list_absolute_err2.append(abs(method1(fun2, a2, b2, e)[0] - x_absolute2))
#         list_eps.append(e)
#         e *= 10
#     plt.figure(3)
#     plt.title("График зависимости погрешноси от заданной точности")
#     plt.xscale('log')
#     plt.xlabel('epsilon')
#     plt.ylabel('iterations')
#     plt.plot(list_eps, list_absolute_err1, label='Bisection transcendental function')
#     plt.plot(list_eps, list_absolute_err2, label='Bisection  polynome')
#     plt.legend()
#
#
# def absolute_error_of_number_iter_aitken(method2, phi_fun1, phi_fun_d1, phi_fun2, phi_fun_d2, x_first_approx1,
#                                          x_first_approx2,
#                                          x_absolute1, x_absolute2, eps):
#     e = eps
#     list_absolute_err1 = []
#     list_absolute_err2 = []
#     list_eps = []
#     for i in range(10):
#         list_absolute_err1.append(abs(method2(phi_fun1, phi_fun_d1, e, x_first_approx1, q1)[0] - x_absolute1))
#         list_absolute_err2.append(abs(method2(phi_fun2, phi_fun_d2, e, x_first_approx2, q2)[0] - x_absolute2))
#     plt.figure(3)
#     plt.title("График зависимости погрешноси от заданной точности")
#     plt.xscale('log')
#     plt.xlabel('epsilon')
#     plt.ylabel('absolute error')
#     plt.plot(list_eps, list_absolute_err1, label='Eitken transcendental function')
#     plt.plot(list_eps, list_absolute_err2, label='Eitken  polynome')
#     plt.legend()
#
#
# absolute_error_of_number_iter_bisec(bisection, fun_trans, fun_poly, eps1, x_absolute_trans, x_absolute_poly)
# absolute_error_of_number_iter_aitken(fixedPointIterations_Aitken, phi_fun_trans, phi_fun_trans_d, phi_fun_poly,
#                                      phi_fun_poly_d,
#                                      a1 + (b1 - a1) / 2, a2 + (b2 - a2) / 2, x_absolute_trans, x_absolute_poly, eps2)


def absolute_err_of_iter():
    plt.figure(4)
    plt.title("График зависимости погрешноси от итерации")
    plt.xlabel('iterations')
    plt.ylabel('absolute error')
    plt.yscale('log')
    plt.grid()
    plt.plot(bisec1[3], bisec1[2], label='Bisection transcendental function')
    plt.plot(bisec2[3], bisec2[2], label='Bisection  polynome')
    plt.plot(fixed_p_i_1[3], fixed_p_i_1[2], label='Fixed Point Iterations transcendental function')
    plt.plot(fixed_p_i_2[3], fixed_p_i_2[2], label='Fixed Point Iterations  polynome')
    plt.plot(aitken1[3], aitken1[2], label='Eitken transcendental function')
    plt.plot(aitken2[3], aitken2[2], label='Eitken  polynome')
    plt.legend()


absolute_err_of_iter()


# Function to get data and plot an addiction number of iterations from first approx
def iter_of_first_approx(method, fun1, fun2, e):
    a1_x = 0.47
    a2_x = -1.74
    b1_x = 2.47
    b2_x = 2.26
    list_iter1 = []
    list_iter2 = []
    list_a1_x = []
    list_a2_x = []
    list_b1_x = []
    list_b2_x = []
    for i in range(10):
        list_a1_x.append(a1_x)
        list_a2_x.append(a2_x)
        list_b1_x.append(b1_x)
        list_b2_x.append(b2_x)
        list_iter1.append(method(fun1, a1_x, b1_x, e, x_absolute_trans)[1])
        list_iter2.append(method(fun2, a2_x, b2_x, e, x_absolute_poly)[1])
        a1_x += 0.11
        b1_x -= 0.11
        a2_x += 0.22
        b2_x -= 0.22
    plt.figure(10)
    plt.ylabel('iterations')
    plt.xlabel('fisrt approx')
    plt.title("Зависимость количества итераций от начального приближения")
    plt.grid()
    plt.plot(list_a1_x, list_iter1, label='Bisection for transcendental fun', color='b')
    plt.plot(list_b1_x, list_iter1, color='b')
    plt.plot(list_a2_x, list_iter2, label='Bisection for polynome fun', color='r')
    plt.plot(list_b2_x, list_iter2, color='r')
    plt.legend()


iter_of_first_approx(bisection, fun_trans, fun_poly, eps1)

plt.figure(120)
plt.title("Производная фи функции алг уравнения и трансцендент")
plt.ylabel('Y')
plt.xlabel('X')
plt.plot(_x2, phi_fun_poly_d(_x2), label='производная фи функции полинома')
plt.plot(_x1, phi_fun_trans_d(_x1), label='производная фи функции трансцендентной функции')
plt.legend()
plt.grid()

# plt.figure(121)
# z = np.arange(-10000,10000,1)
# plt.grid()
# plt.plot(z,fun_poly(z))

plt.figure(121)
plt.grid()
plt.ylabel('Y')
plt.xlabel('X')
plt.plot(_x2, phi_fun_poly(_x2), label='phi pol')
plt.plot(_x1, phi_fun_trans(_x1), label='phi trans')

plt.legend()
plt.show()



# Find zeros of the functions
z = Symbol('x')
print("roots of transcendental : ", solve('(x - 1) ** 2 - exp(-x)', z))
print("roots of polynome : ", solve('x ** 4 - 10 * x ** 2 - 16 * x + 5', z))
