from typing import Dict, Tuple, Type, Union

# Валидация даты
DATE_FORMAT: str = "%d.%m.%Y"

# Валидация периодов
MIN_PERIODS: int = 1
MAX_PERIODS: int = 60

# Валидация суммы вклада
MIN_AMOUNT: int = 10000
MAX_AMOUNT: int = 3000000

# Валидация процентной ставки
MIN_RATE: float = 1.0
MAX_RATE: float = 8.0

BASE_SUCCESS_STRATUS_CODE: int = 200
BASE_ERROR_STATUS_CODE: int = 400

MONTHS_IN_YEAR: int = 12
FROM_PERCENT_COEF: int = 100

# Типы входных полей
FIELDS_TYPES: Dict[str, Tuple[Union[Type[str], Type[int], Type[float]], ...]] = {
    "date": (str,),
    "periods": (int,),
    "amount": (int,),
    "rate": (float, int),
}

# Ошибки валидации
ERROR_MESSAGES: Dict[str, str] = {
    "invalid_date_format": f"Некорректный формат даты. "
    f"Используйте формат {DATE_FORMAT}.",
    "invalid_periods": f"Количество месяцев"
    f" по вкладу должно быть от {MIN_PERIODS} до {MAX_PERIODS}."
    " Было получено {input}. ",
    "invalid_amount": f"Сумма вклада должна быть от {MIN_AMOUNT} до {MAX_AMOUNT}."
    + " Было получено {input}. ",
    "invalid_rate": f"Процентная ставка должна быть от {MIN_RATE} до {MAX_RATE}."
    + " Было получено {input}. ",
    "invalid_type": "Неверный тип поля %s: ожидался %s, был получен %s",
    "required_field": "Поле %s обязательное. ",
}

