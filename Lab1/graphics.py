import matplotlib.pyplot as plt
import numpy as np
from sympy.solvers import solve
from sympy import Symbol

# Find zeros of the functions
z = Symbol('x')
print("roots of transcendental : ", solve('(x - 1) ** 2 - exp(-x)', z))
print("roots of polynome : ", solve('x ** 4 - 10 * x ** 2 - 16 * x + 5', z))

M2 = -35


def fun_trans(x):
    return (x - 1) ** 2 - np.exp(-x)


def fun_poly(x):
    return x ** 4 - 10 * x ** 2 - 16 * x + 5


def phi_fun_trans_d(x):
    return -np.exp(-x) / x - (np.exp(-x) - 1) / (x ** 2)


def phi_fun_poly_d(x):
    return 1 - (2 / M2) * (4 * x ** 3 - 20 * x - 16)


def read_file(file_name):
    Y, X = np.loadtxt(file_name, delimiter=' ', unpack=True)
    return Y, X


def iter_from_epsilon_graph(fun_read_file):
    plt.figure(13)
    plt.title("График зависимости количества итераций от эпсилон")
    plt.xlabel('точность epsilon')
    plt.ylabel('количество итераций')
    plt.xscale('log')
    plt.plot(fun_read_file('data_files_for_graphics/iter_from_eps.txt')[1],
             fun_read_file('data_files_for_graphics/iter_from_eps.txt')[0],
             label='Bisection Method Analitical Fun')
    plt.plot(fun_read_file('data_files_for_graphics/iter_from_eps_fpi.txt')[1],
             fun_read_file('data_files_for_graphics/iter_from_eps_fpi.txt')[0],
             label='Fixed Point Iterations Method Analitical Fun')
    plt.plot(fun_read_file('data_files_for_graphics/iter_from_eps_aitken.txt')[1],
             fun_read_file('data_files_for_graphics/iter_from_eps_aitken.txt')[0],
             label='Aitken Method Analitical Fun')
    plt.plot(fun_read_file('data_files_for_graphics/iter_from_eps2.txt')[1],
             fun_read_file('data_files_for_graphics/iter_from_eps2.txt')[0],
             label='Bisection Method Polynome')
    plt.plot(fun_read_file('data_files_for_graphics/iter_from_eps_fpi2.txt')[1],
             fun_read_file('data_files_for_graphics/iter_from_eps_fpi2.txt')[0],
             label='Fixed Point Iterations Method Polynome')
    plt.plot(fun_read_file('data_files_for_graphics/iter_from_eps_aitken2.txt')[1],
             fun_read_file('data_files_for_graphics/iter_from_eps_aitken2.txt')[0],
             label='Aitken Method Polynome')
    plt.legend()
    plt.grid()


iter_from_epsilon_graph(read_file)


def error_of_iter():
    plt.figure(1)
    plt.title("График зависимости абсолютной погрешности от интерации")
    plt.ylabel('погрешность')
    plt.xlabel('количество итераций')
    plt.yscale('log')
    plt.plot(read_file('data_files_for_graphics/error_of_iter_bisec.txt')[1],
             read_file('data_files_for_graphics/error_of_iter_bisec.txt')[0], 'r',
             label='Bisection Method transcendental fun', )
    plt.plot(read_file('data_files_for_graphics/error_of_iter_bisec2.txt')[1],
             read_file('data_files_for_graphics/error_of_iter_bisec2.txt')[0], 'y',
             label='Bisection Method for polynome', )

    plt.plot(read_file('data_files_for_graphics/error_of_iter_fpi1.txt')[1],
             read_file('data_files_for_graphics/error_of_iter_fpi1.txt')[0], 'b',
             label='Fixed Point Iterations for transcendental fun', )
    plt.plot(read_file('data_files_for_graphics/error_of_iter_fpi2.txt')[1],
             read_file('data_files_for_graphics/error_of_iter_fpi2.txt')[0], 'g',
             label='Fixed POint Iterations for polynome', )

    plt.plot(read_file('data_files_for_graphics/error_of_iter_aitken1.txt')[1],
             read_file('data_files_for_graphics/error_of_iter_aitken1.txt')[0], 'b',
             label='Aitken for transcendental fun', )
    plt.plot(read_file('data_files_for_graphics/error_of_iter_aitken2.txt')[1],
             read_file('data_files_for_graphics/error_of_iter_aitken2.txt')[0], 'g',
             label='Aitken for polynome', )

    plt.legend()
    plt.grid()


