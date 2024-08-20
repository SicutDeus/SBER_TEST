from calendar import monthrange
from collections import OrderedDict
from datetime import datetime
from typing import OrderedDict as OrderedDictType

from .config import DATE_FORMAT, FROM_PERCENT_COEF, MONTHS_IN_YEAR


def get_last_day_of_next_month(date: datetime) -> datetime:
    """
    Возвращает последний день следующего месяца относительно переданной даты.

    Args:
        date (datetime): Дата, от которой отсчитывается следующий месяц.

    Returns:
        datetime: Дата, представляющая последний день следующего месяца.
    """
    current_year, current_month = date.year, date.month

    if current_month == 12:
        next_year, next_month = current_year + 1, 1
    else:
        next_year, next_month = current_year, current_month + 1

    _, last_day = monthrange(next_year, next_month)
    return datetime(next_year, next_month, last_day)


def calculate_deposit(
    date: str,
    periods: int,
    amount: int,
    rate: float,
    *args,
    **kwargs,
) -> OrderedDictType[str, float]:
    """
    Рассчитывает сумму вклада на конец каждого месяца в течение заданного периода.

    Args:
        date (str): Дата начала вклада в формате "dd.mm.YYYY".
        periods (int): Количество периодов (месяцев), на которые рассчитывается вклад.
        amount (int): Начальная сумма вклада.
        rate (float): Процентная ставка по вкладу.

    Returns:
        OrderedDictType[str, float]: Упорядоченный словарь,
        где ключами являются даты (строки),
        а значениями — суммы на конец каждого месяца.
    """
    result: OrderedDictType[str, float] = OrderedDict()
    current_amount: float = amount
    current_date: datetime = datetime.strptime(date, DATE_FORMAT)

    for _ in range(periods):
        current_amount += current_amount * rate / MONTHS_IN_YEAR / FROM_PERCENT_COEF
        result[current_date.strftime(DATE_FORMAT)] = round(current_amount, 2)
        current_date = get_last_day_of_next_month(current_date)

    return result
