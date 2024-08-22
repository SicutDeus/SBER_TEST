from typing import Type, Union

from marshmallow import fields, validate

from app.config import DATE_FORMAT, ERROR_MESSAGES


def get_numeric_field(
    field_type: Type[fields.Field],
    description: str,
    field_name: str,
    min_value: Union[int, float],
    max_value: Union[int, float],
) -> fields.Field:
    """
    Создает числовое поле для схемы Marshmallow с валидацией диапазона значений.

    Args:
        field_type (Type[fields.Field]): Тип поля, используемый для числовых данных
        (например, fields.Int, fields.Float).
        description (str): Описание поля.
        field_name (str): Имя поля, используемое для создания сообщений об ошибках.
        min_value (Union[int, float]): Минимальное допустимое значение для поля.
        max_value (Union[int, float]): Максимальное допустимое значение для поля.

    Returns:
        fields.Field: Поле Marshmallow с установленными требованиями и валидацией.
    """
    return field_type(
        required=True,
        description=description,
        validate=[
            validate.Range(
                min=min_value,
                max=max_value,
                error=ERROR_MESSAGES["invalid_" + field_name],
            ),
        ],
        error_messages={
            "required": ERROR_MESSAGES["required_field"] % "rate",
        },
    )


def get_date_field(
    field_type: Type[fields.Field], description: str, field_name: str
) -> fields.Field:
    """
    Создает поле даты для схемы Marshmallow
    с определенным форматом и сообщениями об ошибках.

    Args:
        field_type (Type[fields.Field]):
        Тип поля, используемый для данных типа дата
        (например, fields.Date / fields.Str).
        description (str): Описание поля.
        field_name (str): Имя поля, используемое для создания сообщений об ошибках.

    Returns:
        fields.Field: Поле Marshmallow с установленными форматом даты.
    """
    return field_type(
        required=True,
        format=DATE_FORMAT,
        description=description,
        error_messages={
            "required": ERROR_MESSAGES["required_field"] % field_name,
        },
    )