# def iter_of_approx():
#     plt.figure(12)
#     plt.title("График зависимости колличества итераций от начального приближени€")
#     plt.xlabel('начальная точка')
#     plt.ylabel('количество итераций')
#     plt.yscale('log')
#     plt.plot(read_file('BiSec_iter_of_prib_analit.txt')[1], read_file('BiSec_iter_of_prib_analit.txt')[0], 'r',
#              label='BiSection_for_analit', )
#     plt.plot(read_file('BiSec_iter_of_prib_tranc.txt')[1], read_file('BiSec_iter_of_prib_tranc.txt')[0], 'y',
#              label='BiSection_for_tranc', )
#
#     plt.plot(read_file('Newtone_iter_of_prib_analit.txt')[1], read_file('Newtone_iter_of_prib_analit.txt')[0], 'b',
#              label='Newtone_for_analit', )
#     plt.plot(read_file('Newtone_iter_of_prib_tranc.txt')[1], read_file('Newtone_iter_of_prib_tranc.txt')[0], 'g',
#              label='Newtone_for_tranc', )
#     plt.legend()
#     plt.grid()


error_of_iter()

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


def graph():
    # Графики функций
    _x1 = np.arange(a1, b1, 0.001)
    _x2 = np.arange(a2, b2, 0.001)

    # 1)График трансцендентной функции и полинома
    plt.figure(3)
    plt.title("Графики функций")
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.text(b2 - 0.1, 0, "»", verticalalignment='center', horizontalalignment='center')
    plt.text(x_absolute_poly, 0, "0", verticalalignment='center', horizontalalignment='center')
    plt.text(a2 + 0.1, 0, "«", verticalalignment='center', horizontalalignment='center')
    plt.plot(_x1, fun_trans(_x1), label='(x - 1) ^ 2 - exp(-x)')
    plt.plot(_x2, fun_poly(_x2), label='x ^ 4 - 10 * x ^ 2 - 16 * x + 5')
    plt.legend()
    plt.text(b1 - 0.35, 0, "»", verticalalignment='center', horizontalalignment='center')
    plt.text(x_absolute_trans, 0, "0", verticalalignment='center', horizontalalignment='center')
    plt.text(a1 + 1, 0, "«", verticalalignment='center', horizontalalignment='center')

    plt.grid()
    plt.legend()


def error_of_eps():
    plt.figure(2)
    plt.title("График зависимости абсолютной погрешности от эпсилон")
    plt.xlabel('точность epsilon')
    plt.ylabel('погрешность')
    plt.xscale('log')
    plt.plot(read_file('data_files_for_graphics/error_of_eps_bisec.txt')[1],
             read_file('data_files_for_graphics/error_of_eps_bisec.txt')[0],
             label='Bisection Method Analitical Fun')
    plt.plot(read_file('data_files_for_graphics/error_of_eps_fpi.txt')[1],
             read_file('data_files_for_graphics/error_of_eps_fpi.txt')[0],
             label='Fixed Point Iterations Method Analitical Fun')
    plt.plot(read_file('data_files_for_graphics/error_of_eps_aitken.txt')[1],
             read_file('data_files_for_graphics/error_of_eps_aitken.txt')[0],
             label='Aitken Method Analitical Fun')
    plt.plot(read_file('data_files_for_graphics/error_of_eps_bisec2.txt')[1],
             read_file('data_files_for_graphics/error_of_eps_bisec2.txt')[0],
             label='Bisection Method Polynome')
    plt.plot(read_file('data_files_for_graphics/error_of_eps_fpi2.txt')[1],
             read_file('data_files_for_graphics/error_of_eps_fpi2.txt')[0],
             label='Fixed Point Iterations Method Polynome')
    plt.plot(read_file('data_files_for_graphics/error_of_eps_aitken2.txt')[1],
             read_file('data_files_for_graphics/error_of_eps_aitken2.txt')[0],
             label='Aitken Method Polynome')
    plt.legend()
    plt.grid()


def graph_phi_fun_d():
    _x1 = np.arange(a1, b1, 0.001)
    _x2 = np.arange(a2, b2, 0.001)

    plt.figure(125)
    plt.title("Производная фи функции алг уравнения и трансцендент")
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.plot(_x2, phi_fun_poly_d(_x2), label='производная фи функции полинома')
    plt.plot(_x1, phi_fun_trans_d(_x1), label='производная фи функции трансцендентной функции')
    plt.legend()
    plt.grid()


graph()
error_of_eps()
graph_phi_fun_d()
plt.show()
