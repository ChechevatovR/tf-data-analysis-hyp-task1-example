import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 782395183  # Ваш chat ID, не меняйте название переменной


def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    alpha = 0.09
    n = x_cnt
    p_x_cap = x_success / x_cnt
    m = y_cnt
    p_y_cap = y_success / y_cnt

    P = (n * p_x_cap + m * p_y_cap) / (n + m)
    Z = (p_x_cap - p_y_cap) / ((P * (1 - P) * (1 / n + 1 / m)) ** .5)

    q = norm.ppf(alpha)
    result = Z < q
    return result
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # return ... # Ваш ответ, True или False
