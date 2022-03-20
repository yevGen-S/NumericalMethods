from runge_kutta_4order import runge_kutta_4order
import numpy as np
import matplotlib.pyplot as plt

# Driver method

x0 = 0.1
x = 1


def compare_exact_result_and_method(x0, x):
    plt.figure(1)
    x0 = x0
    y0 = np.sqrt(x0)
    z0 = 1 / (2 * (np.sqrt(x0)))

    x = x
    h = (x - x0)

    interval = np.linspace(x0, x, 20)
    plt.scatter(interval, np.sqrt(interval), label='exact result')

    for eps in ([1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7]):
        runge_res = runge_kutta_4order(x0, y0, z0, x, h, eps)

        plt.plot(runge_res[0][0], runge_res[0][1], label=f'runge eps = {eps}')
    plt.legend()
    plt.grid()
    plt.title("Сравнение точного ответа и полученного в методе.")
    plt.savefig("./images_[0.1,1]/compare_exact_result_and_method")


def number_of_iters_of_defined_eps(x0, x):
    plt.figure(2)
    x0 = x0
    y0 = np.sqrt(x0)
    z0 = 1 / (2 * (np.sqrt(x0)))

    x = x
    h = (x - x0)

    eps = 1e-1
    eps_arr = []
    iter_arr = []
    for i in range(10):
        runge_res = runge_kutta_4order(x0, y0, z0, x, h, eps)
        eps_arr.append(eps)
        iter_arr.append(runge_res[2][-1])
        eps = eps / 10

    # plt.xscale('log')
    plt.plot(eps_arr, iter_arr)
    plt.xlabel("eps")
    plt.ylabel("iterations")
    plt.grid()
    plt.title("Зависимость количества итераций от задаваемой точности.")
    plt.savefig("./images_[0.1,1]/number_of_iters_of_defined_eps")


def expiremental_eps_of_defined_eps(x0, x):
    plt.figure(3)
    x0 = x0
    y0 = np.sqrt(x0)
    z0 = 1 / (2 * (np.sqrt(x0)))

    x = x
    h = (x - x0)

    eps = 1e-1
    exact_eps = []
    experimatal_eps = []
    for i in range(10):
        runge_res = runge_kutta_4order(x0, y0, z0, x, h, eps)
        exact_eps.append(eps)
        experimatal_eps.append(runge_res[1][-1])
        eps = eps / 10

    plt.xscale('log')
    plt.yscale('log')

    plt.plot(exact_eps, exact_eps, label='bisectrice')
    plt.plot(experimatal_eps, exact_eps, label='runge-kutta')
    plt.xlabel("задаваемое eps")
    plt.ylabel("экспериментальное eps")
    plt.grid()
    plt.legend()
    plt.title("Зависимость абсолютной ошибки от задаваемой точности.")
    plt.savefig("./images_[0.1,1]/expiremental_eps_of_defined_eps")


def step_of_defined_eps(x0, x):
    plt.figure(4)
    x0 = x0
    y0 = np.sqrt(x0)
    z0 = 1 / (2 * (np.sqrt(x0)))

    x = x
    h = (x - x0)

    eps = 1e-1
    eps_arr = []
    step = []
    for i in range(10):
        runge_res = runge_kutta_4order(x0, y0, z0, x, h, eps)
        eps_arr.append(eps)
        step.append(runge_res[3])
        eps = eps / 10

    plt.xscale('log')
    plt.plot(eps_arr, step, label='runge-kutta')
    plt.xlabel("задаваемое eps")
    plt.ylabel("шаг")
    plt.grid()
    plt.legend()
    plt.title("Зависимость шага от задаваемой точности.")
    plt.savefig("./images_[0.1,1]/step_of_defined_eps")


def relative_err_of_start_conditions_changes(x0, x):
    plt.figure(5)
    x0 = x0
    y0 = np.sqrt(x0)
    z0 = 1 / (2 * (np.sqrt(x0)))

    x = x
    h = (x - x0)
    eps = 1e-10

    relative_err = []
    err_arr = []

    z_with_err = z0

    for k in range(1, 6):
        err = float(f"0.0{k}")
        z_with_err = z0 * (1 + err)
        runge_res = runge_kutta_4order(x0, y0, z_with_err, x, h, eps)
        x_arr = runge_res[0][0]
        y_arr = np.sqrt(x_arr)

        relative_err.append(max([abs((y_arr[i] - runge_res[0][1][i]) / y_arr[i]) for i in range(len(y_arr))]))
        err_arr.append(err)

    # plt.xscale('log')
    plt.plot(err_arr, relative_err, label='runge-kutta')
    plt.xlabel("внесенная в начальные данные ошибка")
    plt.ylabel("относительная ошибка результата")
    plt.grid()
    plt.legend()
    plt.title("Зависимость относительной ошибки \nот ошибки внесенной в начальные данные.")
    plt.savefig("./images_[0.1,1]/relative_err_of_start_conditions_changes")


compare_exact_result_and_method(x0, x)
number_of_iters_of_defined_eps(x0, x)
expiremental_eps_of_defined_eps(x0, x)
step_of_defined_eps(x0, x)
relative_err_of_start_conditions_changes(x0, x)
plt.show()
