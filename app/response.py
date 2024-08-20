import json
from typing import Any, Dict

from flask import Response


def get_unsorted_json_response(data: Dict[str, Any], status_code: int) -> Response:
    """
    Создает HTTP-ответ с несортированным JSON на основе предоставленных данных.

    Args:
        data (Dict[str, Any]): Данные для преобразования в JSON.
        Словарь, где ключи — строки, а значения могут быть любого типа.
        status_code (int): HTTP статус-код для ответа.

    Returns:
        Response:
        Объект ответа Flask с JSON, установленным MIME-типом и указанным статус-кодом.
    """
    return Response(
        json.dumps(
            data,
            indent=4,
            separators=(",", ": "),
            sort_keys=False,
        ),
        mimetype="application/json",
        status=status_code,
    )
