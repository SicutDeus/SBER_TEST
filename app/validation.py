import typing
from datetime import datetime

from marshmallow import INCLUDE, Schema, ValidationError, fields, pre_load, validates

from .config import (
    DATE_FORMAT,
    ERROR_MESSAGES,
    FIELDS_TYPES,
    MAX_AMOUNT,
    MAX_PERIODS,
    MAX_RATE,
    MIN_AMOUNT,
    MIN_PERIODS,
    MIN_RATE,
)
from .fields import get_date_field, get_numeric_field


class DepositRequestSchema(Schema):
    """
    Схема валидации запроса на расчет вклада.

    Включает в себя поля: дата, количество месяцев, сумма вклада и процентная ставка,
    а также методы для проверки типов данных и корректности формата даты.
    """

    date: fields.Str = get_date_field(
        fields.Str,
        "Дата заявки в формате dd.mm.YYYY",
        "date",
    )
    periods: fields.Int = get_numeric_field(
        fields.Int,
        "Количество месяцев по вкладу",
        "periods",
        MIN_PERIODS,
        MAX_PERIODS,
    )
    amount: fields.Int = get_numeric_field(
        fields.Int,
        "Сумма вклада",
        "amount",
        MIN_AMOUNT,
        MAX_AMOUNT,
    )
    rate: fields.Float = get_numeric_field(
        fields.Float,
        "Процентная ставка по вкладу",
        "rate",
        MIN_RATE,
        MAX_RATE,
    )

    class Meta:
        unknown = INCLUDE

    @pre_load
    def check_types(
        self, data: typing.Dict[str, typing.Any], **kwargs
    ) -> typing.Dict[str, typing.Any]:
        """
        Проверяет, что типы полей в запросе соответствуют ожидаемым.

        Args:
            data (typing.Dict[str, typing.Any]): Входные данные для валидации.

        Raises:
            ValidationError: Если тип данных не соответствует ожидаемому.

        Returns:
            typing.Dict[str, typing.Any]: Данные после проверки типов.
        """
        for field_name, value in data.items():
            expected_types = FIELDS_TYPES.get(field_name, None)
            if expected_types and not isinstance(value, expected_types):
                expected_type_msg = "/".join(
                    [expected_type.__name__ for expected_type in expected_types]
                )
                raise ValidationError(
                    ERROR_MESSAGES["invalid_type"]
                    % (field_name, expected_type_msg, type(value).__name__),
                    field_name=field_name,
                )
        return data

    @validates("date")
    def validate_date(self, value: str) -> None:
        """
        Проверяет, что дата соответствует формату dd.mm.YYYY.

        Args:
            value (str): Дата для проверки.

        Raises:
            ValidationError: Если дата не соответствует ожидаемому формату.
        """
        try:
            datetime.strptime(value, DATE_FORMAT)
        except ValueError:
            raise ValidationError(ERROR_MESSAGES["invalid_date_format"])

    def validate(self, *args, **kwargs) -> str:
        """
        Переопределяет метод валидации, возвращая ошибки в необходимом формате.

        Returns:
            str: Строка с описанием ошибок валидации, если они есть.
        """
        result = super().validate(*args, **kwargs)
        return "".join(
            [f"{key}: {'. '.join(values)}" for key, values in result.items()]
        )
