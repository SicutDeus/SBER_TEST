from typing import Any, Dict, Tuple, Union

from flasgger import swag_from
from flask import Blueprint, Response, jsonify, request

from app.config import BASE_ERROR_STATUS_CODE, BASE_SUCCESS_STRATUS_CODE
from app.response import get_unsorted_json_response
from app.utils import calculate_deposit
from app.validation import DepositRequestSchema
deposit_api = Blueprint("deposit_api", __name__)


@deposit_api.route("/calculate", methods=["POST"])
@swag_from("swagger.yml", validation=True)
def calculate() -> Union[Response, Tuple[Response, int]]:
    """
    Обрабатывает POST-запрос для расчета депозита.

    Получает данные JSON из запроса, валидирует их и, если данные корректны,
    вычисляет результат с помощью функции calculate_deposit.
    В случае успешного выполнения возвращает результат в виде JSON.
    Если данные некорректны или происходит ошибка,
    возвращает соответствующее сообщение об ошибке.

    Returns:
        Union[Response, Tuple[Response, int]]: JSON-ответ с результатом расчета депозита
        или сообщение об ошибке, и соответствующий HTTP статус-код.
    """
    data: Dict[str, Any] = request.get_json()

    # Валидация данных
    errors: str = DepositRequestSchema().validate(data)
    if errors:
        return (
            jsonify({"error": errors}),
            BASE_ERROR_STATUS_CODE,
        )

    try:
        # Вычисление депозита и возврат успешного ответа
        return get_unsorted_json_response(
            calculate_deposit(**data),
            BASE_SUCCESS_STRATUS_CODE,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), BASE_ERROR_STATUS_CODE
